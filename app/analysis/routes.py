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


@app.route('/')
def index():
    return redirect(url_for('data_management'))


@app.route('/data_management')
def data_management():
    return render_template('data_management.html')


@app.route('/data_management/get_eval_results', methods=['GET'])
def get_eval_results():
    # init return message
    year = int(request.form["cur_year"])
    print('curretn_year:'+str(year))

    return_msg = dict()
    if os.path.isfile(config.EVAL_FILE):
        eval_results_df = pd.read_csv(config.EVAL_FILE)

        json_eval_results = eval_results_df.transpose().to_json(orient='split')

        return_msg['data'] = json_eval_results
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
    df = pred_utils.construct_data()

    # do prediction
    data_list, columns_list = pred_utils.predict(df)

    c_n_m = config.COLS_SHOW_MAP
    feat_importance_df = pd.read_csv(config.FEAT_DESC_FILE)

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







