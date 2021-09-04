from os.path import join


def compile_path(major_path):
    return lambda name: '_'.join((major_path, name.lower()))


ENV_KEYNAME = '1CETL_ENV'
CONFIG_FILENAME = 'mangodb.ini'
LOG_FILENAME = '1cetl.log'
API_RETRY_COUNT = 3
DWH_ENV_KEYS = {'PROD': '__',               # Добавлен dunder для запрета случайной отправки данных в PROD GP.
                'DEV': 'DWHDev',            # После переноса в production добавить значение 'DWHProd'
                'STAGE': 'DWHStage'}

MODELS_DIR_PATH = join('app', 'models')
CONFIG_PATH = join('app', 'public', 'credentials', CONFIG_FILENAME)
LOG_PATH = join('app', 'public', 'logs', LOG_FILENAME)

MODELS_MODULE_PATH = compile_path('app.models.models')
SCHEMAS_MODULE_PATH = compile_path('app.schemas.schemas')
API_CONN_MODULE_PATH = compile_path('app.config.api_conn.api')
