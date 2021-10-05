from app.core.templates.api_settings import APISettings


class ZUPSettings(APISettings):
    CONFIG_KEY = 'ApiZupProd'
    ROUTES: dict = {'JobPositions': '/data/job_positions',
                    'Contractors': '/data/contractors',
                    'Departments': '/data/departments',
                    'Employees': '/data/employees',
                    'StaffTable': '/data/staff_table',
                    'StaffTableExceptions': '/data/staff_table_exceptions',
                    'StaffTableOccupation': '/data/staff_table_occupation',
                    'PersonAccounts': '/data/accounts',
                    'Sellers': '/data/sellers',
                    'SellersGroups': '/data/seller_groups',
                    'SalesIndicators': '/data/sale_indicators',
                    'EmployeesRanks': '/data/employees_ranks',
                    'CatalogAdaptation': '/data/adaptation_task_types',
                    }
