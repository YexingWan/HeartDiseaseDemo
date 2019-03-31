from flask_migrate import Migrate
from os import environ
from sys import exit

from config import config_dict
#from app import create_app, db
from app import create_app

# can be changed in .env file
# get_config_mode = environ.get('ACA_PROJ_CONFIG_MODE')
get_config_mode = 'Production'
try:
    config_mode = config_dict[get_config_mode.capitalize()]
except KeyError:
    exit('Error: Invalid config environment variable entry.')

app = create_app(config_mode, selenium=True)
#Migrate(app, db)

if __name__ == '__main__':
    app.run()

