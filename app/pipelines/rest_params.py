from typing import Dict
from sqlalchemy import and_

from .rest import Rest
from app.logging_.decorators import logging_this
from app.core.enums import Operations


class RestParams(Rest):
    def __init__(self, db, alias_name, month_scope: Dict):
        """Класс для работы с данными с возможностью фильтрации по заданному полю

        :param db: Объект сессии SQLAlchemy подключения к БД
        :param alias_name: Название класса таблицы из модели описания
        :param month_scope: Словарь с параметрами периода выборки {'from': datetime, 'to': datetime}
        """
        super().__init__(db, alias_name)
        self.month_scope = month_scope

    def _month_scope_t_(self, func):
        """Преобразование данных :month_scope с помощью заданной функции

        :param func: Функция для преобразования данных :month_scope
        :return: Преобразованный словарь :month_scope
        """
        return {key: func(value) for key, value in self.month_scope.items()}

    def _request_(self, url: str):
        return self.http.get(url, params=self.params, auth=(self.settings.USER, self.settings.PASSWORD))

    @property
    def params(self):
        return self._month_scope_t_(lambda x: x.strftime('%d.%m.%Y'))

    @logging_this(operation=Operations.TASK, task=Operations.CLEAR, summary=True, timing=True)
    def clear(self, model_name: str) -> int:
        """Удаление данных в таблице с использованием поля фильтра в описании модели SQLAlchemy

        :param model_name: Имя класса таблицы из описания модели SQLAlchemy
        :return: Количество удаленных строк
        """
        model = getattr(self.module_models, model_name)
        filter_field = getattr(model, model.__filterfield__)
        num_rows_deleted = self.db.query(model).filter(
            and_(filter_field >= self.month_scope.get('from').date(),
                 filter_field <= self.month_scope.get('to'))
        ).delete()
        self.db.commit()
        return num_rows_deleted
