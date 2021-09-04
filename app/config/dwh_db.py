from os import environ

from app.core.templates.db_settings import DBSettings
from app.core.consts import DWH_ENV_KEYS, ENV_KEYNAME


class DWHDBSettings(DBSettings):
    CONFIG_KEY: str = DWH_ENV_KEYS.get(environ.get(ENV_KEYNAME))
    DB_DRIVER: str = 'postgresql+psycopg2'
