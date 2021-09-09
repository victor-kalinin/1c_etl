from .api_cons import ConsSettings


class ConsAccumsSettings(ConsSettings):
    ROUTES = {'ConsAccum': '/accum',
              'ConsCashflow': '/cashflow',
              }
