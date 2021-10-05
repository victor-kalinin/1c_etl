import json
import ast
from typing import Dict
from sqlalchemy.orm import Session
from os.path import basename, isfile, join
from os import environ
from datetime import datetime
from dateutil.relativedelta import relativedelta
import configparser
from glob import glob

from app.core.enums import Direction
from app.core.consts import MODELS_OS_PATH, FILENAME_KEY


def fill_settings(settings_obj):
    config = configparser.ConfigParser()
    config.read(environ[FILENAME_KEY])
    attrs = [attr for attr in dir(settings_obj) if not attr.startswith('_')]
    try:
        for attr in attrs:
            value = config[settings_obj.CONFIG_KEY].get(attr)
            if value is not None:
                setattr(settings_obj, attr, value)
    except configparser.Error:
        raise configparser.ParsingError

    return settings_obj


def execute_sql(db: Session, sql: str, values: Dict = None):
    if values is None:
        values = {}
    return db.execute(sql, values).fetchall()


def sql_to_json(db: Session, sql: str, values: Dict = None):
    res = execute_sql(db, sql, values)
    return [json.dumps(dict(row)) for row in res]


def month_scope(months: int, direction: Direction) -> Dict:
    today = datetime.today()
    delta_months = today + relativedelta(months=months) * direction.value
    return {'from': min(today, delta_months),
            'to': max(today, delta_months)}


def get_modules_names(path: str):
    modules = glob(join(path, "*.py"))
    return {basename(f)[:-3]: join(path, basename(f)) for f in modules
            if isfile(f) and not f.endswith('__init__.py')}


def get_alias_group(alias_name):
    splitted_name = alias_name.rsplit('_', -1)
    return splitted_name[-1] if len(splitted_name) > 1 else 'static'


def get_tables_dict():
    table_dict = {}
    for module_name, module_path in get_modules_names(MODELS_OS_PATH).items():
        with open(module_path, encoding='utf-8') as f:
            tree = ast.parse(f.read())

        for node in tree.body:
            if isinstance(node, ast.ClassDef):
                for node_body in node.body:
                    if isinstance(node_body, ast.Assign) and len(node_body.targets) == 1:
                        target = node_body.targets[0]
                        if isinstance(target, ast.Name) and target.id == '__tablename__':
                            table_dict[ast.literal_eval(node_body.value)] = {'alias': module_name.split('_', 1)[1],
                                                                             'table_name': node.name}
    return table_dict


def get_alias_from_tablename(tablename):
    return get_tables_dict().get(tablename, None)