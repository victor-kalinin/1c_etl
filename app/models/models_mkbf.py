from sqlalchemy import Column, Text, Boolean, DateTime, JSON

from app.db.base import Base


class CatalogCfo(Base):
    __tablename__ = 'rs1c_mkbf_catalog_cfo'
    __table_args__ = {'schema': 'rsrc'}
    
    ЦФО = Column(Text, primary_key=True)
    Родитель = Column(Text, primary_key=True)
    Код = Column(Text, primary_key=True)
    Наименование = Column(Text, primary_key=True)
    ПометкаУдаления = Column(Boolean)


class CatalogPodr(Base):
    __tablename__ = 'rs1c_mkbf_catalog_podr'
    __table_args__ = {'schema': 'rsrc'}
    
    Подразделение = Column(Text, primary_key=True)
    Организация = Column(Text, primary_key=True)
    Родитель = Column(Text, primary_key=True)
    Код = Column(Text, primary_key=True)
    Наименование = Column(Text, primary_key=True)
    ОбособленноеПодразделение = Column(Boolean)
    ПометкаУдаления = Column(Boolean)


class CatalogStOb(Base):
    __tablename__ = 'rs1c_mkbf_catalog_st_ob'
    __table_args__ = {'schema': 'rsrc'}
    
    СтатьиОборотов = Column(Text, primary_key=True)
    ЭтоГруппа = Column(Boolean)
    Наименование = Column(Text, primary_key=True)
    ТипСтатьи = Column(Text)
    Кодификатор = Column(Text)
    Направление = Column(Text)
    Родитель = Column(Text, primary_key=True)
    ТипРаспределения = Column(Text)
    ПометкаУдаления = Column(Boolean)


class CatalogTypeRsp(Base):
    __tablename__ = 'rs1c_mkbf_catalog_type_rsp'
    __table_args__ = {'schema': 'rsrc'}
    
    ТипРаспределения = Column(Text, primary_key=True)
    Наименование = Column(Text, primary_key=True)
    ПометкаУдаления = Column(Boolean)


class CatalogNg(Base):
    __tablename__ = 'rs1c_mkbf_catalog_ng'
    __table_args__ = {'schema': 'rsrc'}
    
    НоменклатурнаяГруппа = Column(Text, primary_key=True)
    ЭтоГруппа = Column(Boolean)
    Наименование = Column(Text, primary_key=True)
    ТипСтатьи = Column(Text)
    Кодификатор = Column(Text)
    Родитель = Column(Text, primary_key=True)
    ПометкаУдаления = Column(Boolean)


class CatalogScenariy(Base):
    __tablename__ = 'rs1c_mkbf_catalog_scenariy'
    __table_args__ = {'schema': 'rsrc'}
    
    Сценарий = Column(Text, primary_key=True)
    ЭтоГруппа = Column(Boolean)
    Родитель = Column(Text, primary_key=True)
    Наименование = Column(Text, primary_key=True)
    ПометкаУдаления = Column(Boolean)


class Documents(Base):
    __tablename__ = 'rs1c_mkbf_documents'
    __table_args__ = {'schema': 'rsrc'}
    
    Ссылка = Column(Text, primary_key=True)
    Номер = Column(Text, primary_key=True)
    Дата = Column(DateTime)
    НГ_Ссылка = Column(Text, primary_key=True)
    НГ_Код = Column(Text, primary_key=True)
    НГ_Наименование = Column(Text, primary_key=True)
    ПроцентРаспределенияНаПродукт = Column(JSON)
