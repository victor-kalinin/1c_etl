import importlib
import inspect
import requests
import json
from typing import List
from pydantic import parse_obj_as, BaseModel
from sqlalchemy.orm import Session

from app.core import consts
from app.core.helpers import fill_settings


class Rest:
    def __init__(self, db: Session, alias_name: str):
        self.alias_name = alias_name
        self.db = db
        self.module_models = importlib.import_module(consts.MODELS_MODULE_PATH(alias_name))
        self.module_schemas = importlib.import_module(consts.SCHEMAS_MODULE_PATH(alias_name))

    @property
    def settings(self):
        api_module = importlib.import_module(consts.API_CONN_MODULE_PATH(self.alias_name))
        class_name = [m[0] for m in inspect.getmembers(api_module, inspect.isclass)
                      if m[1].__module__ == api_module.__name__][0]
        return fill_settings(getattr(api_module, class_name)())

    def _request_(self, url: str):
        return requests.get(url, auth=(self.settings.USER, self.settings.PASSWORD))

    def extract(self, route: str, schema_name: str):
        url = ''.join((self.settings.API_PATH, route))
        schema = getattr(self.module_schemas, schema_name)
        res = self._request_(url)
        res_dict = json.loads(res.content.decode())
        return parse_obj_as(List[schema], res_dict)

    def transform(self):
        raise NotImplemented

    def clear(self, model_name: str):
        model = getattr(self.module_models, model_name)
        num_rows_deleted = self.db.query(model).delete()
        self.db.commit()
        return num_rows_deleted

    def load(self, model_name: str, item: BaseModel):
        model = getattr(self.module_models, model_name)
        row = model(**item.__dict__)
        self.db.add(row)
        self.db.commit()

    def start(self, table_name=None, clear=True):
        def etl(_table_name, _route_path):
            if clear:  # Очищаем таблицу перез загрузкой данных
                self.clear(_table_name)

            # Получаем данные из 1С, используя данные маршрутов из схемы settings
            rest_data = self.extract(_route_path, _table_name)

            # Загружаем данные таблицу в целевой базе данных
            for item in rest_data:
                self.load(_table_name, item)

        if table_name is not None:
            etl(table_name, self.settings.ROUTES.get(table_name))
        else:
            for table_name, route_path in self.settings.ROUTES.items():
                etl(table_name, route_path)
