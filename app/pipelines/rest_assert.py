import json
from typing import Dict, List

from .rest_params import RestParams
from app.logging_.decorators import logging_this
from app.core.enums import Operations


class RestAssert(RestParams):
    def __init__(self, db, alias_name, month_scope: Dict, sql_query: str):
        """Класс для работы с данными с отправкой предварительной выборки

        :param db: Объект сессии SQLAlchemy подключения к БД
        :param alias_name: Имя класса таблицы из описания модели SQLAlchemy
        :param month_scope: Словарь с параметрами периода выборки {'from': datetime, 'to': datetime}
        :param sql_query: SQL-запрос для выборки предварительных данных
        """
        super().__init__(db, alias_name, month_scope)
        self.sql_query = sql_query
        self._data = None

    def _request_(self, url: str):
        """Получение данных из REST API после отправки данных предварительной выборки методом POST

        :param url: Строка адреса с route api
        :return: Объект Response
        """
        return self.http.post(url, data=self._data, auth=(self.settings.USER, self.settings.PASSWORD))

    @logging_this(operation=Operations.TASK, task=Operations.EXTRACT, summary=True, timing=True)
    def extract(self, route: str, schema_name: str) -> List:
        """Получение данных и формирование общего списка с ними для дальшейшей обработки

        :param route: Строка адреса с route api
        :param schema_name: Название схемы данных в формате Pydantic
        :return: Список с полученными данными
        """
        params_sql = self._month_scope_t_(lambda x: x.date())
        res = self._execute_sql_(self.sql_query, params_sql)
        sql_result = [json.dumps(dict(row)) for row in res if row is not None]
        result = []
        for self._data in sql_result:
            result.extend(super().extract(route, schema_name=schema_name, no_decor=True))
        return result

    def start(self, table_class=None, clear=None):
        if table_class is None:
            raise NotImplementedError('Функционал пакетной обработки не может быть реализован. '
                                      'Необходимо явное указание table_name')
        super().start(table_class=table_class, clear=clear)
