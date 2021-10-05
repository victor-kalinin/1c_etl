from app.config.api_conn.api_zup import ZUPSettings


class ZUPParamsSettings(ZUPSettings):
    ROUTES = {'EmployeesHistory': '/data/employees_history',
              'StaffTableHistory': '/data/staff_table_history',
              'Tutors': '/data/tutors',
              'SellersGroupsStructure': '/data/sellers_groups_structure',
              'SalesGroupsPlan': '/data/sales_groups_plan',
              'SalesPlan': '/data/sales_plan',
              'RecruitmentDecision': '/data/recruitment_decision',
              'Trainings': '/data/trainings',
              'AdaptationTasks': '/data/adaptation_tasks',
              }
