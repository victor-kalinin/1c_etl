from os.path import join


def compile_path(major_path):
    return lambda name: '_'.join((major_path, name.lower()))


MODELS_OS_PATH = join('app', 'models')
CONFIG_OS_PATH = join('app', 'config')

MODELS_MODULE_PATH = compile_path('app.models.models')
SCHEMAS_MODULE_PATH = compile_path('app.schemas.schemas')
API_CONN_MODULE_PATH = compile_path('app.config.api_conn.api')

CONFIG_FILE = 'mangodb.ini'

FILENAME_KEY = 'CONFIG_FILENAME'
CREDENTIALS_KEY = 'MANGOCREDENTIALS'
