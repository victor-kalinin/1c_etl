from datetime import datetime

from app.core.templates.schema import TemplateModel


class BonusWorkTime(TemplateModel):
    Период: datetime
    Сотрудник: str
    НормаДней: int
    ДнейОтпуска: int
    ДнейВДекрете: int
    ДнейБольничного: int
