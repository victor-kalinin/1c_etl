from os.path import join


def compile_path(major_path):
    return lambda name: '_'.join((major_path, name.lower()))


MODELS_OS_PATH = join('app', 'models')
CONFIG_OS_PATH = join('app', 'public', 'credentials')
LOGS_OS_PATH = join('app', 'public', 'logs')

MODELS_MODULE_PATH = compile_path('app.models.models')
SCHEMAS_MODULE_PATH = compile_path('app.schemas.schemas')
API_CONN_MODULE_PATH = compile_path('app.config.api_conn.api')

CONFIG_FILE = 'mangodb.ini'
LOG_FILE = '1cetl.log'

FILENAME_KEY = 'CONFIG_FILENAME'
CREDENTIALS_KEY = 'MANGOCREDENTIALS'
LOGFILE_KEY = '1CETL_LOGFILE'

API_RETRY_COUNT = 3
