import os


# base path
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data_files')

# directory
UPLOAD_DIR = os.path.join(DATA_DIR, 'uploads')
STABLE_DIR = os.path.join(DATA_DIR, 'stables')
OUTPUT_DIR = os.path.join(DATA_DIR, 'output')
MODEL_DIR = os.path.join(BASE_DIR, 'model_files')
FEAT_DESC_FILE = os.path.join(STABLE_DIR,'feature_description.csv')
MODEL_PATH = os.path.join(MODEL_DIR, 'model.bin')
EVAL_FILE = os.path.join(OUTPUT_DIR, 'eval.csv')
RESULT_FILE = os.path.join(OUTPUT_DIR, 'result.csv')

# file
TRAINING_DATA = os.path.join(DATA_DIR,'')


COLS_SHOW_MAP = {
    'a':'show as a',
    'b':'show as b'
}

