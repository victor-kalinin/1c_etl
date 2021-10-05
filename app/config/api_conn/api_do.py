from app.core.templates.api_settings import APISettings


class DOSettings(APISettings):
    CONFIG_KEY = 'ApiDoProd'
    ROUTES: dict = {'ManagementStructureHeads': '/management_structure_heads',
                    'ManagementStructureOccupation': '/management_structure_occupation',
                    'ManagementStructure': '/management_structure',
                    }
