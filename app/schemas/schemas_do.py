from typing import Optional

from app.core.templates.schema import TemplateModel


class ManagementStructureHeads(TemplateModel):
    Структура: str
    ФизическоеЛицоРуководитель: str
    ПометкаУдаления: bool


class ManagementStructureOccupation(TemplateModel):
    Структура: str
    ФизическоеЛицо: str
    ПометкаУдаления: bool


class ManagementStructure(TemplateModel):
    Структура: str
    Родитель: str
    СтруктураНаименование: str
    Подразделение: Optional[str]
