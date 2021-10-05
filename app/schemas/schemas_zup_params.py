from datetime import datetime

from app.core.templates.schema import TemplateModel


class EmployeesHistory(TemplateModel):
    Период: datetime
    Регистратор: str
    ВидСобытия: str
    Ставок: float
    Сотрудник: str
    Подразделение: str
    Должность: str
    Позиция: str


class StaffTableHistory(TemplateModel):
    Регистратор: str
    Дата: datetime
    Используется: bool
    КоличествоСтавок: float
    Позиция: str


class Tutors(TemplateModel):
    ДатаКомиссии: datetime
    СотрудникНаставник: str
    ТипОперации: str


class SellersGroupsStructure(TemplateModel):
    Период: datetime
    Продавец: str
    ГруппаПродавцов: str


class SalesGroupsPlan(TemplateModel):
    Период: datetime
    ГруппаПродавцов: str
    Звание: str
    Показатель: str
    Значение: int


class SalesPlan(TemplateModel):
    Период: datetime
    Продавец: str
    Показатель: str
    Значение: int


class RecruitmentDecision(TemplateModel):
    Решение: str
    Организация: str
    ФизическоеЛицо: str
    Ответственный: str
    Позиция: str
    ДатаРешения: datetime
    НомерРешения: str
    Проведено: bool


class Trainings(TemplateModel):
    ДатаОперации: datetime
    СотрудникНаставник: str
    СотрудникСтажер: str
    ТипОперации: str


class AdaptationTasks(TemplateModel):
    Задача: str
    Решение: str
    Мероприятие: str
    СотрудникИсполнитель: str
    ДатаНачала: datetime
    СрокИсполнения: datetime
