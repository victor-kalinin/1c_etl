from app.core.templates.api_settings import APISettings


class MKBFSettings(APISettings):
    CONFIG_KEY = 'ApiMkbfProd'
    ROUTES: dict = {'CatalogCfo': '/catalog?name=CFO',
                    'CatalogPodr': '/catalog?name=Podr',
                    'CatalogStOb': '/catalog?name=StOb',
                    'CatalogTypeRsp': '/catalog?name=TypeRsp',
                    'CatalogNg': '/catalog?name=NomenclatureGroups',
                    'CatalogScenariy': '/catalog?name=Scenariy',
                    'Documents': '/documents?name=DistributionData',
                    }
