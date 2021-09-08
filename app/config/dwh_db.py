from os import environ

from app.core.templates.db_settings import DBSettings
from app.core.consts import DWH_ENV_KEYS, ENV_KEYNAME


class DWHDBSettings(DBSettings):
    """
    Класс с настройками для подключения к БД

    CONFIG_KEY : str
        Ключ ini header блока с credentials в файле *.ini
    DB_DRIVER : str
        Драйвер в формате SQLAlchemy
    """

    # Значение :CONFIG_KEY: получаем ключ из словаря из файла consts.py,
    # используя env переменную (которую мы задали при запуске приложения через argparse) как ключ
    CONFIG_KEY: str = DWH_ENV_KEYS.get(environ.get(ENV_KEYNAME))
    DB_DRIVER: str = 'postgresql+psycopg2'
