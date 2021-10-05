from datetime import datetime

from app.core.templates.schema import TemplateModel


class Accum(TemplateModel):
    Период: datetime
    Сценарий: str
    ЦФО: str
    ЦФОКод: str
    ЦФОНаименование: str
    СтатьяОборотов: str
    НоменклатурнаяГруппа: str
    ПодразделениеОрганизации: str
    СчетчикПодрОрг: int
    Количество: int
    Сумма: float
    ЭтоПлан: bool
    ЭтоВнутригрупповойОборот: bool


class AccumPl(TemplateModel):
    Период: datetime
    Организация: str
    Валюта: str
    Сценарий: str
    Продукт: str
    ЦФО: str
    ЦФОКод: str
    ЦФОНаименование: str
    СтатьяОборотов: str
    Сумма: float
    ЭтоВнутригрупповойОборот: bool
