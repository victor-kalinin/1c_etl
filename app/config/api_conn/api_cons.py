from app.core.templates.api_settings import APISettings


class ConsSettings(APISettings):
    CONFIG_KEY = 'Api1sConsProd'
    ROUTES = {'CatalogCfo': '/catalog?name=CFO',
              'CatalogStOb': '/catalog?name=StOb',
              'CatalogNg': '/catalog?name=NomenclatureGroups',
              'CatalogScenariy': '/catalog?name=Scenariy',
              'CatalogAccount': '/catalog?name=Account',
              'CatalogBankAccount': '/catalog?name=BankAccount',
              'CatalogStDDS': '/catalog?name=StDDS',
              }
