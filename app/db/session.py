from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import json

from app.core.helpers import fill_settings
from app.config.dwh_db import DWHDBSettings


def dumps(d):
    return json.dumps(d, ensure_ascii=False)


def get_db() -> Generator:
    engine = create_engine(str(fill_settings(DWHDBSettings())), json_serializer=dumps)
    session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = session_local()
    try:
        yield db
    finally:
        db.close()
