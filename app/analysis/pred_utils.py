import pandas as pd
from ast import literal_eval
import copy
import numpy as np
import math
import dask
from dask import dataframe as dd
import time
from sklearn import preprocessing
from xgboost.sklearn import XGBClassifier
from app.analysis.server_side_datatable import collect_data_serverside

import config
import os
import xgboost

presult = None
num_boost_round = 150
# num_boost_round = 200
n_thread = -1
label_name = "Failed"

# columns not in result df (but used in predict)
cols_not_presented_list = ["Probability", "Waterway", "LS", "Highly_Corrosive", "Corrosive"
    , "None_Corrosive", "Above_Ground", "Encased_in_Pipe", "In_Tunnel", "Standard_Depth", "Tunnel_Portals"
    , "FWY_CW", "FWY_RR", "MjR_CW_Dual", "MjR_RR_Dual", "MjR_CW_Single", "MjR_RR_Single", "MiR_CW", "MiR_RR", "RW_Coal"
    , "RW_Goods", "RW_LR", "RW_Link", "RW_MaL", "RW_MiL", "RW_Siding", "RW_Tourist", "LU_CBD1", "LU_CBD2", "LU_IndComm"
    , "LU_Resid", "LU_Hosp", "LU_Air",
                           ]

feature_count_in_tool_results = 5
feature_list_in_tool_results = ["#_failures", "horizontal_length", "age", "pipe_type", "pipe_size"]




def construct_training_testing_datas(csv_data_swc: str, csv_data_tool: str, predict_year: int,renew_model:bool):
    """

    :param csv_data_swc: path to processed data file
    :param csv_data_tool: path to previous tool results
    :param predict_year: year to predict, generate training data from 2000 to (predict_year-1)
    :param renew_model: flag for renew model
    :return: No return
    """

    assert (predict_year > 2000)
    if renew_model:
        observation_years = list(range(2000, predict_year + 1))
    else:
        if os.path.isfile(os.path.join(config.MODEL_PATH,'xgb_%s.model' % predict_year)):
            observation_years = list(range(2000, predict_year + 1))
            print("Model found.")
        else:
            print("Model for %s year not found, retrain the model for %s year by uploaded file."%(predict_year,predict_year))
            observation_years = list(range(2000, predict_year + 1))
            renew_model = True


    def gen_cumsum(x):
        scope = set(x['reportdates_break'])
        if len(scope) == 0:
            return [0] * len(x['all_years'])
        return list(np.cumsum(list(map(lambda x: (x - 1) in scope, x['all_years']))))

    def gen_onehot(x):
        scope = set(x['reportdates_break'])
        if len(scope) == 0:
            return [0] * len(x['all_years'])
        return list(map(lambda x: int(x in scope), x['all_years']))

    def y_s_f_zip(x):
        return list(zip(x['all_years'], x['his_cumsum'], x['onehot_fail']))


    # =================↑ applied functions and variable============

    df_tool_result = pd.read_csv(csv_data_tool)
    df_swc = pd.read_csv(csv_data_swc, low_memory=False,dtype={'shutdown_block_id':np.int})
    df_swc['shutdown_block_id'] = df_swc['shutdown_block_id'].astype(np.str)
    #print(df_swc['shutdown_block_id'])

    # ==================↑ read data===================

    # tqdm.pandas(desc="processing stage0")
    df_swc['reportdates_break'] = df_swc['reportdates_break'].apply(literal_eval)

    df_swc['all_years'] = [observation_years for _ in range(len(df_swc.index))]

    df_swc['his_cumsum'] = df_swc[['reportdates_break', 'all_years']].apply(gen_cumsum, axis=1)

    df_swc['onehot_fail'] = df_swc[['reportdates_break', 'all_years']].apply(gen_onehot, axis=1)

    df_swc['y_s_f_zip'] = df_swc.apply(y_s_f_zip, axis=1)
    df_swc.drop(columns=['all_years', 'his_cumsum', 'onehot_fail', 'reportdates_break'], inplace=True)

    df_melt = df_swc['y_s_f_zip'].apply(pd.Series).reset_index().melt(id_vars='index')[['index', 'value']]
    df_swc.drop(columns=['y_s_f_zip'], inplace=True)
    df_swc = pd.merge(df_melt, df_swc, how='left', left_on='index', right_index=True)

    df_swc = df_swc.assign(**pd.DataFrame(df_swc["value"].values.tolist()).rename(
        columns={0: 'observation_year', 1: "#_failures", 2: 'Failed'}))
    df_swc.drop(columns=['value', 'index'], inplace=True)
    df_swc['age'] = df_swc["observation_year"] - df_swc["laid_year"]

    # ================↑ process and merge====================
    cat_list = []
    if not renew_model:
        df_tool_result_year = df_tool_result[["Probability_{}:Float".format(predict_year), "AssetPipeID"]]
        df_tool_result_year = df_tool_result_year.rename(
            columns={"Probability_{}:Float".format(predict_year): 'Probability', 'AssetPipeID': 'pipes'})
        df_training_data_year = df_swc[df_swc["observation_year"] == predict_year]
        df_merge = dask.delayed(pd.merge)(df_training_data_year, df_tool_result_year, on='pipes', how='inner')
        cat_list.append(df_merge)
        df_new = pd.concat(dask.compute(*cat_list), sort=True)

    else:
        cat_list = []
        for y in range(2001, predict_year + 1):
            df_tool_result_year = df_tool_result[["Probability_{}:Float".format(y), "AssetPipeID"]]
            df_tool_result_year = df_tool_result_year.rename(
                columns={"Probability_{}:Float".format(y): 'Probability', 'AssetPipeID': 'pipes'})
            df_training_data_year = df_swc[df_swc["observation_year"] == y]
            df_merge = dask.delayed(pd.merge)(df_training_data_year, df_tool_result_year, on='pipes', how='inner')
            cat_list.append(df_merge)
        df_new = pd.concat(dask.compute(*cat_list), sort=True)

    # ================↑ final merge with tool_result by years (can be speeded up by parallel)====================



    return df_new


def analyse(df, cols_removed, cols_cate_feature_list, file_fi, cohort_index, df_fe, predict_year, renew_model):

    if not renew_model and not os.path.isfile(os.path.join(config.MODEL_PATH,'xgb_%s.model' % predict_year)):
        renew_model = True

    df = df.rename(columns={'G_Pressure': 'g_pressure', "P_Pressure": "p_pressure"})

    # select data from df by pipe_size
    if cohort_index == 1:
        df = df[df["pipe_size"] < 300]
    elif cohort_index == 2:
        df = df[df["pipe_size"] >= 300]
        df = df[df["pipe_size"] < 375]
    elif cohort_index == 3:
        df = df[df["pipe_size"] >= 375]

    df = df.rename(columns={"pipe_type": "material", "lag": "latitude", "long": "longitude"})
    df_copy = df.copy()

    # encode the category columns as [0,1,...]
    for c_f in cols_cate_feature_list:
        df[c_f] = df[c_f].astype("category")
        lbe = preprocessing.LabelEncoder()
        _tem = list(df[c_f].values)
        lbe.fit(_tem)
        df[c_f] = lbe.transform(_tem)
    # ============================↑ data processing======================

    """
    needed config：
        max year of observation data 
    """

    if renew_model:

        df_train = df[df["observation_year"] <= predict_year - 1]
        df_test = df[df["observation_year"] == predict_year]
        df_test_copy = df_copy[df_copy["observation_year"] == (predict_year)].copy()

        y_train = df_train[label_name]
        X_train = df_train.drop(cols_removed, axis=1)

        y_test = df_test[label_name]
        X_test = df_test.drop(cols_removed, axis=1)

        xgb1 = XGBClassifier(n_jobs=n_thread,
                             silent=1,
                             objective="binary:logistic",
                             n_estimators=num_boost_round,
                             learning_rate=0.01,
                             # learning_rate=0.1,
                             min_child_weight=0,
                             max_depth=5,
                             gamma=0,
                             subsample=0.8,
                             # subsample=0.7,
                             colsample_bytree=0.7,
                             reg_lambda=1,
                             reg_alpha=0,
                             seed=1)
        xgb1.fit(X_train, y_train)

        xgb1.save_model(os.path.join(config.MODEL_PATH,'xgb_%s.model'%predict_year))
        print("finish modeling, model save as xgb_%s.model"%predict_year)

    else:
        df_test = df[df["observation_year"] == predict_year]
        df_test_copy = df_copy[df_copy["observation_year"] == (predict_year)].copy()
        y_test = df_test[label_name]
        X_test = df_test.drop(cols_removed, axis=1)
        xgb1 = xgboost.XGBClassifier({'nthread': n_thread},seed=1)
        xgb1.load_model(os.path.join(config.MODEL_PATH,'xgb_%s.model' % predict_year))

    # train xgboost


    # ====================↑training model=========================

    if renew_model:
        # Print the name and gini importance of each feature in decreasing order
        col_names = X_test.columns.values

        importance = copy.deepcopy(xgb1.feature_importances_)
        mean_prob = 0

        """
        mean the gini importance of feature "Probability" and allocate tham to 5 features?????
        than generate the file to log the importance of feature via importance from high to low
        """
        for i_fi in range(X_test.shape[1]):
            if col_names[i_fi] == "Probability":
                mean_prob = importance[i_fi] / feature_count_in_tool_results
                break

        for i_fi in range(X_test.shape[1]):
            if col_names[i_fi] in feature_list_in_tool_results:
                importance[i_fi] += mean_prob

        idx = np.argsort(importance)[::-1]

        for i_fi in range(X_test.shape[1]):
            if col_names[idx[i_fi]] in cols_not_presented_list:
                continue
            feature_explanation = df_fe.loc[col_names[idx[i_fi]]]["Description"]
            if pd.isnull(feature_explanation):
                feature_explanation = ""

            str_fi_out = "{},{},{}\n".format(col_names[idx[i_fi]],
                                             str(importance[idx[i_fi]]),
                                             feature_explanation)  # "test year,cohort,feature,importance\n"
            file_fi.write(str_fi_out)

        file_fi.close()

    # ===================↑write importance of feature file==========================

    test_result = xgb1.predict_proba(X_test)[:, 1]

    # ===================↑predict==========================
    df_test_copy["fail_probability"] = test_result
    df_test_copy = df_test_copy.drop(cols_not_presented_list, axis=1)
    tool_prob = df_test["Probability"] # column of tool feature
    pipes_col = df_test["pipes"] #

    return test_result, y_test, xgb1, pipes_col, tool_prob, df_test_copy


def predict(df, predict_year, feat_importance_file, pred_result_file, renew_model: bool):

    print('Start modeling and predicting...')

    s = time.time()

    cols_cate_feature_list = ['lga', 'material']

    df_fe = pd.read_csv(config.FEAT_DESC_FILE, index_col="Feature")

    if not renew_model and not os.path.isfile(os.path.join(config.MODEL_PATH,'xgb_%s.model' % predict_year)):
        renew_model = True

    if renew_model:
        file_fi = open(feat_importance_file, "w")
        file_fi_header = "feature,importance,description\n"
        file_fi.write(file_fi_header)
    else:
        file_fi = None

    cols_removed = ["observation_year", "pipes", "Failed",'shutdown_block_id','trunk_main_name','trunk_main_number']

    cohort_index = 4

    # =================↑ input var gen====================

    df_analyze, y_test, xgb, pipes_col, tool_prob, df_result = analyse(df=df,
                                                                        predict_year=predict_year,
                                                                        cols_removed=cols_removed,
                                                                        cols_cate_feature_list=cols_cate_feature_list,
                                                                        file_fi=file_fi,
                                                                        cohort_index=cohort_index,
                                                                        df_fe=df_fe,
                                                                        renew_model=renew_model)
    print('done!')

    # =================↑ modeling and prediection===============

    df_result['Failed'] = y_test

    df_result = df_result.sort_values(by=["fail_probability"], ascending=False)

    # construct df for analyse performance of model
    priority_list = df_result.copy()

    df_result = df_result.drop(["Failed"], axis=1)
    df_result = df_result.drop(["observation_year"], axis=1)
    # df_result.to_csv("../output/probability.csv", index=False)
    df_result.to_csv(pred_result_file, index=False)

    # save priority_list for analyse performance of model
    priority_list.to_csv(config.ResultFilesPaths(int(predict_year)).PRI_LIST_ALL_FILE, index=False)
    priority_list[priority_list["pipe_size"] >= 375].to_csv(
        config.ResultFilesPaths(int(predict_year)).PRI_LIST_375_FILE, index=False)

    performance_eval = priority_list[["fail_probability","Failed"]]
    performance_eval_375 = priority_list[priority_list["pipe_size"] >= 375][["fail_probability", "Failed"]]

    eval_df = evaluate_model(performance_eval, 100)
    eval_375_df = evaluate_model(performance_eval_375, 100)

    eval_df.to_csv(config.ResultFilesPaths(int(predict_year)).EVAL_FILE, index=False)
    eval_375_df.to_csv(config.ResultFilesPaths(int(predict_year)).EVAL_375_FILE, index=False)

    print("\nPrediction is done.")

    print("Time cost {}s".format(time.time() - s))

    df_trunk, df_shutdown = get_trunk_shutdownblock_eval(df_result)

    df_trunk.rename(columns={0:'fail_probability'},inplace=True)
    df_shutdown.rename(columns={0: 'fail_probability'}, inplace=True)

    df_trunk.sort_values(by=['fail_probability'],inplace=True,ascending=False)
    df_shutdown.sort_values(by=['fail_probability'],inplace=True,ascending=False)

    df_shutdown['shutdown_block_id'] = df_shutdown['shutdown_block_id'].astype(str)

    #print(df_shutdown.dtypes)

    df_trunk.to_csv(config.ResultFilesPaths(int(predict_year)).TRUNK_FILE,index=False)
    df_shutdown.to_csv(config.ResultFilesPaths(int(predict_year)).SHUTDOWN_BOLCK_FILE,index=False)

    df_result.fillna('',inplace = True)



    return df_result[config.SEL_COLS.keys()].values.tolist(), config.SEL_COLS.keys()


def evaluate_model(df, coarse=100):
    n_records = len(df)
    percent_list = list(np.arange(1, coarse+1) / coarse)
    total_failure = df["Failed"].sum()

    detection_rate_list = []

    for percent in percent_list:
        n_sel_records = math.floor(n_records * percent)
        detection_rate = df.iloc[:n_sel_records]['Failed'].sum() / total_failure
        detection_rate_list.append(detection_rate)

    eval_result_df = pd.DataFrame()
    eval_result_df['inspection percent (%)'] = np.array(percent_list) * 100
    eval_result_df['detection rate (%)'] = np.array(detection_rate_list) * 100

    return eval_result_df


def get_result_history(year):
    if os.path.isfile(config.ResultFilesPaths(year).PRED_RESULT_FILE):
        print('have result')
        df = pd.read_csv(config.ResultFilesPaths(year).PRED_RESULT_FILE)[config.SEL_COLS.keys()]
        df = df.fillna("")
        return df.values.tolist(),list(config.SEL_COLS.keys())

    else:
        print('on result')
        return None, None


def get_trunk_shutdownblock_eval(df):
    """
    :param df: result data frame
    :return: two df, trunk and shutdowblock pivot
    """

    df_trunk = df.copy()[df['trunk_main_number'].notnull()]
    df_sb = df[df['shutdown_block_id'].notnull()]

    df_sb['shutdown_block_id'] = df_sb['shutdown_block_id'].astype(str)

    re_trunk = dd.from_pandas(df_trunk,npartitions=8).groupby('trunk_main_number')['fail_probability'].apply(block_eval,meta=('int')).compute(scheduler='processes')
    re_sb = dd.from_pandas(df_sb,npartitions=8).groupby('shutdown_block_id')['fail_probability'].apply(block_eval,meta=('int')).compute(scheduler='processes')

    re_trunk = re_trunk.reset_index()
    re_sb = re_sb.reset_index()






    return re_trunk, re_sb

def block_eval(ser):
    """
    :param p: series of failure propability on same block/trunk
    :return:
    """
    #print(type(ser))
    return 1 - np.prod(np.array(1-ser))

