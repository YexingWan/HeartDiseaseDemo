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
FEAT_IMPORTANCE_FILE = os.path.join(STABLE_DIR,'feature_importance.csv')

MODEL_PATH = os.path.join(MODEL_DIR, 'model.bin')
EVAL_FILE = os.path.join(OUTPUT_DIR, 'eval.csv')
RESULT_FILE = os.path.join(OUTPUT_DIR, 'result.csv')

# file
TRAINING_DATA = os.path.join(STABLE_DIR,'processed.cleveland.data')


COLS_SHOW_MAP = {
    'age':'age',
    'sex':'sex',
    'CPT': 'chest pain type',
    'RBP': 'resting blood pressure',
    'SC': 'serum cholestoral',
    'FBS': 'fasting blood sugar',
    'RER': 'resting electrocardiographic results',
    'MHRA': 'maximum heart rate achieved',
    'EIA': 'exercise induced angina',
    'oldpeak': 'oldpeak',
    'SOTPESTS': 'slope of the peak exercise ST segment',
    'NOMV': 'number of major vessels (0-3) colored by flourosopy',
    'thal': 'thal'
}

