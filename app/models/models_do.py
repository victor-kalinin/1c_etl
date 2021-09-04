from sqlalchemy import Column, Text, Boolean

from app.db.base import Base


class ManagementStructureHeads(Base):
    __tablename__ = 'rs1c_do_management_structure_heads'
    __table_args__ = {'schema': 'rsrc'}
    __post_execute__ = 'nrml.reload_mstructure_heads_history()'
    
    Структура = Column(Text, primary_key=True)
    ФизическоеЛицоРуководитель = Column(Text, primary_key=True)
    ПометкаУдаления = Column(Boolean)


class ManagementStructureOccupation(Base):
    __tablename__ = 'rs1c_do_management_structure_occupation'
    __table_args__ = {'schema': 'rsrc'}
    __post_execute__ = 'nrml.reload_mstructure_occupation_history()'
    
    Структура = Column(Text, primary_key=True)
    ФизическоеЛицо = Column(Text, primary_key=True)
    ПометкаУдаления = Column(Boolean)


class ManagementStructure(Base):
    __tablename__ = 'rs1c_do_management_structure'
    __table_args__ = {'schema': 'rsrc'}
    
    Структура = Column(Text, primary_key=True)
    Родитель = Column(Text, primary_key=True)
    СтруктураНаименование = Column(Text, primary_key=True)
    Подразделение = Column(Text)
