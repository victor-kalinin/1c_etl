from sqlalchemy import Column, Text, Integer, Boolean, DateTime, Float
from datetime import datetime

from app.db.base import Base


class MDAccum(Base):
    __tablename__ = 'rs1c_md_accum'
    __table_args__ = {'schema': 'rsrc'}
    __filterfield__ = 'Период'

    Период = Column(DateTime)
    Сценарий = Column(Text, primary_key=True)
    ЦФО = Column(Text, primary_key=True)
    ЦФОКод = Column(Text)
    ЦФОНаименование = Column(Text)
    СтатьяОборотов = Column(Text, primary_key=True)
    НоменклатурнаяГруппа = Column(Text, primary_key=True)
    ПодразделениеОрганизации = Column(Text, primary_key=True)
    СчетчикПодрОрг = Column(Integer)
    Количество = Column(Integer)
    Сумма = Column(Float)
    ЭтоПлан = Column(Boolean)
    ЭтоВнутригрупповойОборот = Column(Boolean)
    Продукция = Column(Text, primary_key=True)
    ДатаЗагрузки = Column(DateTime, default=datetime.now)
