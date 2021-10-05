from typing import Optional
from datetime import datetime

from app.core.templates.schema import TemplateModel


class DoTasksTracking(TemplateModel):
    Задача: Optional[str]
    ЗадачаЗУП: Optional[str]
    ТипЗадачи: Optional[str]
    Исполнитель: Optional[str]
    ДатаВыполнения: Optional[datetime]
    Выполнена: Optional[bool]
    СтатусПроцесса: Optional[str]
