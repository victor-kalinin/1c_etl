from app.config.api_conn.api_zup import ZUPSettings


class ZUPAssertSettings(ZUPSettings):
    ROUTES = {'BonusWorkTime': '/data/bonus_work_time',
              }
