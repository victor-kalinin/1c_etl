import importlib
import inspect
import requests
import json
from typing import List
from pydantic import parse_obj_as, BaseModel
from sqlalchemy.orm import Session
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

from app.core import consts
from app.core.helpers import fill_settings
from app.core.enums import ORMOperations


class Rest:
    def __init__(self, db: Session, alias_name: str):
        self.alias_name = alias_name
        self.db = db
        self.http = self._set_request_session_()
        self.module_models = importlib.import_module(consts.MODELS_MODULE_PATH(alias_name))
        self.module_schemas = importlib.import_module(consts.SCHEMAS_MODULE_PATH(alias_name))

    @staticmethod
    def _set_request_session_():
        retry_strategy = Retry(total=consts.API_RETRY_COUNT,
                               status_forcelist=[429, 500, 502, 503, 504],
                               method_whitelist=["HEAD", "GET", "OPTIONS"])
        adapter = HTTPAdapter(max_retries=retry_strategy)
        http = requests.Session()
        http.mount("https://", adapter)
        http.mount("http://", adapter)
        return http

    @property
    def settings(self):
        api_module = importlib.import_module(consts.API_CONN_MODULE_PATH(self.alias_name))
        class_name = [m[0] for m in inspect.getmembers(api_module, inspect.isclass)
                      if m[1].__module__ == api_module.__name__][0]
        return fill_settings(getattr(api_module, class_name)())

    def _url_(self, _route_path: str):
        return ''.join((self.settings.API_PATH, _route_path))

    def _request_(self, url: str):
        return self.http.get(url, auth=(self.settings.USER, self.settings.PASSWORD))

    def extract(self, url: str, schema_name: str):
        schema = getattr(self.module_schemas, schema_name)
        res = self._request_(url)
        res_dict = json.loads(res.content.decode())
        return parse_obj_as(List[schema], res_dict)

    def transform(self):
        raise NotImplemented

    def clear_all(self, model_name: str):
        model = getattr(self.module_models, model_name)
        num_rows_deleted = self.db.query(model).delete()
        self.db.commit()
        return num_rows_deleted

    def clear(self, model_name: str):
        self.clear_all(model_name)

    def load(self, model_name: str, item: BaseModel):
        model = getattr(self.module_models, model_name)
        row = model(**item.__dict__)
        self.db.add(row)
        self.db.commit()

    def start(self, table_class=None, clear=False):
        def etl(_table_class, _route_path):
            if clear:
                count_deleted_rows = self.clear_all(model_name=_table_class)
                return {'operation': ORMOperations.CLEAR,
                        'count_rows': count_deleted_rows}

            url = self._url_(_route_path)
            rest_data = self.extract(url, _table_class)
            row_count = len(rest_data)

            if rest_data is None:
                raise TypeError(f'Данные не были получены из REST API. url: {url}')

            if row_count > 0:
                self.clear(_table_class)

                for item in rest_data:
                    self.load(_table_class, item)
                return {'operation': ORMOperations.LOAD,
                        'count_rows': row_count}
            else:
                raise ValueError(f'Были получен пустой ответ. url: {url}')

        if table_class is not None:
            return etl(table_class, self.settings.ROUTES.get(table_class))
        else:
            result = []
            for table_class, route_path in self.settings.ROUTES.items():
                result = result.append(etl(table_class, route_path))
            return result
