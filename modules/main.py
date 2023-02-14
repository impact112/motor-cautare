
from modules.database import *
from modules.routes import get_app
import yaml

config_data: dict

with open( 'config.yml', 'r' ) as fd:
    config_data = yaml.safe_load( fd )

app = get_app( config_data )
