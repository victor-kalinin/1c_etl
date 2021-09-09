from sqlalchemy import Column, Text, Boolean, DateTime, Float
from datetime import datetime

from app.db.base import Base


class ConsAccum(Base):
    __tablename__ = 'rs1c_cons_accum'
    __table_args__ = {'schema': 'rsrc'}
    __filterfield__ = 'Период'
    
    Период = Column(DateTime)
    Организация = Column(Text)
    Сценарий = Column(Text, primary_key=True)
    ЦФО = Column(Text, primary_key=True)
    ЦФОКод = Column(Text)
    ЦФОНаименование = Column(Text)
    СтатьяОборотов = Column(Text, primary_key=True)
    НоменклатурнаяГруппа = Column(Text, primary_key=True)
    Контрагент = Column(Text)
    Сумма = Column(Float)
    ЭтоПлан = Column(Boolean)
    ЭтоВнутригрупповойОборот = Column(Boolean)
    ЭтоКорректировка = Column(Boolean)
    ДатаЗагрузки = Column(DateTime, default=datetime.now)


class ConsCashflow(Base):
    __tablename__ = 'rs1c_cons_cashflow'
    __table_args__ = {'schema': 'rsrc'}
    __filterfield__ = 'Период'

    Период = Column(DateTime)
    Организация = Column(Text, primary_key=True)
    СтатьяДДС = Column(Text, primary_key=True)
    Валюта = Column(Text)
    БанковскийСчет = Column(Text, primary_key=True)
    Счет = Column(Text, primary_key=True)
    Контрагент = Column(Text)
    ВГО = Column(Boolean)
    СуммаОборот = Column(Float)
    СуммаПриход = Column(Float)
    СуммаРасход = Column(Float)
    ДатаЗагрузки = Column(DateTime, default=datetime.now)
