from app.core.templates.db_settings import DBSettings


class DWHDBSettings(DBSettings):
    CONFIG_KEY: str = 'DWHProd'
    DB_DRIVER: str = 'postgresql+psycopg2'
