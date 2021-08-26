from typing import Dict
from sqlalchemy import and_

from .rest import Rest


class RestParams(Rest):
    def __init__(self, db, alias_name, month_scope: Dict):
        super().__init__(db, alias_name)
        self.month_scope = month_scope

    def _month_scope_t_(self, func):
        return {key: func(value) for key, value in self.month_scope.items()}

    @property
    def params(self):
        return self._month_scope_t_(lambda x: x.strftime('%d.%m.%Y'))

    def _request_(self, url: str):
        return self.http.get(url, params=self.params, auth=(self.settings.USER, self.settings.PASSWORD))

    def clear_all(self, *args, **kwargs):
        super().clear(*args, **kwargs)

    def clear(self, model_name: str):
        model = getattr(self.module_models, model_name)
        filter_field = getattr(model, model.__filterfield__)
        num_rows_deleted = self.db.query(model).filter(
            and_(filter_field >= self.month_scope.get('from').date(),
                 filter_field <= self.month_scope.get('to'))
        ).delete()
        self.db.commit()
        return num_rows_deleted
