import argparse
from typing import Dict

from app.core.helpers import get_tables_dict, month_scope, get_alias_from_tablename, get_alias_group
from app.core.sql import work_bonus
from app.core.enums import Direction, Operations
from app.pipelines import rest, rest_params, rest_assert
from app.logging_.decorators import logging_this, try_except_wrap


PARSER = argparse.ArgumentParser()
PARSER.add_argument('-e', '--env', choices=['PROD', 'DEV', 'STAGE'], required=True,
                    help='Рабочее окружение')
PARSER.add_argument('-g', '--groups', choices=['static', 'params', 'accums', 'assert'],
                    type=str, nargs='+', default=['static', 'params', 'assert'],
                    help='Список групп таблиц для пакетной выгрузки данных')
PARSER.add_argument('-t', '--table_name', action='store', type=str, default=None,
                    help='Название таблицы для единичной выгрузки')
PARSER.add_argument('-ca', '--clear_all', action='store_true',
                    help='Режим полной очистки таблиц без загрузки данных')
PARSER.add_argument('-m', '--months', action='store', type=int, default=2,
                    help='Количество месяцев для выгрузки периода')
PARSER.add_argument('-d', '--direction', choices=['FORWARD', 'BACKWARD'], default='BACKWARD',
                    help='Направление формирования периода выгрузки')


@logging_this(operation=Operations.MAIN)
def main(parsed_args) -> None:
    """Основная рабочая процедура

    :param parsed_args: Аргументы, полученные с помощью :argparse
    """
    from app.db.session import get_db

    @try_except_wrap
    @logging_this(operation=Operations.TABLE, summary=True, timing=True)
    def start_pipeline(params: Dict, **kwargs) -> None:
        """Основной ETL pipeline для работы с данными

        :param params: Словарь в формате одной записи :get_tables_dict()
        :param kwargs: Дополнительные параметры для логгера
        """
        pipeline = None
        _db = next(get_db())
        _month_scope = month_scope(parsed_args.months, Direction.__getattr__(parsed_args.direction))

        # Выбираем тип класса из значения параметра :group
        if params['group'] == 'static':
            pipeline = rest.Rest(db=_db, alias_name=params['alias'])
        elif params['group'] in ('params', 'accums'):
            pipeline = rest_params.RestParams(db=_db, alias_name=params['alias'], month_scope=_month_scope)
        elif params['group'] == 'assert':
            pipeline = rest_assert.RestAssert(db=_db, alias_name=params['alias'], month_scope=_month_scope,
                                              sql_query=work_bonus)

        # Если :group был выбран корректно из заранее заданных, то запускаем обработку методом .start
        if pipeline is not None:
            pipeline.start(table_class=params['table_class'], clear=parsed_args.clear_all)

    # Проверяем на наличие в аргументах значения ключа :table_name - имеет высший приоритет на выполнение
    # Параметр :msg нужен для логгера - передаем в нем имя физической таблицы
    if parsed_args.table_name is not None:
        table_params = get_alias_from_tablename(parsed_args.table_name)
        start_pipeline(table_params, msg=f'{parsed_args.table_name}.')
    else:
        for table_name, table_params in get_tables_dict().items():
            if get_alias_group(table_params.get('alias')) in parsed_args.groups:
                start_pipeline(table_params, msg=f'{table_name}.')
