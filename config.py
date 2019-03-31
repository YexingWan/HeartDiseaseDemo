import os
from os import environ


class Config(object):
    SECRET_KEY = 'key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # THEME SUPPORT
    #  if set then url_for('static', filename='', theme='')
    #  will add the theme name to the static URL:
    #    /static/<DEFAULT_THEME>/filename
    # DEFAULT_THEME = "themes/dark"
    DEFAULT_THEME = None


class ProductionConfig(Config):
    DEBUG = False

    # PostgreSQL database
    SQLALCHEMY_DATABASE_URI = 'postgresql://{}:{}@{}:{}/{}'.format(
        environ.get('GENTELELLA_DATABASE_USER', 'gentelella'),
        environ.get('GENTELELLA_DATABASE_PASSWORD', 'gentelella'),
        environ.get('GENTELELLA_DATABASE_HOST', 'db'),
        environ.get('GENTELELLA_DATABASE_PORT', 5432),
        environ.get('GENTELELLA_DATABASE_NAME', 'gentelella')
    )


class DebugConfig(Config):
    DEBUG = True


config_dict = {
    'Production': ProductionConfig,
    'Debug': DebugConfig,
}

# base path
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

DATA_DIR = os.path.join(BASE_DIR, 'data_files')

# upload path
UPLOAD_DIR = os.path.join(DATA_DIR, 'uploads')
WATER_MAINS_FILE = os.path.join(UPLOAD_DIR, 'water_mains.csv')
FAILURES_FILE = os.path.join(UPLOAD_DIR, 'failures.csv')

# Existing processed data files
STABLE_DIR = os.path.join(DATA_DIR, 'stables')
GROUND_LEVEL_FILE = os.path.join(STABLE_DIR, 'Mean-variance GL_eachpipe all sydney.csv')
PRESSURE_FILE = os.path.join(STABLE_DIR, 'pressure for all pipes separated_PG.csv')
# INFO_EM_FILE = os.path.join(STABLE_DIR, 'EMData_Aug2018.xlsx')      # categorical values of soil
# NEW_SOIL_FILE = os.path.join(STABLE_DIR, 'Whole_data_new_soil_Dilusha.csv')     # numeric values of soil
INFO_EM_FILE = os.path.join(STABLE_DIR, 'full_new_EM.csv')      # categorical values of soil
NEW_SOIL_FILE = os.path.join(STABLE_DIR, 'full_new_soil.csv')     # numeric values of soil
TOOLS_RESULT_FILE = os.path.join(STABLE_DIR, 'results_Pipe.csv')
FEAT_DESC_FILE = os.path.join(STABLE_DIR, 'feature_description.csv')
TOPOLOGY_FILE = os.path.join(STABLE_DIR, 'topology_shape_features.csv')


# Saved processed data files

PROCESSED_DIR = os.path.join(DATA_DIR, 'processed')
MERGED_DATA_FILE = os.path.join(PROCESSED_DIR, 'merged_data.csv')
TRAN_DATA_FILE = os.path.join(PROCESSED_DIR, 'train_data.csv')

OUTPUT_DIR = os.path.join(DATA_DIR, 'output')


class ResultFilesPaths:
    def __init__(self, year):
        self.YEAR = year

    @property
    def FEAT_IMPORTANCE_FILE(self):
        return os.path.join(OUTPUT_DIR, 'feat_importance_{}.csv'.format(self.YEAR))

    @property
    def PRED_RESULT_FILE(self):
        return os.path.join(OUTPUT_DIR, 'pred_result_{}.csv'.format(self.YEAR))

    @property
    def PRI_LIST_ALL_FILE(self):
        return os.path.join(OUTPUT_DIR, 'priority_list_all_{}.csv'.format(self.YEAR))

    @property
    def PRI_LIST_375_FILE(self):
        return os.path.join(OUTPUT_DIR, 'priority_list_375_{}.csv'.format(self.YEAR))

    @property
    def EVAL_FILE(self):
        return os.path.join(OUTPUT_DIR, 'eval_{}.csv'.format(self.YEAR))

    @property
    def EVAL_375_FILE(self):
        return os.path.join(OUTPUT_DIR, 'eval_375_{}.csv'.format(self.YEAR))

    @property
    def TRUNK_FILE(self):
        return os.path.join(OUTPUT_DIR, 'trunk_priority_{}.csv'.format(self.YEAR))

    @property
    def SHUTDOWN_BOLCK_FILE(self):
        return os.path.join(OUTPUT_DIR, 'shutdown_block_priority_{}.csv'.format(self.YEAR))


# csv file formats
FILE_FORMATS = {
    'water_mains': [],
    'failures': []
}

# Other configurations
NUM_CORES = 2

MODEL_PATH = os.path.join(BASE_DIR, 'model_files')

# Selected columns for prediction results showing
# key: column from original data
# value: display name in data table
SEL_COLS = {'pipes':                'Pipe ID',
            '#_failures':           'Failures',
            'fail_probability':     'Failure Probability',
            'laid_year':            'Laid Year',
            'lga':                  'LGA',
            'pipe_size':            'Size (mm)',
            'material':             'Material',
            'horizontal_length':    'Length (m)',
            'shutdown_block_id':    'Shutdown Block ID',
            'trunk_main_name': 'Trunk Name',
            'trunk_main_number':   'Trunk Number'
            }

#'trunk_main_number':   'Trunk Number'
#'trunk_main_name': 'Trunk Name',
# 'shutdown_block_id':    'Shutdown Block ID'}

# session keys
SESSION_PRED_YEAR = 'pred_year'
