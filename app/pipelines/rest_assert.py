from typing import Dict

from .rest_params import RestParams
from app.core.helpers import sql_to_json


class RestAssert(RestParams):
    def __init__(self, db, alias_name, month_scope: Dict, sql_query: str):
        super().__init__(db, alias_name, month_scope)
        self.sql_query = sql_query
        self._data = None

    def _request_(self, url: str):
        return self.http.post(url, data=self._data, auth=(self.settings.USER, self.settings.PASSWORD))

    def extract(self, route: str, schema_name: str):
        params_sql = self._month_scope_t_(lambda x: x.date())
        sql_result = sql_to_json(self.db, self.sql_query, params_sql)
        result = []
        for self._data in sql_result:
            result.extend(super().extract(self._url_(route), schema_name=schema_name))
        return result

    def start(self, table_class=None, clear=None):
        if table_class is None:
            raise NotImplementedError('Функционал пакетной обработки не может быть реализован. '
                                      'Необходимо явное указание table_name')
        return super().start(table_class=table_class, clear=clear)
