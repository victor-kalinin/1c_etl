from sqlalchemy import Column, Text, Integer, Boolean, DateTime, Float

from app.db.base import Base


class JobPositions(Base):
    __tablename__ = 'rs1c_zup_job_positions'
    __table_args__ = {'schema': 'rsrc'}

    Должность = Column(Text, primary_key=True)
    Наименование = Column(Text, primary_key=True)
    ПометкаУдаления = Column(Boolean)


class Contractors(Base):
    __tablename__ = 'rs1c_zup_contractors'
    __table_args__ = {'schema': 'rsrc'}

    ДатаНачала = Column(DateTime)
    ДатаОкончания = Column(DateTime)
    Договор = Column(Text, primary_key=True)
    Сотрудник = Column(Text, primary_key=True)
    Организация = Column(Text, primary_key=True)
    Подразделение = Column(Text, primary_key=True)


class Departments(Base):
    __tablename__ = 'rs1c_zup_departments'
    __table_args__ = {'schema': 'rsrc'}
    __post_execute__ = 'nrml.reload_dep_hierarchy'

    Код = Column(Text, primary_key=True)
    Наименование = Column(Text, primary_key=True)
    ОбособленноеПодразделение = Column(Boolean)
    КПП = Column(Text, primary_key=True)
    Сформировано = Column(Boolean)
    ДатаСоздания = Column(DateTime)
    Расформировано = Column(Boolean)
    ДатаРасформирования = Column(DateTime)
    ПометкаУдаления = Column(Boolean)
    Подразделение = Column(Text, primary_key=True)
    Организация = Column(Text, primary_key=True)
    Родитель = Column(Text, primary_key=True)
    Руководитель = Column(Text)
    ПозицияРуководителя = Column(Text)


class Employees(Base):
    __tablename__ = 'rs1c_zup_employees'
    __table_args__ = {'schema': 'rsrc'}

    Наименование = Column(Text, primary_key=True)
    ТабельныйНомер = Column(Text, primary_key=True)
    ФИО = Column(Text, primary_key=True)
    ДатаПриема = Column(DateTime)
    ДатаУвольнения = Column(DateTime)
    ИспытательныйСрокДатаЗавершения = Column(DateTime)
    Сотрудник = Column(Text, primary_key=True)
    Организация = Column(Text, primary_key=True)
    ФизическоеЛицо = Column(Text, primary_key=True)
    Подразделение = Column(Text, primary_key=True)
    Должность = Column(Text, primary_key=True)
    ВидЗанятости = Column(Text, primary_key=True)
    ВидДоговора = Column(Text, primary_key=True)


class StaffTable(Base):
    __tablename__ = 'rs1c_zup_staff_table'
    __table_args__ = {'schema': 'rsrc'}

    Наименование = Column(Text, primary_key=True)
    Утверждена = Column(Boolean)
    ДатаУтверждения = Column(DateTime)
    Закрыта = Column(Boolean)
    ДатаЗакрытия = Column(DateTime)
    КатегорияПерсонала = Column(Text)
    Позиция = Column(Text, primary_key=True)
    Организация = Column(Text, primary_key=True)
    Подразделение = Column(Text, primary_key=True)
    Должность = Column(Text, primary_key=True)


class StaffTableExceptions(Base):
    __tablename__ = 'rs1c_zup_staff_table_exceptions'
    __table_args__ = {'schema': 'rsrc'}

    ДатаНачала = Column(DateTime)
    ДатаОкончания = Column(DateTime)
    КоличествоСтавок = Column(Float)
    Позиция = Column(Text, primary_key=True)


class StaffTableOccupation(Base):
    __tablename__ = 'rs1c_zup_staff_table_occupation'
    __table_args__ = {'schema': 'rsrc'}

    ДатаНачала = Column(DateTime)
    ДатаОкончания = Column(DateTime)
    ВидЗанятостиПозиции = Column(Text, primary_key=True)
    КоличествоСтавок = Column(Float)
    РегистраторСобытия = Column(Text, primary_key=True)
    Сотрудник = Column(Text, primary_key=True)
    Позиция = Column(Text, primary_key=True)


class PersonAccounts(Base):
    __tablename__ = 'rs1c_zup_person_accounts'
    __table_args__ = {'schema': 'rsrc'}

    ИнформационнаяСистема = Column(Text, primary_key=True)
    Идентификатор = Column(Text, primary_key=True)
    ИмяПользователя = Column(Text, primary_key=True)
    ПредставлениеПользователя = Column(Text, primary_key=True)
    Действует = Column(Boolean)
    ФизическоеЛицо = Column(Text, primary_key=True)


class Sellers(Base):
    __tablename__ = 'rs1c_zup_sellers'
    __table_args__ = {'schema': 'rsrc'}

    Продавец = Column(Text, primary_key=True)
    Наименование = Column(Text, primary_key=True)
    ПометкаУдаления = Column(Boolean)
    Сотрудник = Column(Text, primary_key=True)


class SellersGroups(Base):
    __tablename__ = 'rs1c_zup_sellers_groups'
    __table_args__ = {'schema': 'rsrc'}

    ГруппаПродавцов = Column(Text, primary_key=True)
    Наименование = Column(Text, primary_key=True)
    ПометкаУдаления = Column(Boolean)


class SalesIndicators(Base):
    __tablename__ = 'rs1c_zup_sales_indicators'
    __table_args__ = {'schema': 'rsrc'}

    ПоказательПродаж = Column(Text, primary_key=True)
    Наименование = Column(Text, primary_key=True)
    ПометкаУдаления = Column(Boolean)
    Точность = Column(Integer)
    ЭтоПроцент = Column(Boolean)


class EmployeesRanks(Base):
    __tablename__ = 'rs1c_zup_employees_ranks'
    __table_args__ = {'schema': 'rsrc'}

    Период = Column(DateTime)
    Сотрудник = Column(Text, primary_key=True)
    Звание = Column(Text, primary_key=True)
    ЗваниеДляНадбавки = Column(Text)


class CatalogAdaptation(Base):
    __tablename__ = 'rs1c_zup_catalog_adaptation'
    __table_args__ = {'schema': 'rsrc'}

    Мероприятие = Column(Text, primary_key=True)
    Группа = Column(Text, primary_key=True)
    ГруппаНаименование = Column(Text, primary_key=True)
    Наименование = Column(Text, primary_key=True)
    Описание = Column(Text, primary_key=True)
    ПометкаУдаления = Column(Boolean)
