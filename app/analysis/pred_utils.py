import pandas as pd
import numpy as np
import math
import time
from sklearn import preprocessing
import config
import os
import xgboost

presult = None
n_thread = 8

# TODO: change the label name
label_name = "Failed"


# TODO: construct data for prediction
def construct_data():
    pass


def predict(df):
    def analyse(df, cols_cate_feature_list):

        df_copy = df.copy()

        # encode the category columns as [0,1,...]
        for c_f in cols_cate_feature_list:
            df[c_f] = df[c_f].astype("category")
            lbe = preprocessing.LabelEncoder()
            _tem = list(df[c_f].values)
            lbe.fit(_tem)
            df[c_f] = lbe.transform(_tem)
        # ============================↑ data processing======================


        y_test = df[label_name]
        X_test = df.drop([label_name], axis=1)
        xgb1 = xgboost.XGBClassifier({'nthread': n_thread}, seed=1)
        xgb1.load_model(os.path.join(config.MODEL_PATH))
        test_result = xgb1.predict_proba(X_test)[:, 1]

        # ===================↑predict==========================
        df_copy["result_probability"] = test_result

        return test_result, y_test, xgb1, df_copy

    def evaluate_model(df, coarse=100):
        n_records = len(df)
        percent_list = list(np.arange(1, coarse + 1) / coarse)
        total_failure = df[label_name].sum()
        detection_rate_list = []

        for percent in percent_list:
            n_sel_records = math.floor(n_records * percent)
            detection_rate = df.iloc[:n_sel_records][label_name].sum() / total_failure
            detection_rate_list.append(detection_rate)

        eval_result_df = pd.DataFrame()
        eval_result_df['inspection percent (%)'] = np.array(percent_list) * 100
        eval_result_df['detection rate (%)'] = np.array(detection_rate_list) * 100

        return eval_result_df



    print('Start modeling and predicting...')

    s = time.time()

    # TODO: change the category label name
    cols_cate_feature_list = ['lga', 'material']


    test_result, y_test, xgb, df_result = analyse(df=df, cols_cate_feature_list=cols_cate_feature_list)
    df_result = df_result.sort_values(by=["result_probability"], ascending=False)
    df_result.to_csv(config.RESULT_FILE, index=False)
    performance_eval = df_result[["result_probability",label_name]]
    eval_df = evaluate_model(performance_eval, 100)
    eval_df.to_csv(config.EVAL_FILE, index=False)
    print("\nPrediction is done.")

    print("Time cost {}s".format(time.time() - s))

    df_result.fillna('',inplace = True)

    # TODO: set columns name map (column_name => shown_name) on config.py
    return df_result.values.tolist(), config.COLS_SHOW_MAP.keys()


# TODO: train model
def train():
    pass


