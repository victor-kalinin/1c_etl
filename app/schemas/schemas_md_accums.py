from typing import Optional
from datetime import datetime

from app.core.templates.schema import TemplateModel


class MDAccum(TemplateModel):
    Период: datetime
    Сценарий: str
    ЦФО: str
    ЦФОКод: Optional[str]
    ЦФОНаименование: Optional[str]
    СтатьяОборотов: str
    НоменклатурнаяГруппа: str
    ПодразделениеОрганизации: str
    СчетчикПодрОрг: int
    Количество: int
    Сумма: float
    ЭтоПлан: bool
    ЭтоВнутригрупповойОборот: bool
    Продукция: str
