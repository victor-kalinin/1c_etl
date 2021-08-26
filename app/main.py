from os import environ
from os.path import join
import argparse

from app.core.consts import CONFIG_OS_PATH, CONFIG_FILE, CREDENTIALS_KEY, FILENAME_KEY


PARSER = argparse.ArgumentParser()
PARSER.add_argument('-e', '--env', choices=['PROD', 'DEV'], required=True,
                    help='Рабочее окружение')
PARSER.add_argument('-t', '--table_name', action='store', type=str, default=None,
                    help='Название таблицы для единичной выгрузки')
PARSER.add_argument('-m', '--months', action='store', type=int, default=2,
                    help='Количество месяцев для выгрузки периода')
PARSER.add_argument('-d', '--direction', choices=['FORWARD', 'BACKWARD'], default='BACKWARD',
                    help='Направление формирования периода выгрузки')


def main(parsed_args):
    # if --no_current_table:
    #   if --no_months:
    #       - update all static tables
    #   elif [months {default: 2}] and [direction {default: -1}]:
    #       - update all static tables
    #       - update all periodic tables
    #       - update all accums
    #       - update work_bonus
    # elif --has_table:
    #   - all the same above, but using table name

    config_dir = CONFIG_OS_PATH
    if parsed_args.env == 'PROD' and environ.get(CREDENTIALS_KEY) is not None:
        config_dir = environ.get(CREDENTIALS_KEY)
    environ[FILENAME_KEY] = join(config_dir, CONFIG_FILE)
