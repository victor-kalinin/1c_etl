from typing import Optional
from datetime import datetime

from app.core.templates.schema import TemplateModel


class ConsAccum(TemplateModel):
    Период: datetime
    Организация: Optional[str]
    Сценарий: str
    ЦФО: str
    ЦФОКод: Optional[str]
    ЦФОНаименование: Optional[str]
    СтатьяОборотов: str
    НоменклатурнаяГруппа: str
    Контрагент: Optional[str]
    Сумма: float
    ЭтоПлан: bool
    ЭтоВнутригрупповойОборот: bool
    ЭтоКорректировка: bool


class ConsCashflow(TemplateModel):
    Период: datetime
    Организация: str
    СтатьяДДС: str
    Валюта: Optional[str]
    БанковскийСчет: str
    Счет: str
    Контрагент: Optional[str]
    ВГО: bool
    СуммаОборот: float
    СуммаПриход: float
    СуммаРасход: float
