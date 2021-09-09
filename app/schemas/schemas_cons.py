from app.core.templates.schema import TemplateModel


class CatalogCfo(TemplateModel):
    ЦФО: str
    Родитель: str
    Код: str
    Наименование: str
    ПометкаУдаления: bool


class CatalogStOb(TemplateModel):
    СтатьиОборотов: str
    ЭтоГруппа: bool
    Наименование: str
    ТипСтатьи: str
    Кодификатор: str
    Направление: str
    Родитель: str
    ПометкаУдаления: bool


class CatalogNg(TemplateModel):
    НоменклатурнаяГруппа: str
    ЭтоГруппа: bool
    Наименование: str
    Родитель: str
    ПометкаУдаления: bool


class CatalogScenariy(TemplateModel):
    Сценарий: str
    ЭтоГруппа: bool
    Родитель: str
    Наименование: str
    ПометкаУдаления: bool


class CatalogAccount(TemplateModel):
    Счет: str
    Код: str
    Наименование: str
    ПометкаУдаления: bool


class CatalogBankAccount(TemplateModel):
    БанковскийСчет: str
    Организация: str
    Валютный: bool
    Валюта: str
    Наименование: str
    ПометкаУдаления: bool


class CatalogStDDS(TemplateModel):
    СтатьяДДС: str
    ЭтоГруппа: bool
    Родитель: str
    Наименование: str
    ПометкаУдаления: bool
