import pandas as pd
import numpy as np
import math
import time
from sklearn import preprocessing
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import roc_curve
from sklearn import svm
from sklearn.metrics import accuracy_score
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import KFold
import joblib
import config
import os
import xgboost


presult = None
n_thread = 8

# TODO: change the label name
label_name = "target"
df_columns = ['age', 'sex', 'CPT', 'RBP', 'SC', 'FBS', 'RER', 'MHRA', 'EIA', 'oldpeak', 'SOTPESTS', 'NOMV', 'thal', 'target']
columns_name = ["age", "sex", "chest pain type", "resting blood pressure", "serum cholestoral", "fasting blood sugar",\
                     "resting electrocardiographic results", "maximum heart rate achieved", "exercise induced angina",\
                     "oldpeak", "slope of the peak exercise ST segment", "number of major vessels", "thal", "target"]


# TODO: construct data for prediction
def construct_data():
    def bin(min, max, num=5):
        bin_val = (max - min) / num
        return [min + i * bin_val for i in range(num + 1)]

    data_df = pd.read_csv(config.TRAINING_DATA, header = None, na_values = '?')
    data_df.columns = df_columns

    num_col_list = ['age', 'RBP', 'SC', 'MHRA','oldpeak']
    cols_cate_feature_list = ['sex', 'CPT', 'RER', 'NOMV', 'thal','FBS','EIA','SOTPESTS']


    data_df = data_df.apply(lambda x: x.fillna(x.value_counts().index[0]))
    data_df['target'] = data_df['target'].apply(lambda x: 0 if x == 0 else 1)


    #============binning numerical data================#
    # label = [0, 1, 2,3,4]
    # for nc in num_col_list:
    #     print(data_df[nc].min(),data_df[nc].max())
    #     bin_l = bin(data_df[nc].min(), data_df[nc].max())
    #     data_df[nc] = pd.cut(data_df[nc], bins = bin_l, labels = label).astype(np.int)
    data_df[cols_cate_feature_list] = data_df[cols_cate_feature_list].astype('category')


    for nc in num_col_list:
        data_df[nc] = data_df[nc].apply(lambda x:(x - data_df[nc].min())/(data_df[nc].max()-data_df[nc].min()))

    # ============split training and evaluating data================#
    train_df,  eval_df = train_test_split(data_df, test_size = 0.1)

    train_x = train_df.drop(['target'], axis = 1)
    #train_x = pd.get_dummies(train_x)
    train_y = train_df['target']


    eval_x = eval_df.drop(['target'], axis=1)
    #eval_x = pd.get_dummies(eval_x)
    eval_y = eval_df['target']



    return train_x.values, train_y.values, eval_x.values, eval_y.values





def predict(df):
    def analyse(df):
        df_copy = df.copy()

        num_col_list = ['age', 'RBP', 'SC', 'MHRA', 'oldpeak']


        # ============================↑ data processing======================
        df_copy[label_name] = df_copy[label_name].apply(lambda x: 0 if x == 0 else 1)

        for nc in num_col_list:
            df_copy[nc] = df_copy[nc].apply(lambda x: (x - df_copy[nc].min()) / (df_copy[nc].max() - df_copy[nc].min()))

        y_test = df_copy[label_name]
        X_test = df_copy.drop([label_name], axis=1).values

        #X_test = pd.get_dummies(X_test).values

        model_0 = joblib.load(os.path.join(config.MODEL_DIR, "model_0"))
        model_1 = joblib.load(os.path.join(config.MODEL_DIR, "model_1"))
        model_2 = joblib.load(os.path.join(config.MODEL_DIR, "model_2"))
        model_3 = joblib.load(os.path.join(config.MODEL_DIR, "model_3"))
        model_4 = joblib.load(os.path.join(config.MODEL_DIR, "model_4"))
        model_5 = joblib.load(os.path.join(config.MODEL_DIR, "model_5"))

        predict_y_0_prob = model_0.predict_proba(X_test)[:,1]
        predict_y_1_prob = model_1.predict_proba(X_test)[:,1]
        predict_y_2_prob = model_2.predict_proba(X_test)[:,1]
        predict_y_3_prob = model_3.predict_proba(X_test)[:,1]
        predict_y_4_prob = model_4.predict(X_test)
        predict_y_5_prob = model_5.predict_proba(X_test)[:,1]



        re = np.array(predict_y_0_prob) + np.array(predict_y_1_prob) + np.array(predict_y_2_prob) + np.array(predict_y_3_prob) \
              + np.array(predict_y_4_prob) + np.array(predict_y_5_prob)
        re = re / 6


        # ===================↑predict==========================
        df["result_probability"] = re.round(5)

        return re, y_test, df

    def evaluate_model(df, coarse=100):
        df[label_name] = df[label_name].apply(lambda x: 0 if x == 0 else 1)
        n_records = len(df)
        percent_list = list(np.arange(1, coarse + 1) / coarse)
        total_num = df[label_name].sum()
        recall_list = []
        precise_list = []

        for percent in percent_list:
            n_sel_records = math.floor(n_records * percent)
            t1 = df.iloc[:n_sel_records]
            tp = t1[t1[label_name] == 1].shape[0]
            t2 = df.iloc[n_sel_records:]
            tn = t2[t2[label_name] == 0].shape[0]

            recall = tp / total_num
            recall_list.append(recall)
            precise = tp / (tp + tn)
            precise_list.append(precise)

        precision, recall, thresholds = precision_recall_curve(df[label_name], df["result_probability"])
        eval_result_df = pd.DataFrame()
        eval_result_df['recall'] = np.around(np.array(recall) * 100, decimals=2)
        eval_result_df['precise'] = np.around(np.array(precision) * 100, decimals=2)
        eval_result_df['thresholds'] = np.insert(thresholds,0, 0.0)

        fpr, tpr, thresholds = roc_curve(df[label_name], df["result_probability"])
        roc_result_df = pd.DataFrame()
        roc_result_df['fpr'] = np.around(np.array(fpr) * 100, decimals=2)
        roc_result_df['tpr'] = np.around(np.array(tpr) * 100,  decimals=2)
        roc_result_df['thresholds'] = thresholds

        return eval_result_df, roc_result_df



    print('Start modeling and predicting...')

    s = time.time()

    test_result, y_test, df_result = analyse(df)
    df_result = df_result.sort_values(by=["result_probability"], ascending=False)
    df_result.to_csv(config.RESULT_FILE, index=False)
    performance_eval = df_result[["result_probability",label_name]]
    eval_df, roc_df = evaluate_model(performance_eval, 100)
    eval_df.to_csv(config.EVAL_FILE, index=False)
    roc_df.to_csv(config.ROC_FILE, index=False)
    print("\nPrediction is done.")

    print("Time cost {}s".format(time.time() - s))

    df_result.fillna('',inplace = True)

    # TODO: set columns name map (column_name => shown_name) on config.py
    return df_result.values.tolist(), config.COLS_SHOW_MAP.keys()




# TODO: train model
def train():

    train_x, train_y, eval_x, eval_y = construct_data()


    model_0 = xgboost.XGBClassifier(
        learning_rate = 0.1,
        n_estimators = 100,
        max_depth = 9,
        min_child_weight = 1,
        gamma = 0,
        subsample = 0.1,
        colsample_bytree = 0.8,
        objective = 'binary:logistic',
        nthread = 8,
        scale_pos_weight = 1
    )

    model_1 = svm.SVC(C=1.0, kernel='rbf', degree=5, gamma='auto',
                    coef0=0.0, shrinking=True, probability=True,
                    tol=1e-3, cache_size=200, class_weight=None,
                    verbose=False, max_iter=-1, decision_function_shape='ovr',
                    random_state=None)



    model_2 = RandomForestClassifier(n_estimators = 150, n_jobs=-1 )




    model_3 = KNeighborsClassifier(n_neighbors=10)

    def get_model():
        model = Sequential()

        model.add(Dense(32, activation='relu', input_dim= 13))
        model.add(Dense(32, activation='relu'))
        #model.add(Dense(32, activation='relu'))
        model.add(Dense(2, activation='softmax'))

        optimizer = Adam(lr=1e-3)
        model.compile(
            loss='sparse_categorical_crossentropy',
            optimizer=optimizer,
            metrics=['accuracy']
        )
        return model

    model_4 = get_model()

    model_5 = MultinomialNB()

    model_0.fit(train_x, train_y)
    model_1.fit(train_x, train_y)
    model_2.fit(train_x, train_y)
    model_3.fit(train_x, train_y)
    model_4.fit(train_x, train_y, batch_size=16, epochs=20,verbose=0)
    model_5.fit(train_x, train_y)

    # ====================save model====================
    joblib.dump(model_0, os.path.join(config.MODEL_DIR, "model_0"))
    joblib.dump(model_0, os.path.join(config.MODEL_DIR, "model_1"))
    joblib.dump(model_0, os.path.join(config.MODEL_DIR, "model_2"))
    joblib.dump(model_0, os.path.join(config.MODEL_DIR, "model_3"))
    joblib.dump(model_0, os.path.join(config.MODEL_DIR, "model_4"))
    joblib.dump(model_0, os.path.join(config.MODEL_DIR, "model_5"))




    #====================generate feature importance====================
    importance = model_0.feature_importances_


    importance_dic = config.COLS_SHOW_MAP

    feature_description = pd.DataFrame.from_dict(importance_dic, orient= "index").reset_index()
    feature_description.columns = ["Feature", "Description"]
    feature_description.to_csv(os.path.join(config.STABLE_DIR, "feature_description.csv"))


    feature_importance = feature_description.copy()
    feature_importance.insert(loc = 1, column = "importance", value = importance)
    feature_importance.to_csv(os.path.join(config.STABLE_DIR, "feature_importance.csv"), index= None)


    predict_y_0 = model_0.predict(eval_x)
    predict_y_1 = model_1.predict(eval_x)
    predict_y_2 = model_2.predict(eval_x)
    predict_y_3 = model_3.predict(eval_x)
    predict_y_4 = model_4.predict(eval_x)
    predict_y_4 = predict_y_4.argmax(axis=1)
    predict_y_5 = model_5.predict(eval_x)




    re = np.array(predict_y_0)+np.array(predict_y_1)+  np.array(predict_y_2)+ np.array(predict_y_3)\
         + np.array(predict_y_4) + np.array(predict_y_5)
    re = map(lambda x:1 if x >= 3 else 0,re)
    l = list(re)
    # print(accuracy_score(eval_y, predict_y_0))
    # print(accuracy_score(eval_y, predict_y_1))
    # print(accuracy_score(eval_y, predict_y_2))
    # print(accuracy_score(eval_y, predict_y_3))
    # print(accuracy_score(eval_y, predict_y_4))
    # print(accuracy_score(eval_y, predict_y_5))
    # print(accuracy_score(eval_y,l))
    # print()
    # print()

    return accuracy_score(eval_y, l)



    '''
    # ============stacking================#
    stack_model = [model_0, model_1, model_2, model_3, model_4, model_5]

    ntrain = train_x.shape[0]  ## number of train data
    neval = eval_y.shape[0]  ## number of eval data
    train_stack = np.zeros((ntrain, 6))
    eval_stack = np.zeros((neval, 6))


    for i, model in enumerate(stack_model):
        if i == 4:
            train_stack[:, i] = model.predict(train_x)[:,1]
            eval_stack[:, i] = model.predict(eval_x)[:,1]

        else:
            train_stack[:, i] = model.predict_proba(train_x)[:,1]
            eval_stack[:, i] = model.predict_proba(eval_x)[:,1]
    # predict_y_0_prob = model_0.predict_proba(eval_x)
    # predict_y_1_prob = model_1.predict_proba(eval_x)
    # predict_y_2_prob = model_2.predict_proba(eval_x)
    # predict_y_3_prob = model_3.predict_proba(eval_x)
    # predict_y_4_prob = model_4.predict(eval_x)
    # predict_y_5_prob = model_4.predict(eval_x)



    stack_model = RandomForestClassifier(n_estimators = 150, n_jobs=-1 )
    stack_model.fit(train_stack, train_y)
    stack_predict = stack_model.predict(eval_stack)
    return accuracy_score(eval_y, stack_predict)
    '''




if __name__ == '__main__':
    train()