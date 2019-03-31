import pandas as pd
from dask import dataframe as dd

import config


def check_file_formats(filepath, file_type):
    """

        check if the format is valid given the filepath and file_type

        PARAM:
            filepath: path of the file
            file_type: 'water_mains', 'failures'
    """
    data_df = pd.read_csv(filepath, nrows=5)
    cols = data_df.columns.tolist()
    format_cols = config.FILE_FORMATS[file_type]

    if len(format_cols) != 0:
        return set(format_cols).issubset(set(cols))
    else:
        return True


def _combine_features(row):
    if row["pipe_size"] < 300:
        row["Bulk Density"] = row["Bulk Density (30-60cm)"]
        row["Organic Carbon of soil"] = row["Organic Carbon of soil (30-60cm)"]
        row["Clay content of soil"] = row["Clay content of soil (30-60cm)"]
        row["Silt of soil"] = row["Silt of soil (30-60cm)"]
        row["Sand"] = row["Sand_30-60"]
        row["pH CaCl2 of soil"] = row["pH CaCl2 of soil (30-60cm)"]
        row["Total Nitrogen of soil"] = row["Total Nitrogen of soil (30-60cm)"]
        row["Total Phosphorus of soil"] = row["Total Phosphorus of soil (30-60cm)"]
        row["Available Water Capacity of soil"] = row["Available Water Capacity of soil (30-60cm)"]
        row["Effective Cation Exchange Capacity of soil"] = row["Effective Cation Exchange Capacity of soil (30-60cm)"]
    else:
        row["Bulk Density"] = row["Bulk Density (60-100cm)"]
        row["Organic Carbon of soil"] = row["Organic Carbon of soil (60-100cm)"]
        row["Clay content of soil"] = row["Clay content of soil (60-100cm)"]
        row["Silt of soil"] = row["Silt of soil (60-100cm)"]
        row["Sand"] = row["Sand_60-100"]
        row["pH CaCl2 of soil"] = row["pH CaCl2 of soil (60-100cm)"]
        row["Total Nitrogen of soil"] = row["Total Nitrogen of soil (60-100cm)"]
        row["Total Phosphorus of soil"] = row["Total Phosphorus of soil (60-100cm)"]
        row["Available Water Capacity of soil"] = row["Available Water Capacity of soil (60-100cm)"]
        row["Effective Cation Exchange Capacity of soil"] = row["Effective Cation Exchange Capacity of soil (60-100cm)"]
    return row


def construct_processed_data(info_pipe_path: str,
                             info_GL_path: str,
                             info_pressure_path: str,
                             info_fail_path: str,
                             info_EM_path: str,
                             info_soil_path: str,
                             info_topology_path:str,
                             saved_result_path: str):
    """

    :param info_pipe_path: path to pipe info file
    :param info_GL_path: path to GL info file
    :param info_pressure_path: path to pressure info file
    :param info_fail_path: path to failure info file
    :param info_EM_path: path to EMData.xml
    :param info_soil_path: path to Whole_data_new_soil_Dilusha.csv
    :param info_topology_path: path to topology file
    :param saved_result_path: path for saving result
    :return:
    """


    # ground level noisy data processing

    gl_df = pd.read_csv(info_GL_path, low_memory=False)
    pressure_df = pd.read_csv(info_pressure_path, low_memory=False)
    pipe_df = pd.read_csv(info_pipe_path, low_memory=False,dtype={'shutdown_block_id':str})
    fail_df = pd.read_csv(info_fail_path, low_memory=False)
    df_topology = pd.read_csv(info_topology_path, low_memory=False)
    df_soil_numerical = pd.read_csv(info_soil_path, index_col="sgan")
    soil_categorical_cols_list = ["Waterway", "LS", "Highly_Corrosive", "Corrosive", "None_Corrosive"
        , "Above_Ground", "Encased_in_Pipe", "In_Tunnel", "Standard_Depth", "Tunnel_Portals", "FWY_CW"
        , "FWY_RR", "MjR_CW_Dual", "MjR_RR_Dual", "MjR_CW_Single", "MjR_RR_Single", "MiR_CW", "MiR_RR", "RW_Coal"
        , "RW_Goods", "RW_LR", "RW_Link", "RW_MaL", "RW_MiL", "RW_Siding", "RW_Tourist", "LU_CBD1", "LU_CBD2"
        , "LU_IndComm", "LU_Resid", "LU_Hosp", "LU_Air"]

    df_soil_categorical = pd.read_csv(info_EM_path,
                                      usecols=['system_generated_asset_number'] + soil_categorical_cols_list,
                                      index_col="system_generated_asset_number")

    gl_df.loc[gl_df['meanGL'] < -10, 'meanGL'] = -10

    # =======================↑ read data===================================



    pressure_df = pressure_df[['G_Pressure', 'P_Pressure', 'pipes']].copy().dropna()

    # convert report years to finance year and record in df fail_break_years_df
    fail_break_df = fail_df.loc[fail_df['TASK_CODE'] == "WR1A", ['ASSET_NUMBER', 'WORKORDER_REPORTED_DATE']].copy()
    fail_break_df['ASSET_NUMBER'] = pd.to_numeric(fail_break_df['ASSET_NUMBER'], errors='coerce')
    fail_break_df = fail_break_df.dropna(subset=['ASSET_NUMBER'])
    fail_break_df.rename(columns={'ASSET_NUMBER': 'pipes'}, inplace=True)
    fail_break_df['WORKORDER_REPORTED_DATE'] = pd.to_datetime(fail_break_df['WORKORDER_REPORTED_DATE'], format='%Y%m%d',
                                                              errors='ignore')
    fail_break_df['f_year'] = dd.from_pandas(fail_break_df['WORKORDER_REPORTED_DATE'], npartitions=8).map_partitions(
        lambda s: s.apply(lambda x: x.year if x.month >= 7 else (x.year - 1))).compute(scheduler='processes')
    group_series = fail_break_df.groupby('pipes')['f_year'].apply(list)
    fail_break_years_df = pd.DataFrame({"pipes": group_series.index,
                                        "reportdates_break": group_series}).reset_index(drop=True)
    fail_break_years_df['pipes'] = fail_break_years_df['pipes'].astype('int64')

    # # filter by critical
    pipe_df = pipe_df[pipe_df['critical'] == 'Yes']

    # filter by size
    # pipe_df = pipe_df[pipe_df['pipe_size'] >= 250]

    # get needed columns from pipe_df
    pipe_need_df = pipe_df[
        ['system_generated_asset_number', 'lga', 'pipe_type', 'pipe_size', 'laid_year','trunk_main_name','trunk_main_number','shutdown_block_id']].copy()

    pipe_need_df.rename(columns={'system_generated_asset_number': 'pipes'}, inplace=True)

    # ============================== ↑ preprocessing===========================


    pressure_GL_merge_df = pd.merge(gl_df, pressure_df, on='pipes')
    temp1 = pd.merge(pressure_GL_merge_df, pipe_need_df, how='inner', on='pipes')

    df_soil_categorical_new = pd.merge(df_soil_numerical, df_soil_categorical, left_index=True, right_index=True,
                                       how='inner').reset_index().rename(columns={"index": "pipes"})

    temp2 = pd.merge(df_soil_categorical_new, temp1, on='pipes', how='inner')
    result = pd.merge(temp2, fail_break_years_df, how='left', on='pipes')

    result = pd.merge(result,df_topology,how='left',on='pipes').reset_index(drop=True)
    # ========================== ↑ merge all df====================

    features_new = ["Bulk Density",
                    "Organic Carbon of soil",
                    "Clay content of soil",
                    "Silt of soil",
                    "Sand", "Sand",
                    "pH CaCl2 of soil",
                    "Total Nitrogen of soil",
                    "Total Phosphorus of soil",
                    "Available Water Capacity of soil",
                    "Effective Cation Exchange Capacity of soil"]

    for feature in features_new:
        result[feature] = 0

    # use Dask to parallel process data
    result = dd.from_pandas(result, npartitions=config.NUM_CORES). \
        map_partitions(
        lambda df: df.apply(_combine_features, axis=1)). \
        compute(scheduler='processes')

    cols_removed = ["Bulk Density (30-60cm)", "Bulk Density (60-100cm)",
                    "Organic Carbon of soil (30-60cm)", "Organic Carbon of soil (60-100cm)",
                    "Clay content of soil (30-60cm)", "Clay content of soil (60-100cm)",
                    "Silt of soil (30-60cm)", "Silt of soil (60-100cm)",
                    "Sand_30-60", "Sand_60-100",
                    "pH CaCl2 of soil (30-60cm)", "pH CaCl2 of soil (60-100cm)",
                    "Total Nitrogen of soil (30-60cm)", "Total Nitrogen of soil (60-100cm)",
                    "Total Phosphorus of soil (30-60cm)", "Total Phosphorus of soil (60-100cm)",
                    "Available Water Capacity of soil (30-60cm)", "Available Water Capacity of soil (60-100cm)",
                    "Effective Cation Exchange Capacity of soil (30-60cm)",
                    "Effective Cation Exchange Capacity of soil (60-100cm)"]
    result = result.drop(cols_removed, axis=1)
    result['reportdates_break'] = result['reportdates_break'].apply(lambda x: x if isinstance(x, list) else [])

    # ==========================final processing result=================

    result.to_csv(saved_result_path, index=False)

