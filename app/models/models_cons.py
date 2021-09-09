from sqlalchemy import Column, Text, Boolean, DateTime, JSON

from app.db.base import Base


class CatalogCfo(Base):
    __tablename__ = 'rs1c_cons_catalog_cfo'
    __table_args__ = {'schema': 'rsrc'}
    
    ЦФО = Column(Text, primary_key=True)
    Родитель = Column(Text, primary_key=True)
    Код = Column(Text, primary_key=True)
    Наименование = Column(Text, primary_key=True)
    ПометкаУдаления = Column(Boolean)


class CatalogStOb(Base):
    __tablename__ = 'rs1c_cons_catalog_st_ob'
    __table_args__ = {'schema': 'rsrc'}
    
    СтатьиОборотов = Column(Text, primary_key=True)
    ЭтоГруппа = Column(Boolean)
    Наименование = Column(Text, primary_key=True)
    ТипСтатьи = Column(Text, primary_key=True)
    Кодификатор = Column(Text, primary_key=True)
    Направление = Column(Text, primary_key=True)
    Родитель = Column(Text, primary_key=True)
    ПометкаУдаления = Column(Boolean)


class CatalogNg(Base):
    __tablename__ = 'rs1c_cons_catalog_ng'
    __table_args__ = {'schema': 'rsrc'}
    
    НоменклатурнаяГруппа = Column(Text, primary_key=True)
    ЭтоГруппа = Column(Boolean)
    Наименование = Column(Text, primary_key=True)
    Родитель = Column(Text, primary_key=True)
    ПометкаУдаления = Column(Boolean)


class CatalogScenariy(Base):
    __tablename__ = 'rs1c_cons_catalog_scenariy'
    __table_args__ = {'schema': 'rsrc'}
    
    Сценарий = Column(Text, primary_key=True)
    ЭтоГруппа = Column(Boolean)
    Родитель = Column(Text, primary_key=True)
    Наименование = Column(Text, primary_key=True)
    ПометкаУдаления = Column(Boolean)


class CatalogAccount(Base):
    __tablename__ = 'rs1c_cons_catalog_account'
    __table_args__ = {'schema': 'rsrc'}

    Счет = Column(Text, primary_key=True)
    Код = Column(Text, primary_key=True)
    Наименование = Column(Text, primary_key=True)
    ПометкаУдаления = Column(Boolean)


class CatalogBankAccount(Base):
    __tablename__ = 'rs1c_cons_catalog_bank_account'
    __table_args__ = {'schema': 'rsrc'}

    БанковскийСчет = Column(Text, primary_key=True)
    Организация = Column(Text, primary_key=True)
    Валютный = Column(Boolean)
    Валюта = Column(Text)
    Наименование = Column(Text, primary_key=True)
    ПометкаУдаления = Column(Boolean)


class CatalogStDDS(Base):
    __tablename__ = 'rs1c_cons_catalog_st_dds'
    __table_args__ = {'schema': 'rsrc'}

    СтатьяДДС = Column(Text, primary_key=True)
    ЭтоГруппа = Column(Boolean)
    Родитель = Column(Text, primary_key=True)
    Наименование = Column(Text, primary_key=True)
    ПометкаУдаления = Column(Boolean)
