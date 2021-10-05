from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.helpers import fill_settings
from app.config.dwh_db import DWHDBSettings


engine = create_engine(str(fill_settings(DWHDBSettings())))
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
