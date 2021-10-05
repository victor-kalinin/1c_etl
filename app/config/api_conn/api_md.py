from app.core.templates.api_settings import APISettings


class MDSettings(APISettings):
    CONFIG_KEY = 'ApiMdProd'
    ROUTES: dict = {'CatalogCfo': '/catalog?name=CFO',
                    'CatalogPodr': '/catalog?name=Podr',
                    'CatalogStOb': '/catalog?name=StOb',
                    'CatalogTypeRsp': '/catalog?name=TypeRsp',
                    'CatalogNom': '/catalog?name=Nomenclature',
                    'CatalogNomGroups': '/catalog?name=NomenclatureGroups',
                    'CatalogScenariy': '/catalog?name=Scenariy',
                    'Documents': '/documents?name=DistributionData',
                    }
