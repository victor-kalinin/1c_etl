from .api_mkbf import MKBFSettings


class MKBFAccumsSettings(MKBFSettings):
    ROUTES = {'Accum': '/accum',
              'AccumPl': '/accum_pl',
              }
