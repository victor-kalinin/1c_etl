from typing import Dict
import requests

from .rest_params import RestParams
from app.core.helpers import sql_to_json


class RestAssert(RestParams):
    def __init__(self, db, alias_name, month_scope: Dict, sql_query: str):
        super().__init__(db, alias_name, month_scope)
        self.sql_query = sql_query
        self._data = None

    def _request_(self, url: str):
        return requests.post(url, data=self._data, auth=(self.settings.USER, self.settings.PASSWORD))

    def extract(self, route: str, schema_name: str):
        params_sql = self._month_scope_t_(lambda x: x.date())
        sql_result = sql_to_json(self.db, self.sql_query, params_sql)
        result = []
        for self._data in sql_result:
            result.extend(super().extract(route=route, schema_name=schema_name))
        return result

    def start(self, table_name=None, clear=True):
        if table_name is None:
            raise NotImplementedError('Функционал пакетной обработки не может быть реализован. '
                                      'Необходимо явное указание table_name')
        super().start(clear=clear, table_name=table_name)