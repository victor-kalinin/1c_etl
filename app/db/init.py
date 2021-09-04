import importlib

from app.core.consts import MODELS_DIR_PATH
from app.core.helpers import get_modules_names
from .session import engine
from .base import Base


def create_new_db():
    modules_list = get_modules_names(MODELS_DIR_PATH)
    for models_name in modules_list:
        importlib.import_module(f'app.models.{models_name}')

    Base.metadata.create_all(bind=engine)
