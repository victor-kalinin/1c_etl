from typing import Optional
from pydantic import Json
from datetime import datetime

from app.core.templates.schema import TemplateModel


class CatalogCfo(TemplateModel):
    ЦФО: str
    Родитель: str
    Код: str
    Наименование: str
    ПометкаУдаления: bool


class CatalogPodr(TemplateModel):
    Подразделение: str
    Организация: str
    Родитель: str
    Код: str
    Наименование: str
    ОбособленноеПодразделение: bool
    ПометкаУдаления: bool


class CatalogStOb(TemplateModel):
    СтатьиОборотов: str
    ЭтоГруппа: bool
    Наименование: str
    ТипСтатьи: str
    Кодификатор: str
    Направление: str
    Родитель: str
    ТипРаспределения: str
    ПометкаУдаления: bool


class CatalogTypeRsp(TemplateModel):
    ТипРаспределения: str
    Наименование: str
    ПометкаУдаления: bool


class CatalogNom(TemplateModel):
    Ссылка: str
    Код: str
    Наименование: str
    ПометкаУдаления: bool


class CatalogNomGroups(TemplateModel):
    НоменклатурнаяГруппа: str
    ЭтоГруппа: bool
    Наименование: str
    ТипСтатьи: Optional[str]
    Кодификатор: Optional[str]
    Родитель: str
    ПометкаУдаления: bool


class CatalogScenariy(TemplateModel):
    Сценарий: str
    ЭтоГруппа: bool
    Родитель: str
    Наименование: str
    ПометкаУдаления: bool


class Documents(TemplateModel):
    Ссылка: str
    Номер: str
    Дата: datetime
    НГ_Ссылка: str
    НГ_Код: str
    НГ_Наименование: str
    ПроцентРаспределенияНаПродукт = Json
