import sys
from os import environ, getcwd
sys.path.append(getcwd())

from sqlalchemy import Table, Column, Integer, String, DateTime, Boolean, Float, Text, JSON, MetaData
from sqlalchemy.dialects.postgresql import UUID
from app.core.consts import ENV_KEYNAME
environ[ENV_KEYNAME] = 'STAGE'

from app.db.session import engine


print('Инициализация базы данных ... ', end='')
metadata = MetaData()

ConsCatalogCfo = Table('rs1c_cons_catalog_cfo', metadata,
                       Column('ЦФО', Text),
                       Column('Родитель', Text),
                       Column('Код', Text),
                       Column('Наименование', Text),
                       Column('ПометкаУдаления', Boolean),
                       schema='rsrc')

ConsCatalogStOb = Table('rs1c_cons_catalog_st_ob', metadata,
                        Column('СтатьиОборотов', Text),
                        Column('ЭтоГруппа', Boolean),
                        Column('Наименование', Text),
                        Column('ТипСтатьи', Text),
                        Column('Кодификатор', Text),
                        Column('Направление', Text),
                        Column('Родитель', Text),
                        Column('ПометкаУдаления', Boolean),
                        schema='rsrc')

ConsCatalogNg = Table('rs1c_cons_catalog_ng', metadata,
                      Column('НоменклатурнаяГруппа', Text),
                      Column('ЭтоГруппа', Boolean),
                      Column('Наименование', Text),
                      Column('Родитель', Text),
                      Column('ПометкаУдаления', Boolean),
                      schema='rsrc')

ConsCatalogScenariy = Table('rs1c_cons_catalog_scenariy', metadata,
                            Column('Сценарий', Text),
                            Column('ЭтоГруппа', Boolean),
                            Column('Родитель', Text),
                            Column('Наименование', Text),
                            Column('ПометкаУдаления', Boolean),
                            schema='rsrc')

ConsAccum = Table('rs1c_cons_accum', metadata,
                  Column('Период', DateTime),
                  Column('Организация', Text),
                  Column('Сценарий', Text),
                  Column('ЦФО', Text),
                  Column('ЦФОКод', Text),
                  Column('ЦФОНаименование', Text),
                  Column('СтатьяОборотов', Text),
                  Column('НоменклатурнаяГруппа', Text),
                  Column('Контрагент', Text),
                  Column('Сумма', Float),
                  Column('ЭтоПлан', Boolean),
                  Column('ЭтоВнутригрупповойОборот', Boolean),
                  Column('ЭтоКорректировка', Boolean),
                  Column('ДатаЗагрузки', DateTime),
                  schema='rsrc')

DoManagementStructureHeads = Table('rs1c_do_management_structure_heads', metadata,
                                   Column('Структура', Text),
                                   Column('ФизическоеЛицоРуководитель', Text),
                                   Column('ПометкаУдаления', Boolean),
                                   schema='rsrc')

DoManagementStructureOccupation = Table('rs1c_do_management_structure_occupation', metadata,
                                        Column('Структура', Text),
                                        Column('ФизическоеЛицо', Text),
                                        Column('ПометкаУдаления', Boolean),
                                        schema='rsrc')

DoManagementStructure = Table('rs1c_do_management_structure', metadata,
                              Column('Структура', Text),
                              Column('Родитель', Text),
                              Column('СтруктураНаименование', Text),
                              Column('Подразделение', Text),
                              schema='rsrc')

DoTasksTracking = Table('rs1c_do_tasks_tracking', metadata,
                        Column('Задача', Text),
                        Column('ЗадачаЗУП', Text),
                        Column('ТипЗадачи', Text),
                        Column('Исполнитель', Text),
                        Column('ДатаВыполнения', DateTime),
                        Column('Выполнена', Boolean),
                        Column('СтатусПроцесса', Text),
                        schema='rsrc')

MdCatalogCfo = Table('rs1c_md_catalog_cfo', metadata,
                     Column('ЦФО', Text),
                     Column('Родитель', Text),
                     Column('Код', Text),
                     Column('Наименование', Text),
                     Column('ПометкаУдаления', Boolean),
                     schema='rsrc')

MdCatalogPodr = Table('rs1c_md_catalog_podr', metadata,
                      Column('Подразделение', Text),
                      Column('Организация', Text),
                      Column('Родитель', Text),
                      Column('Код', Text),
                      Column('Наименование', Text),
                      Column('ОбособленноеПодразделение', Boolean),
                      Column('ПометкаУдаления', Boolean),
                      schema='rsrc')

MdCatalogStOb = Table('rs1c_md_catalog_st_ob', metadata,
                      Column('СтатьиОборотов', Text),
                      Column('ЭтоГруппа', Boolean),
                      Column('Наименование', Text),
                      Column('ТипСтатьи', Text),
                      Column('Кодификатор', Text),
                      Column('Направление', Text),
                      Column('Родитель', Text),
                      Column('ТипРаспределения', Text),
                      Column('ПометкаУдаления', Boolean),
                      schema='rsrc')

MdCatalogTypeRsp = Table('rs1c_md_catalog_type_rsp', metadata,
                         Column('ТипРаспределения', Text),
                         Column('Наименование', Text),
                         Column('ПометкаУдаления', Boolean),
                         schema='rsrc')

MdCatalogNom = Table('rs1c_md_catalog_n', metadata,
                     Column('Ссылка', Text),
                     Column('Код', Text),
                     Column('Наименование', Text),
                     Column('ПометкаУдаления', Boolean),
                     schema='rsrc')

MdCatalogNomGroups = Table('rs1c_md_catalog_ng', metadata,
                           Column('НоменклатурнаяГруппа', Text),
                           Column('ЭтоГруппа', Boolean),
                           Column('Наименование', Text),
                           Column('ТипСтатьи', Text, nullable=True),
                           Column('Кодификатор', Text, nullable=True),
                           Column('Родитель', Text),
                           Column('ПометкаУдаления', Boolean),
                           schema='rsrc')

MdCatalogScenariy = Table('rs1c_md_catalog_scenariy', metadata,
                          Column('Сценарий', Text),
                          Column('ЭтоГруппа', Boolean),
                          Column('Родитель', Text),
                          Column('Наименование', Text),
                          Column('ПометкаУдаления', Boolean),
                          schema='rsrc')

MdDocuments = Table('rs1c_md_documents', metadata,
                    Column('Ссылка', Text),
                    Column('Номер', Text),
                    Column('Дата', DateTime),
                    Column('НГ_Ссылка', Text),
                    Column('НГ_Код', Text),
                    Column('НГ_Наименование', Text),
                    Column('ПроцентРаспределенияНаПродукт', JSON),
                    schema='rsrc')

MDAccum = Table('rs1c_md_accum', metadata,
                Column('Период', DateTime),
                Column('Сценарий', Text),
                Column('ЦФО', Text),
                Column('ЦФОКод', Text),
                Column('ЦФОНаименование', Text),
                Column('СтатьяОборотов', Text),
                Column('НоменклатурнаяГруппа', Text),
                Column('ПодразделениеОрганизации', Text),
                Column('СчетчикПодрОрг', Integer),
                Column('Количество', Integer),
                Column('Сумма', Float),
                Column('ЭтоПлан', Boolean),
                Column('ЭтоВнутригрупповойОборот', Boolean),
                Column('Продукция', Text),
                Column('ДатаЗагрузки', DateTime),
                schema='rsrc')

MkbfCatalogCfo = Table('rs1c_mkbf_catalog_cfo', metadata,
                       Column('ЦФО', Text),
                       Column('Родитель', Text),
                       Column('Код', Text),
                       Column('Наименование', Text),
                       Column('ПометкаУдаления', Boolean),
                       schema='rsrc')

MkbfCatalogPodr = Table('rs1c_mkbf_catalog_podr', metadata,
                        Column('Подразделение', Text),
                        Column('Организация', Text),
                        Column('Родитель', Text),
                        Column('Код', Text),
                        Column('Наименование', Text),
                        Column('ОбособленноеПодразделение', Boolean),
                        Column('ПометкаУдаления', Boolean),
                        schema='rsrc')

MkbfCatalogStOb = Table('rs1c_mkbf_catalog_st_ob', metadata,
                        Column('СтатьиОборотов', Text),
                        Column('ЭтоГруппа', Boolean),
                        Column('Наименование', Text),
                        Column('ТипСтатьи', Text),
                        Column('Кодификатор', Text),
                        Column('Направление', Text),
                        Column('Родитель', Text),
                        Column('ТипРаспределения', Text),
                        Column('ПометкаУдаления', Boolean),
                        schema='rsrc')

MkbfCatalogTypeRsp = Table('rs1c_mkbf_catalog_type_rsp', metadata,
                           Column('ТипРаспределения', Text),
                           Column('Наименование', Text),
                           Column('ПометкаУдаления', Boolean),
                           schema='rsrc')

MkbfCatalogNg = Table('rs1c_mkbf_catalog_ng', metadata,
                      Column('НоменклатурнаяГруппа', Text),
                      Column('ЭтоГруппа', Boolean),
                      Column('Наименование', Text),
                      Column('ТипСтатьи', Text),
                      Column('Кодификатор', Text),
                      Column('Родитель', Text),
                      Column('ПометкаУдаления', Boolean),
                      schema='rsrc')

MkbfCatalogScenariy = Table('rs1c_mkbf_catalog_scenariy', metadata,
                            Column('Сценарий', Text),
                            Column('ЭтоГруппа', Boolean),
                            Column('Родитель', Text),
                            Column('Наименование', Text),
                            Column('ПометкаУдаления', Boolean),
                            schema='rsrc')

MkbfDocuments = Table('rs1c_mkbf_documents', metadata,
                      Column('Ссылка', Text),
                      Column('Номер', Text),
                      Column('Дата', DateTime),
                      Column('НГ_Ссылка', Text),
                      Column('НГ_Код', Text),
                      Column('НГ_Наименование', Text),
                      Column('ПроцентРаспределенияНаПродукт', JSON),
                      schema='rsrc')

MkbfAccum = Table('rs1c_mkbf_accum', metadata,
                  Column('Период', DateTime),
                  Column('Сценарий', Text),
                  Column('ЦФО', Text),
                  Column('ЦФОКод', Text),
                  Column('ЦФОНаименование', Text),
                  Column('СтатьяОборотов', Text),
                  Column('НоменклатурнаяГруппа', Text),
                  Column('ПодразделениеОрганизации', Text),
                  Column('СчетчикПодрОрг', Integer),
                  Column('Количество', Integer),
                  Column('Сумма', Float),
                  Column('ЭтоПлан', Boolean),
                  Column('ЭтоВнутригрупповойОборот', Boolean),
                  Column('ДатаЗагрузки', DateTime),
                  schema='rsrc')

MkbfAccumPl = Table('rs1c_mkbf_accum_pl', metadata,
                    Column('Период', DateTime),
                    Column('Организация', Text),
                    Column('Валюта', Text),
                    Column('Сценарий', Text),
                    Column('Продукт', Text),
                    Column('ЦФО', Text),
                    Column('ЦФОКод', Text),
                    Column('ЦФОНаименование', Text),
                    Column('СтатьяОборотов', Text),
                    Column('Сумма', Float),
                    Column('ЭтоВнутригрупповойОборот', Boolean),
                    Column('ДатаЗагрузки', DateTime),
                    schema='rsrc')

JobPositions = Table('rs1c_zup_job_positions', metadata,
                     Column('Должность', Text),
                     Column('Наименование', Text),
                     Column('ПометкаУдаления', Boolean),
                     schema='rsrc')

Contractors = Table('rs1c_zup_contractors', metadata,
                    Column('ДатаНачала', DateTime),
                    Column('ДатаОкончания', DateTime),
                    Column('Договор', Text),
                    Column('Сотрудник', Text),
                    Column('Организация', Text),
                    Column('Подразделение', Text),
                    schema='rsrc')

Departments = Table('rs1c_zup_departments', metadata,
                    Column('Код', Text),
                    Column('Наименование', Text),
                    Column('ОбособленноеПодразделение', Boolean),
                    Column('КПП', Text),
                    Column('Сформировано', Boolean),
                    Column('ДатаСоздания', DateTime),
                    Column('Расформировано', Boolean),
                    Column('ДатаРасформирования', DateTime),
                    Column('ПометкаУдаления', Boolean),
                    Column('Подразделение', Text),
                    Column('Организация', Text),
                    Column('Родитель', Text),
                    Column('Руководитель', Text),
                    Column('ПозицияРуководителя', Text),
                    schema='rsrc')

Employees = Table('rs1c_zup_employees', metadata,
                  Column('Наименование', Text),
                  Column('ТабельныйНомер', Text),
                  Column('ФИО', Text),
                  Column('ДатаПриема', DateTime),
                  Column('ДатаУвольнения', DateTime),
                  Column('ИспытательныйСрокДатаЗавершения', DateTime),
                  Column('Сотрудник', Text),
                  Column('Организация', Text),
                  Column('ФизическоеЛицо', Text),
                  Column('Подразделение', Text),
                  Column('Должность', Text),
                  Column('ВидЗанятости', Text),
                  Column('ВидДоговора', Text),
                  schema='rsrc')

StaffTable = Table('rs1c_zup_staff_table', metadata,
                   Column('Наименование', Text),
                   Column('Утверждена', Boolean),
                   Column('ДатаУтверждения', DateTime),
                   Column('Закрыта', Boolean),
                   Column('ДатаЗакрытия', DateTime),
                   Column('КатегорияПерсонала', Text),
                   Column('Позиция', Text),
                   Column('Организация', Text),
                   Column('Подразделение', Text),
                   Column('Должность', Text),
                   schema='rsrc')

StaffTableExceptions = Table('rs1c_zup_staff_table_exceptions', metadata,
                             Column('ДатаНачала', DateTime),
                             Column('ДатаОкончания', DateTime),
                             Column('КоличествоСтавок', Float),
                             Column('Позиция', Text),
                             schema='rsrc')

StaffTableOccupation = Table('rs1c_zup_staff_table_occupation', metadata,
                             Column('ДатаНачала', DateTime),
                             Column('ДатаОкончания', DateTime),
                             Column('ВидЗанятостиПозиции', Text),
                             Column('КоличествоСтавок', Float),
                             Column('РегистраторСобытия', Text),
                             Column('Сотрудник', Text),
                             Column('Позиция', Text),
                             schema='rsrc')

PersonAccounts = Table('rs1c_zup_person_accounts', metadata,
                       Column('ИнформационнаяСистема', Text),
                       Column('Идентификатор', Text),
                       Column('ИмяПользователя', Text),
                       Column('ПредставлениеПользователя', Text),
                       Column('Действует', Boolean),
                       Column('ФизическоеЛицо', Text),
                       schema='rsrc')

Sellers = Table('rs1c_zup_sellers', metadata,
                Column('Продавец', Text),
                Column('Наименование', Text),
                Column('ПометкаУдаления', Boolean),
                Column('Сотрудник', Text),
                schema='rsrc')

SellersGroups = Table('rs1c_zup_sellers_groups', metadata,
                      Column('ГруппаПродавцов', Text),
                      Column('Наименование', Text),
                      Column('ПометкаУдаления', Boolean),
                      schema='rsrc')

SalesIndicators = Table('rs1c_zup_sales_indicators', metadata,
                        Column('ПоказательПродаж', Text),
                        Column('Наименование', Text),
                        Column('ПометкаУдаления', Boolean),
                        Column('Точность', Integer),
                        Column('ЭтоПроцент', Boolean),
                        schema='rsrc')

EmployeesRanks = Table('rs1c_zup_employees_ranks', metadata,
                       Column('Период', DateTime),
                       Column('Сотрудник', Text),
                       Column('Звание', Text),
                       Column('ЗваниеДляНадбавки', Text),
                       schema='rsrc')

CatalogAdaptation = Table('rs1c_zup_catalog_adaptation', metadata,
                          Column('Мероприятие', Text),
                          Column('Группа', Text),
                          Column('ГруппаНаименование', Text),
                          Column('Наименование', Text),
                          Column('Описание', Text),
                          Column('ПометкаУдаления', Boolean),
                          schema='rsrc')

EmployeesHistory = Table('rs1c_zup_employees_history', metadata,
                         Column('Период', DateTime),
                         Column('Регистратор', Text),
                         Column('ВидСобытия', Text),
                         Column('Ставок', Integer),
                         Column('Сотрудник', Text),
                         Column('Подразделение', Text),
                         Column('Должность', Text),
                         Column('Позиция', Text),
                         schema='rsrc')

StaffTableHistory = Table('rs1c_zup_staff_table_history', metadata,
                          Column('Регистратор', Text),
                          Column('Дата', DateTime),
                          Column('Используется', Boolean),
                          Column('КоличествоСтавок', Float),
                          Column('Позиция', Text),
                          schema='rsrc')

Tutors = Table('rs1c_zup_tutors', metadata,
               Column('ДатаКомиссии', DateTime),
               Column('СотрудникНаставник', Text),
               Column('ТипОперации', Text),
               schema='rsrc')

SellersGroupsStructure = Table('rs1c_zup_sellers_groups_structure', metadata,
                               Column('Период', DateTime),
                               Column('Продавец', Text),
                               Column('ГруппаПродавцов', Text),
                               schema='rsrc')

SalesGroupsPlan = Table('rs1c_zup_sales_groups_plan', metadata,
                        Column('Период', DateTime),
                        Column('ГруппаПродавцов', Text),
                        Column('Звание', Text),
                        Column('Показатель', Text),
                        Column('Значение', Integer),
                        schema='rsrc')

SalesPlan = Table('rs1c_zup_sales_plan', metadata,
                  Column('Период', DateTime),
                  Column('Продавец', Text),
                  Column('Показатель', Text),
                  Column('Значение', Integer),
                  schema='rsrc')

RecruitmentDecision = Table('rs1c_zup_recruitment_decison', metadata,
                            Column('Решение', Text),
                            Column('Организация', Text),
                            Column('ФизическоеЛицо', Text),
                            Column('Ответственный', Text),
                            Column('Позиция', Text),
                            Column('ДатаРешения', DateTime),
                            Column('НомерРешения', Text),
                            Column('Проведено', Boolean),
                            schema='rsrc')

Trainings = Table('rs1c_zup_trainings', metadata,
                  Column('ДатаОперации', DateTime),
                  Column('СотрудникНаставник', Text),
                  Column('СотрудникСтажер', Text),
                  Column('ТипОперации', Text),
                  schema='rsrc')

AdaptationTasks = Table('rs1c_zup_adaptation_tasks', metadata,
                        Column('Задача', Text),
                        Column('Решение', Text),
                        Column('Мероприятие', Text),
                        Column('СотрудникИсполнитель', Text),
                        Column('ДатаНачала', DateTime),
                        Column('СрокИсполнения', DateTime),
                        schema='rsrc')

BonusWorkTime = Table('rs1c_zup_bonus_work_time', metadata,
                      Column('Период', DateTime),
                      Column('Сотрудник', UUID),
                      Column('НормаДней', Integer),
                      Column('ДнейОтпуска', Integer),
                      Column('ДнейВДекрете', Integer),
                      Column('ДнейБольничного', Integer),
                      schema='rsrc')

CommonDepartmentsHierarchy = Table('common_departments_hierarchy', metadata,
                                   Column('organisation_code', Text),
                                   Column('department_head', Text),
                                   Column('department_body', Text),
                                   Column('department_tail', Text),
                                   Column('last_node_code', Text),
                                   schema='nrml')

DoManagementStructureHeadsHistory = Table('rs1c_do_management_structure_heads_history', metadata,
                                          Column('Структура', Text),
                                          Column('ФизическоеЛицоРуководитель', Text),
                                          Column('ДатаНачала', DateTime),
                                          Column('ДатаОкончания', DateTime),
                                          schema='nrml')

DoManagementStructureOccupationHistory = Table('rs1c_do_management_structure_occupation_history', metadata,
                                               Column('Структура', Text),
                                               Column('ФизическоеЛицо', Text),
                                               Column('ДатаНачала', DateTime),
                                               Column('ДатаОкончания', DateTime),
                                               schema='nrml')

CommonWorkDaysCalendar = Table('common_work_days_calendar', metadata,
                               Column('rn', Integer),
                               Column('dt', DateTime),
                               Column('prev_dt', DateTime),
                               Column('prev_dt_delta', Float),
                               schema='nrml')

CatalogAccount = Table('rs1c_cons_catalog_account', metadata,
                       Column('Счет', Text),
                       Column('Код', Text),
                       Column('Наименование', Text),
                       Column('ПометкаУдаления', Boolean),
                       schema='rsrc')

CatalogBankAccount = Table('rs1c_cons_catalog_bank_account', metadata,
                           Column('БанковскийСчет', Text),
                           Column('Организация', Text),
                           Column('Валютный', Boolean),
                           Column('Валюта', Text),
                           Column('Наименование', Text),
                           Column('ПометкаУдаления', Boolean),
                           schema='rsrc')

CatalogStDDS = Table('rs1c_cons_catalog_st_dds', metadata,
                     Column('СтатьяДДС', Text),
                     Column('ЭтоГруппа', Boolean),
                     Column('Родитель', Text),
                     Column('Наименование', Text),
                     Column('ПометкаУдаления', Boolean),
                     schema='rsrc')

ConsCashflow = Table('rs1c_cons_cashflow', metadata,
                     Column('Период', DateTime),
                     Column('Организация', Text),
                     Column('СтатьяДДС', Text),
                     Column('Валюта', Text),
                     Column('БанковскийСчет', Text),
                     Column('Счет', Text),
                     Column('Контрагент', Text),
                     Column('ВГО', Boolean),
                     Column('СуммаОборот', Float),
                     Column('СуммаПриход', Float),
                     Column('СуммаРасход', Float),
                     Column('ДатаЗагрузки', DateTime),
                     schema='rsrc')


metadata.create_all(engine)
print('Выполнено')
