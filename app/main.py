import argparse
from typing import Dict
from os import environ
from os.path import join


from app.core import consts
from app.core.helpers import get_tables_dict, month_scope, get_alias_from_tablename, get_alias_group
from app.db.session import get_db
from app.core.sql import work_bonus
from app.core.enums import Direction
from app.pipelines import rest, rest_params, rest_assert
from app.logging.logger import get_logger
from app.logging.decorators import logging_this


PARSER = argparse.ArgumentParser()
PARSER.add_argument('-e', '--env', choices=['PROD', 'DEV'], required=True,
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
PARSER.add_argument('-l', '--log_path', action='store', type=str, default=consts.LOGS_OS_PATH,
                    help='Каталог для выгрузки лог-файла')


def main(parsed_args):
    @logging_this
    def start_pipeline(params: Dict):
        pipeline = None
        _db = next(get_db())
        _month_scope = month_scope(parsed_args.months, Direction.__getattr__(parsed_args.direction))

        if params['group'] == 'static':
            pipeline = rest.Rest(db=_db, alias_name=params['alias'])
        elif params['group'] in ('params', 'accums'):
            pipeline = rest_params.RestParams(db=_db, alias_name=params['alias'], month_scope=_month_scope)
        elif params['group'] == 'assert':
            pipeline = rest_assert.RestAssert(db=_db, alias_name=params['alias'], month_scope=_month_scope,
                                              sql_query=work_bonus)
        if pipeline is not None:
            res = pipeline.start(table_class=params['table_class'], clear=parsed_args.clear_all)
            params.update(res)
            return params

    config_dir = consts.CONFIG_OS_PATH
    logger_root = get_logger('ROOT')
    logger_root.info('НАЧАЛО РАБОТЫ')

    if parsed_args.env == 'PROD' and environ.get(consts.CREDENTIALS_KEY) is not None:
        config_dir = environ.get(consts.CREDENTIALS_KEY)

    environ[consts.FILENAME_KEY] = join(config_dir, consts.CONFIG_FILE)
    environ[consts.LOGFILE_KEY] = join(parsed_args.log_path, consts.LOG_FILE)

    if parsed_args.table_name is not None:
        table_params = get_alias_from_tablename(parsed_args.table_name)
        table_params['table_name'] = parsed_args.table_name
        start_pipeline(table_params)
    else:
        for table_name, table_params in get_tables_dict().items():
            if get_alias_group(table_params.get('alias')) in parsed_args.groups:
                table_params['table_name'] = table_name
                start_pipeline(table_params)

    logger_root.info('КОНЕЦ РАБОТЫ')
