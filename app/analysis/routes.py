from app.analysis import pred_utils
from flask import render_template, redirect, url_for, request, jsonify, send_from_directory, session
import pandas as pd
import os
import config
from flask import Flask
from logging import basicConfig, DEBUG, getLogger, StreamHandler

app = Flask(__name__,template_folder='templates',static_folder='static')
basicConfig(filename='error.log', level=DEBUG)
logger = getLogger()
logger.addHandler(StreamHandler())

df_columns = ['age', 'sex', 'CPT', 'RBP', 'SC', 'FBS', 'RER', 'MHRA', 'EIA', 'oldpeak', 'SOTPESTS', 'NOMV', 'thal', 'target']
age_bins = ["0-29", "30-34", "35-39", "40-44", "45-49", "50-54", "55-59", "60-64", "65-69", "70-74", "75-100"]


@app.route('/')
def index():
    return redirect(url_for('data_management'))


@app.route('/data_management')
def data_management():
    return render_template('data_management.html')


@app.route('/data_management/get_eval_results', methods=['GET'])
def get_eval_results():
    # init return message
    #year = int(request.form["cur_year"])
    #print('curretn_year:'+str(year))

    return_msg = dict()
    if os.path.isfile(config.EVAL_FILE) and os.path.isfile(config.ROC_FILE):
        eval_results_df = pd.read_csv(config.EVAL_FILE)
        roc_result_df = pd.read_csv(config.ROC_FILE)
        json_eval_results = eval_results_df.transpose().to_json(orient='split')
        roc_result_df = roc_result_df.transpose().to_json(orient='split')

        return_msg['data'] = [json_eval_results, roc_result_df]
        return_msg['message'] = 'DONE'
    else:
        return_msg['data'] = ''
        return_msg['message'] = 'fail'

    return jsonify(return_msg)


@app.route('/data_management/upload', methods=['POST'])
def upload_files():
    """
        upload data files
    """
    # init return message
    return_msg = dict()

    # get files
    file = request.files['file_name']

    # specify file path to save
    file_path = os.path.join(config.UPLOAD_DIR, 'train.data')


    # save files
    file.save(file_path)

    return_msg['message'] = 'DONE'
    return jsonify(return_msg)


@app.route('/data_management/predict', methods=['POST'])
def do_prediction():
    """
        Perform prediction based on selected year
    """
    # init return message
    return_msg = dict()

    # generate training/test data
    # TODO: impliment construct data function
    #df = pred_utils.construct_data()
    data_df = pd.read_csv(config.TRAINING_DATA, header = None, na_values = '?')
    data_df.columns = df_columns

    # do prediction
    data_list, columns_list = pred_utils.predict(data_df)

    c_n_m = config.COLS_SHOW_MAP
    feat_importance_df = pd.read_csv(config.FEAT_IMPORTANCE_FILE)
    feat_importance_df = feat_importance_df[['Feature','importance']]
    json_feat_importance = feat_importance_df.transpose().to_json(orient='split')
    return_msg['feat_importance'] = json_feat_importance
    return_msg['message'] = 'DONE'
    return_msg['columns'] = [c for c in [c_n_m[sc] for sc in columns_list]]
    return_msg['data'] = data_list

    return jsonify(return_msg)


@app.route('/traing_data_visialize')
def gis_data_layer():
    return render_template('traing_data_visialize.html')


@app.route('/download/<path:filename>')
def download_file(filename):
    return send_from_directory(config.OUTPUT_DIR, filename, as_attachment=True, cache_timeout=0)

@app.route('/traing_data_visialize/CPT', methods=['GET'])
def provide_data_to_show_CPT():
    attr_name = "CPT"
    gender =[1,0]
    classes = [1,2,3,4]
    data_df = pd.read_csv(config.TRAINING_DATA, header = None, na_values = '?')
    data_df.columns = df_columns
    data_df = data_df.apply(lambda x: x.fillna(x.value_counts().index[0]))
    data_df['age_range'] = pd.cut(x=data_df['age'], bins=len(age_bins), labels=age_bins)
    data_df = data_df[['sex','attr_name','age_range']]
    result = []
    for g in gender:
        cur_gender = []
        cur_df = data_df[data_df["sex"] == g][["age_range", attr_name]]
        for c in classes:
            cur_class = cur_df[cur_df[attr_name] == c]
            cur_class = cur_class.groupby(['age_range']).age_range.agg('count').to_frame('count').reset_index()
            cur_class['count'] = cur_class['count'].replace(0, "-")
            cur_gender.append(cur_class['count'].values.tolist())
        result.append(cur_gender)
    return jsonify({ "message" : "successful!" , "data": result})

@app.route('/traing_data_visialize/RBP', methods=['GET'])
def provide_data_to_show_RBP():
    attr_name = "RBP"
    data_df = pd.read_csv(config.TRAINING_DATA, header = None, na_values = '?')
    data_df.columns = df_columns
    data_df = data_df.apply(lambda x: x.fillna(x.value_counts().index[0]))
    data_df_m = data_df[data_df["sex"] == 1][["age", attr_name]]
    data_df_f = data_df[data_df["sex"] == 0][["age", attr_name]]
    data_df_m = data_df_m.groupby(['age',attr_name]).age.agg('count').to_frame('count').reset_index()
    data_df_f = data_df_f.groupby(['age',attr_name]).age.agg('count').to_frame('count').reset_index()
    result = [data_df_m[["age", attr_name, "count"]].values.tolist(), data_df_f[["age", attr_name, "count"]].values.tolist()]

    
    return jsonify({ "message" : "successful!" , "data": result})

@app.route('/traing_data_visialize/SC', methods=['GET'])
def provide_data_to_show_SC():
    attr_name = "SC"
    data_df = pd.read_csv(config.TRAINING_DATA, header = None, na_values = '?')
    data_df.columns = df_columns
    data_df = data_df.apply(lambda x: x.fillna(x.value_counts().index[0]))
    data_df_m = data_df[data_df["sex"] == 1][["age", attr_name]]
    data_df_f = data_df[data_df["sex"] == 0][["age", attr_name]]
    data_df_m = data_df_m.groupby(['age',attr_name]).age.agg('count').to_frame('count').reset_index()
    data_df_f = data_df_f.groupby(['age',attr_name]).age.agg('count').to_frame('count').reset_index()
    result = [data_df_m[["age", attr_name, "count"]].values.tolist(), data_df_f[["age", attr_name, "count"]].values.tolist()]
    return jsonify({ "message" : "successful!" , "data": result})



@app.route('/traing_data_visialize/FBS', methods=['GET'])
def provide_data_to_show_FBS():
    attr_name = "FBS"
    gender =[1,0]
    classes = [0,1]
    data_df = pd.read_csv(config.TRAINING_DATA, header = None, na_values = '?')
    data_df.columns = df_columns
    data_df = data_df.apply(lambda x: x.fillna(x.value_counts().index[0]))
    data_df['age_range'] = pd.cut(x=data_df['age'], bins=len(age_bins), labels=age_bins)
    data_df = data_df[['sex',attr_name,'age_range']]
    result = []
    for g in gender:
        cur_gender = []
        cur_df = data_df[data_df["sex"] == g][["age_range", attr_name]]
        for c in classes:
            cur_class = cur_df[cur_df[attr_name] == c]
            cur_class = cur_class.groupby(['age_range']).age_range.agg('count').to_frame('count').reset_index()
            cur_class['count'] = cur_class['count'].replace(0, "-")
            cur_gender.append(cur_class['count'].values.tolist())
        result.append(cur_gender)
    return jsonify({ "message" : "successful!" , "data": result})

@app.route('/traing_data_visialize/RER', methods=['GET'])
def provide_data_to_show_RER():
    attr_name = "RER"
    gender =[1,0]
    classes = [0,1,2]
    data_df = pd.read_csv(config.TRAINING_DATA, header = None, na_values = '?')
    data_df.columns = df_columns
    data_df = data_df.apply(lambda x: x.fillna(x.value_counts().index[0]))
    data_df['age_range'] = pd.cut(x=data_df['age'], bins=len(age_bins), labels=age_bins)
    data_df = data_df[['sex',attr_name,'age_range']]
    result = []
    for g in gender:
        cur_gender = []
        cur_df = data_df[data_df["sex"] == g][["age_range", attr_name]]
        for c in classes:
            cur_class = cur_df[cur_df[attr_name] == c]
            cur_class = cur_class.groupby(['age_range']).age_range.agg('count').to_frame('count').reset_index()
            cur_class['count'] = cur_class['count'].replace(0, "-")
            cur_gender.append(cur_class['count'].values.tolist())
        result.append(cur_gender)
    return jsonify({ "message" : "successful!" , "data": result})


@app.route('/traing_data_visialize/MHRA', methods=['GET'])
def provide_data_to_show_MHRA():
    attr_name = "MHRA"
    data_df = pd.read_csv(config.TRAINING_DATA, header = None, na_values = '?')
    data_df.columns = df_columns
    data_df = data_df.apply(lambda x: x.fillna(x.value_counts().index[0]))
    data_df_m = data_df[data_df["sex"] == 1][["age", attr_name]]
    data_df_f = data_df[data_df["sex"] == 0][["age", attr_name]]
    data_df_m = data_df_m.groupby(['age',attr_name]).age.agg('count').to_frame('count').reset_index()
    data_df_f = data_df_f.groupby(['age',attr_name]).age.agg('count').to_frame('count').reset_index()
    result = [data_df_m[["age", attr_name, "count"]].values.tolist(), data_df_f[["age", attr_name, "count"]].values.tolist()]
    return jsonify({ "message" : "successful!" , "data": result})

@app.route('/traing_data_visialize/EIA', methods=['GET'])
def provide_data_to_show_EIA():
    attr_name = "EIA"
    gender =[1,0]
    classes = [0,1]
    data_df = pd.read_csv(config.TRAINING_DATA, header = None, na_values = '?')
    data_df.columns = df_columns
    data_df = data_df.apply(lambda x: x.fillna(x.value_counts().index[0]))
    data_df['age_range'] = pd.cut(x=data_df['age'], bins=len(age_bins), labels=age_bins)
    data_df = data_df[['sex',attr_name,'age_range']]
    result = []
    for g in gender:
        cur_gender = []
        cur_df = data_df[data_df["sex"] == g][["age_range", attr_name]]
        for c in classes:
            cur_class = cur_df[cur_df[attr_name] == c]
            cur_class = cur_class.groupby(['age_range']).age_range.agg('count').to_frame('count').reset_index()
            cur_class['count'] = cur_class['count'].replace(0, "-")
            cur_gender.append(cur_class['count'].values.tolist())
        result.append(cur_gender)
    return jsonify({ "message" : "successful!" , "data": result})

@app.route('/traing_data_visialize/oldpeak', methods=['GET'])
def provide_data_to_show_oldpeak():
    attr_name = "oldpeak"
    data_df = pd.read_csv(config.TRAINING_DATA, header = None, na_values = '?')
    data_df.columns = df_columns
    data_df = data_df.apply(lambda x: x.fillna(x.value_counts().index[0]))
    data_df_m = data_df[data_df["sex"] == 1][["age", attr_name]]
    data_df_f = data_df[data_df["sex"] == 0][["age", attr_name]]
    data_df_m = data_df_m.groupby(['age',attr_name]).age.agg('count').to_frame('count').reset_index()
    data_df_f = data_df_f.groupby(['age',attr_name]).age.agg('count').to_frame('count').reset_index()
    result = [data_df_m[["age", attr_name, "count"]].values.tolist(), data_df_f[["age", attr_name, "count"]].values.tolist()]
    return jsonify({ "message" : "successful!" , "data": result})



@app.route('/traing_data_visialize/SOTPESTS', methods=['GET'])
def provide_data_to_show_SOTPESTS():
    attr_name = "SOTPESTS"
    gender =[1,0]
    classes = [1,2,3]
    data_df = pd.read_csv(config.TRAINING_DATA, header = None, na_values = '?')
    data_df.columns = df_columns
    data_df = data_df.apply(lambda x: x.fillna(x.value_counts().index[0]))
    data_df['age_range'] = pd.cut(x=data_df['age'], bins=len(age_bins), labels=age_bins)
    data_df = data_df[['sex',attr_name,'age_range']]
    result = []
    for g in gender:
        cur_gender = []
        cur_df = data_df[data_df["sex"] == g][["age_range", attr_name]]
        for c in classes:
            cur_class = cur_df[cur_df[attr_name] == c]
            cur_class = cur_class.groupby(['age_range']).age_range.agg('count').to_frame('count').reset_index()
            cur_class['count'] = cur_class['count'].replace(0, "-")
            cur_gender.append(cur_class['count'].values.tolist())
        result.append(cur_gender)
    return jsonify({ "message" : "successful!" , "data": result})


@app.route('/traing_data_visialize/NOMV', methods=['GET'])
def provide_data_to_show_NOMV():
    attr_name = "NOMV"
    gender =[1,0]
    classes = [0,1,2,3]
    data_df = pd.read_csv(config.TRAINING_DATA, header = None, na_values = '?')
    data_df.columns = df_columns
    data_df = data_df.apply(lambda x: x.fillna(x.value_counts().index[0]))
    data_df['age_range'] = pd.cut(x=data_df['age'], bins=len(age_bins), labels=age_bins)
    data_df = data_df[['sex',attr_name,'age_range']]
    result = []
    for g in gender:
        cur_gender = []
        cur_df = data_df[data_df["sex"] == g][["age_range", attr_name]]
        for c in classes:
            cur_class = cur_df[cur_df[attr_name] == c]
            cur_class = cur_class.groupby(['age_range']).age_range.agg('count').to_frame('count').reset_index()
            cur_class['count'] = cur_class['count'].replace(0, "-")
            cur_gender.append(cur_class['count'].values.tolist())
        result.append(cur_gender)
    return jsonify({ "message" : "successful!" , "data": result})
