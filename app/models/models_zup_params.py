from sqlalchemy import Column, Text, Integer, Boolean, DateTime, Float

from app.db.base import Base


class EmployeesHistory(Base):
    __tablename__ = 'rs1c_zup_employees_history'
    __table_args__ = {'schema': 'rsrc'}
    __filterfield__ = 'Период'

    Период = Column(DateTime)
    Регистратор = Column(Text, primary_key=True)
    ВидСобытия = Column(Text, primary_key=True)
    Ставок = Column(Integer)
    Сотрудник = Column(Text, primary_key=True)
    Подразделение = Column(Text, primary_key=True)
    Должность = Column(Text, primary_key=True)
    Позиция = Column(Text, primary_key=True)


class StaffTableHistory(Base):
    __tablename__ = 'rs1c_zup_staff_table_history'
    __table_args__ = {'schema': 'rsrc'}
    __filterfield__ = 'Дата'

    Регистратор = Column(Text, primary_key=True)
    Дата = Column(DateTime)
    Используется = Column(Boolean)
    КоличествоСтавок = Column(Float)
    Позиция = Column(Text, primary_key=True)


class Tutors(Base):
    __tablename__ = 'rs1c_zup_tutors'
    __table_args__ = {'schema': 'rsrc'}
    __filterfield__ = 'ДатаКомиссии'

    ДатаКомиссии = Column(DateTime)
    СотрудникНаставник = Column(Text, primary_key=True)
    ТипОперации = Column(Text, primary_key=True)


class SellersGroupsStructure(Base):
    __tablename__ = 'rs1c_zup_sellers_groups_structure'
    __table_args__ = {'schema': 'rsrc'}
    __filterfield__ = 'Период'

    Период = Column(DateTime)
    Продавец = Column(Text, primary_key=True)
    ГруппаПродавцов = Column(Text, primary_key=True)


class SalesGroupsPlan(Base):
    __tablename__ = 'rs1c_zup_sales_groups_plan'
    __table_args__ = {'schema': 'rsrc'}
    __filterfield__ = 'Период'

    Период = Column(DateTime)
    ГруппаПродавцов = Column(Text, primary_key=True)
    Звание = Column(Text, primary_key=True)
    Показатель = Column(Text, primary_key=True)
    Значение = Column(Integer)


class SalesPlan(Base):
    __tablename__ = 'rs1c_zup_sales_plan'
    __table_args__ = {'schema': 'rsrc'}
    __filterfield__ = 'Период'

    Период = Column(DateTime)
    Продавец = Column(Text, primary_key=True)
    Показатель = Column(Text, primary_key=True)
    Значение = Column(Integer)


class RecruitmentDecision(Base):
    __tablename__ = 'rs1c_zup_recruitment_decison'
    __table_args__ = {'schema': 'rsrc'}
    __filterfield__ = 'ДатаРешения'

    Решение = Column(Text, primary_key=True)
    Организация = Column(Text, primary_key=True)
    ФизическоеЛицо = Column(Text, primary_key=True)
    Ответственный = Column(Text, primary_key=True)
    Позиция = Column(Text, primary_key=True)
    ДатаРешения = Column(DateTime)
    НомерРешения = Column(Text, primary_key=True)
    Проведено = Column(Boolean)


class Trainings(Base):
    __tablename__ = 'rs1c_zup_trainings'
    __table_args__ = {'schema': 'rsrc'}
    __filterfield__ = 'ДатаОперации'

    ДатаОперации = Column(DateTime)
    СотрудникНаставник = Column(Text, primary_key=True)
    СотрудникСтажер = Column(Text, primary_key=True)
    ТипОперации = Column(Text, primary_key=True)


class AdaptationTasks(Base):
    __tablename__ = 'rs1c_zup_adaptation_tasks'
    __table_args__ = {'schema': 'rsrc'}
    __filterfield__ = 'ДатаНачала'

    Задача = Column(Text, primary_key=True)
    Решение = Column(Text, primary_key=True)
    Мероприятие = Column(Text, primary_key=True)
    СотрудникИсполнитель = Column(Text, primary_key=True)
    ДатаНачала = Column(DateTime)
    СрокИсполнения = Column(DateTime)
