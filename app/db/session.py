from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import json

from app.core.helpers import fill_settings
from app.config.dwh_db import DWHDBSettings


def dumps(d):
    """Используется для корректной сериализации PG JSON"""
    return json.dumps(d, ensure_ascii=False)


engine = create_engine(str(fill_settings(DWHDBSettings())), json_serializer=dumps)
session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Generator:
    db = session_local()
    try:
        yield db
    finally:
        db.close()
