from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.dialects.postgresql import UUID

from app.db.base import Base


class BonusWorkTime(Base):
    __tablename__ = 'rs1c_zup_bonus_work_time'
    __table_args__ = {'schema': 'rsrc'}
    __filterfield__ = 'Период'

    Период = Column(DateTime)
    Сотрудник = Column(UUID, primary_key=True)
    НормаДней = Column(Integer)
    ДнейОтпуска = Column(Integer)
    ДнейВДекрете = Column(Integer)
    ДнейБольничного = Column(Integer)
