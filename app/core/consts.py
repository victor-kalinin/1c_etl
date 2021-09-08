from os.path import join


def compile_path(major_path):
    return lambda name: '_'.join((major_path, name.lower()))


ENV_KEYNAME = '1CETL_ENV'                   # Название переменной для хранения env значения
CREDENTIALS_FILENAME = 'mangodb.ini'        # Имя файла с настройками credentials
LOG_FILENAME = '1cetl.log'                  # Название файла для хранения лога программы
API_RETRY_COUNT = 3                         # Количество повторных request-запросов, в случае возникновения ошибок
DWH_ENV_KEYS = {'PROD': '__',               # Добавлен dunder для запрета случайной отправки данных в PROD GP.
                'DEV': 'DWHDev',            # После переноса в production добавить значение 'DWHProd'
                'STAGE': 'DWHStage'}

MODELS_DIR_PATH = join('app', 'models')     # Полный путь к каталогу хранения файлов с моделями БД
CREDENTIALS_PATH = join('app', 'public', 'credentials', CREDENTIALS_FILENAME)   # Путь с файлом к папке с credentials
LOG_PATH = join('app', 'public', 'logs', LOG_FILENAME)                          # Путь с файлом к папке с логами

MODELS_MODULE_PATH = compile_path('app.models.models')
SCHEMAS_MODULE_PATH = compile_path('app.schemas.schemas')
API_CONN_MODULE_PATH = compile_path('app.config.api_conn.api')
