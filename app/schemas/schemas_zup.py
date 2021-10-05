from typing import Optional
from datetime import datetime

from app.core.templates.schema import TemplateModel


class JobPositions(TemplateModel):
    Должность: str
    Наименование: str
    ПометкаУдаления: bool


class Contractors(TemplateModel):
    ДатаНачала: datetime
    ДатаОкончания: datetime
    Договор: str
    Сотрудник: str
    Организация: str
    Подразделение: str


class Departments(TemplateModel):
    Код: str
    Наименование: str
    ОбособленноеПодразделение: bool
    КПП: str
    Сформировано: bool
    ДатаСоздания: datetime
    Расформировано: bool
    ДатаРасформирования: datetime
    ПометкаУдаления: bool
    Подразделение: str
    Организация: str
    Родитель: str
    Руководитель: Optional[str]
    ПозицияРуководителя: Optional[str]


class Employees(TemplateModel):
    Наименование: str
    ТабельныйНомер: str
    ФИО: str
    ДатаПриема: datetime
    ДатаУвольнения: datetime
    ИспытательныйСрокДатаЗавершения: datetime
    Сотрудник: str
    Организация: str
    ФизическоеЛицо: str
    Подразделение: str
    Должность: str
    ВидЗанятости: str
    ВидДоговора: str


class StaffTable(TemplateModel):
    Наименование: str
    Утверждена: bool
    ДатаУтверждения: datetime
    Закрыта: bool
    ДатаЗакрытия: datetime
    КатегорияПерсонала: Optional[str]
    Позиция: str
    Организация: str
    Подразделение: str
    Должность: str


class StaffTableExceptions(TemplateModel):
    ДатаНачала: datetime
    ДатаОкончания: datetime
    КоличествоСтавок: float
    Позиция: str


class StaffTableOccupation(TemplateModel):
    ДатаНачала: datetime
    ДатаОкончания: datetime
    ВидЗанятостиПозиции: str
    КоличествоСтавок: float
    РегистраторСобытия: str
    Сотрудник: str
    Позиция: str


class PersonAccounts(TemplateModel):
    ИнформационнаяСистема: str
    Идентификатор: str
    ИмяПользователя: str
    ПредставлениеПользователя: str
    Действует: bool
    ФизическоеЛицо: str


class Sellers(TemplateModel):
    Продавец: str
    Наименование: str
    ПометкаУдаления: bool
    Сотрудник: str


class SellersGroups(TemplateModel):
    ГруппаПродавцов: str
    Наименование: str
    ПометкаУдаления: bool


class SalesIndicators(TemplateModel):
    ПоказательПродаж: str
    Наименование: str
    ПометкаУдаления: bool
    Точность: int
    ЭтоПроцент: bool


class EmployeesRanks(TemplateModel):
    Период: datetime
    Сотрудник: str
    Звание: str
    ЗваниеДляНадбавки: Optional[str]


class CatalogAdaptation(TemplateModel):
    Мероприятие: str
    Группа: str
    ГруппаНаименование: str
    Наименование: str
    Описание: str
    ПометкаУдаления: bool
