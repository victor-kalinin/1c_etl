from typing import Optional, Any, Dict, List
from pydantic import Json, BaseModel
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
    ТипСтатьи: Optional[str]
    Кодификатор: Optional[str]
    Направление: Optional[str]
    Родитель: str
    ТипРаспределения: Optional[str]
    ПометкаУдаления: bool


class CatalogTypeRsp(TemplateModel):
    ТипРаспределения: str
    Наименование: str
    ПометкаУдаления: bool


class CatalogNg(TemplateModel):
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
    ПроцентРаспределенияНаПродукт: List[Dict[str, Any]]
