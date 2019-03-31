from app.analysis import blueprint, data_mgr_utils, pred_utils
from flask import render_template, redirect, url_for, request, jsonify, send_from_directory, session
import pandas as pd
import os
import config
from app.analysis import utils


def init_sessions():
    if config.SESSION_PRED_YEAR not in session:
        session[config.SESSION_PRED_YEAR] = utils.get_default_year()
        print("session year change to : %d" % session[config.SESSION_PRED_YEAR])


@blueprint.route('/set_session_val', methods=['POST'])
def set_sesstions():
    print(request.form)
    print('origin session: ',end='')
    print(session)
    for k in request.form.keys():
        session[k] = request.form[k]
    print("cchanged session: ",end='')
    print(session)
    return "", 200


@blueprint.route('/get_session_val', methods=['POST'])
def get_session_val():
    return jsonify({config.SESSION_PRED_YEAR: int(session[request.form['session_key']])})


@blueprint.route('/')
def index():
    init_sessions()
    return redirect(url_for('analysis_blueprint.data_management'))


@blueprint.route('/data_management')
def data_management():
    init_sessions()
    return render_template('data_management.html')


@blueprint.route('/gis_data_layer')
def gis_data_layer():
    init_sessions()
    return render_template('gis_data_layer.html')


@blueprint.route('/failure_prediction')
def failure_prediction():
    init_sessions()
    return render_template('failure_prediction.html')


@blueprint.route('/analysis')
def analysis():
    init_sessions()
    return render_template('analysis.html')


@blueprint.route('/analysis/get_eval_results', methods=['POST'])
def get_eval_results():
    # init return message
    year = int(request.form["cur_year"])
    print('curretn_year:'+str(year))

    return_msg = dict()
    if os.path.isfile(config.ResultFilesPaths(year).EVAL_FILE) and \
            os.path.isfile(config.ResultFilesPaths(year).EVAL_375_FILE):
        eval_results_df = pd.read_csv(config.ResultFilesPaths(year).EVAL_FILE)
        eval_results_375_df = pd.read_csv(config.ResultFilesPaths(year).EVAL_375_FILE)

        json_eval_results = eval_results_df.transpose().to_json(orient='split')
        json_eval_375_results = eval_results_375_df.transpose().to_json(orient='split')

        return_msg['data'] = json_eval_results
        return_msg['data_375'] = json_eval_375_results
        return_msg['status'] = 'succ'
    else:
        return_msg['data'] = ''
        return_msg['data_375'] = ''
        return_msg['status'] = 'fail'

    return jsonify(return_msg)


@blueprint.route('/data_management/upload', methods=['POST'])
def upload_files():
    """
        upload data files
    """
    # init return message
    return_msg = dict()

    # get files
    water_main_file = request.files['water_main_file']
    failure_record_file = request.files['failure_record_file']

    # specify file path to save
    water_main_filepath = os.path.join(config.UPLOAD_DIR, 'water_mains.csv')
    failure_record_filepath = os.path.join(config.UPLOAD_DIR, 'failures.csv')

    # save files
    water_main_file.save(water_main_filepath)
    failure_record_file.save(failure_record_filepath)

    return_msg['message'] = 'DONE!'
    return jsonify(return_msg)


@blueprint.route('/data_management/check_files', methods=['POST'])
def check_files():
    """
        check data formats
    """
    # init return message
    return_msg = dict()

    # get the saved file
    water_main_filepath = config.WATER_MAINS_FILE
    failure_record_filepath = config.FAILURES_FILE

    # check file formats
    water_mains_format_checked = data_mgr_utils.check_file_formats(water_main_filepath, file_type='water_mains')
    failures_format_checked = data_mgr_utils.check_file_formats(failure_record_filepath, file_type='failures')

    if not (water_mains_format_checked and failures_format_checked):
        # delete files
        if os.path.isfile(water_main_filepath):
            os.remove(water_main_filepath)
        if os.path.isfile(failure_record_filepath):
            os.remove(failure_record_filepath)

        return_msg['status'] = 'fail'
        return_msg['message'] = 'ERROR!'
    else:
        return_msg['status'] = 'succ'
        return_msg['message'] = 'DONE!'
    return jsonify(return_msg)


@blueprint.route('/data_management/merge_files', methods=['POST'])
def merge_files():
    """
        merge data files
    """
    # init return message
    return_msg = dict()

    # merge file
    data_mgr_utils.construct_processed_data(config.WATER_MAINS_FILE, config.GROUND_LEVEL_FILE,
                                            config.PRESSURE_FILE, config.FAILURES_FILE,
                                            config.INFO_EM_FILE, config.NEW_SOIL_FILE,
                                            config.TOPOLOGY_FILE,config.MERGED_DATA_FILE)

    return_msg['status'] = 'succ'
    return_msg['message'] = 'DONE!'
    return jsonify(return_msg)


@blueprint.route('/failure_prediction/predict', methods=['POST'])
def do_prediction():
    """
        Perform prediction based on selected year
    """
    # init return message
    return_msg = dict()

    # get prediction year
    pred_year = int(request.form['pred_year'])

    # reset config
    # config.RESULT_PATH.reset_year(pred_year)

    # flag of retrain model
    renew_model = True if str(request.form['is_retrain']) == 'true' else False

    # generate training/test data
    df = pred_utils.construct_training_testing_datas(config.MERGED_DATA_FILE, config.TOOLS_RESULT_FILE, pred_year,
                                                     renew_model)
    # do prediction

    data_list, columns_list = pred_utils.predict(df, pred_year,
                                                 config.ResultFilesPaths(int(pred_year)).FEAT_IMPORTANCE_FILE,
                                                 config.ResultFilesPaths(int(pred_year)).PRED_RESULT_FILE, renew_model)

    c_n_m = config.SEL_COLS
    feat_importance_df = pd.read_csv(config.ResultFilesPaths(int(pred_year)).FEAT_IMPORTANCE_FILE)
    json_feat_importance = feat_importance_df.transpose().to_json(orient='split')
    return_msg['feat_importance'] = json_feat_importance
    return_msg['message'] = 'DONE!'
    return_msg['columns'] = [c for c in [c_n_m[sc] for sc in columns_list]]
    #return_msg['data'] = data_list

    return jsonify(return_msg)


@blueprint.route('/download/<path:filename>')
def download_file(filename):
    return send_from_directory(config.OUTPUT_DIR, filename, as_attachment=True, cache_timeout=0)


@blueprint.route('/show_pred_result', methods=['POST'])
def get_previous_result():
    year = request.form[config.SESSION_PRED_YEAR]
    #year = session['pred_year']
    print('showing %s years result' % year)
    return_msg = dict()
    c_n_m = config.SEL_COLS
    data_list, columns_list = pred_utils.get_result_history(year)
    #print(data_list)
    #print(columns_list)
    if data_list is not None:
        feat_importance_df = pd.read_csv(config.ResultFilesPaths(year).FEAT_IMPORTANCE_FILE)
        json_feat_importance = feat_importance_df.transpose().to_json(orient='split')
        return_msg['feat_importance'] = json_feat_importance
        return_msg['message'] = 'DONE'
        return_msg['columns'] = [c for c in [c_n_m[sc] for sc in columns_list]]
        return_msg['data'] = data_list
    else:
        return_msg['message'] = 'FAIL'

    #return jsonify({"A":123})
    return jsonify(return_msg)



# @blueprint.route("/serverside_table", methods=['GET'])
# def serverside_table_content():
#     data = collect_data_serverside(request)
#     return jsonify(data)



