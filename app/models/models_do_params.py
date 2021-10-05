from sqlalchemy import Column, Text, Boolean, DateTime

from app.db.base import Base


class DoTasksTracking(Base):
    __tablename__ = 'rs1c_do_tasks_tracking'
    __table_args__ = {'schema': 'rsrc'}
    __filterfield__ = 'ДатаВыполнения'
    
    Задача = Column(Text, primary_key=True)
    ЗадачаЗУП = Column(Text)
    ТипЗадачи = Column(Text)
    Исполнитель = Column(Text)
    ДатаВыполнения = Column(DateTime)
    Выполнена = Column(Boolean)
    СтатусПроцесса = Column(Text)
