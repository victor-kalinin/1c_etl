from os.path import join


def compile_path(major_path):
    return lambda name: '_'.join((major_path, name.lower()))


# Название переменной для хранения env значения
ENV_KEYNAME = '1CETL_ENV'

# Имя файла с настройками credentials
CREDENTIALS_FILENAME = 'mangodb.ini'

# Название файла для хранения лога программы
LOG_FILENAME = '1cetl.log'

# Количество повторных request-запросов, в случае возникновения ошибок
API_RETRY_COUNT = 3

# Словарь с ключами баз данных из файла *.ini с credentials
DWH_ENV_KEYS = {'PROD': 'DWHProd',
                'DEV': 'DWHDev',
                'STAGE': 'DWHStage'}

# Полный путь к каталогу хранения файлов с моделями БД
MODELS_DIR_PATH = join('app', 'models')

# Путь с файлом к папке с credentials
CREDENTIALS_PATH = join('app', 'public', 'credentials', CREDENTIALS_FILENAME)

# Путь с файлом к папке с логами
LOG_PATH = join('app', 'public', 'logs', LOG_FILENAME)

MODELS_MODULE_PATH = compile_path('app.models.models')
SCHEMAS_MODULE_PATH = compile_path('app.schemas.schemas')
API_CONN_MODULE_PATH = compile_path('app.config.api_conn.api')
