from sqlalchemy import Column, Text, Integer, Boolean, DateTime, Float
from datetime import datetime

from app.db.base import Base


class Accum(Base):
    __tablename__ = 'rs1c_mkbf_accum'
    __table_args__ = {'schema': 'rsrc'}
    __filterfield__ = 'Период'

    Период = Column(DateTime)
    Сценарий = Column(Text, primary_key=True)
    ЦФО = Column(Text, primary_key=True)
    ЦФОКод = Column(Text, primary_key=True)
    ЦФОНаименование = Column(Text, primary_key=True)
    СтатьяОборотов = Column(Text, primary_key=True)
    НоменклатурнаяГруппа = Column(Text, primary_key=True)
    ПодразделениеОрганизации = Column(Text, primary_key=True)
    СчетчикПодрОрг = Column(Integer)
    Количество = Column(Integer)
    Сумма = Column(Float)
    ЭтоПлан = Column(Boolean)
    ЭтоВнутригрупповойОборот = Column(Boolean)
    ДатаЗагрузки = Column(DateTime, default=datetime.now)


class AccumPl(Base):
    __tablename__ = 'rs1c_mkbf_accum_pl'
    __table_args__ = {'schema': 'rsrc'}
    __filterfield__ = 'Период'

    Период = Column(DateTime)
    Организация = Column(Text, primary_key=True)
    Валюта = Column(Text, primary_key=True)
    Сценарий = Column(Text, primary_key=True)
    Продукт = Column(Text, primary_key=True)
    ЦФО = Column(Text, primary_key=True)
    ЦФОКод = Column(Text, primary_key=True)
    ЦФОНаименование = Column(Text, primary_key=True)
    СтатьяОборотов = Column(Text, primary_key=True)
    Сумма = Column(Float)
    ЭтоВнутригрупповойОборот = Column(Boolean)
    ДатаЗагрузки = Column(DateTime, default=datetime.now)
