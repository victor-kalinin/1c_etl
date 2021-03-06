import ast
from typing import Dict
from os.path import basename, isfile, join
from datetime import datetime
from dateutil.relativedelta import relativedelta
import configparser
from glob import glob

from app.core.enums import Direction
from app.core.consts import MODELS_DIR_PATH, CREDENTIALS_PATH


def fill_settings(settings_obj):
    """Заполнение объекта с настроками значениями credentials из файла *.ini

    :param settings_obj: object :APISettings or :DBSettings
    :return: Исходный объект с заполненными атрибутами
    """
    config = configparser.ConfigParser()
    config.read(CREDENTIALS_PATH)

    # Формируем список основных атрибутов. Исключаем дандеры (_ и __)
    attrs = [attr for attr in dir(settings_obj) if not attr.startswith('_')]

    # Находим в файле .ini ключ с таким же именем как и атрибут объекта, заполняем значениями.
    # Если исходное значение в объекте непустое - пропускаем
    try:
        for attr in attrs:
            value = config[settings_obj.CONFIG_KEY].get(attr)
            if value is not None:
                setattr(settings_obj, attr, value)
    except configparser.Error:
        raise configparser.ParsingError

    return settings_obj


def month_scope(months: int, direction: Direction) -> Dict:
    """Формирование словаря с диапазоном периода для выгрузки

    :param months: Количество месяцев в диапазоне
    :param direction: Направление формирования периода
    :return: Словарь {'from': datetime, 'to': datetime}
    """
    today = datetime.today()
    delta_months = today + relativedelta(months=months) * direction.value
    return {'from': min(today, delta_months),
            'to': max(today, delta_months)}


def get_modules_names(path: str) -> Dict:
    """Формирование словаря с названиями модулей без *.py

    :param path: Путь к каталогу с файлами
    :return: Словарь {'name_of_file': 'path_to_file/name_of_file'}
    """
    modules = glob(join(path, "*.py"))
    return {basename(f)[:-3]: join(path, basename(f)) for f in modules
            if isfile(f) and not f.endswith('__init__.py')}


def get_alias_group(alias_name: str) -> str:
    """Получение названия группы модулей

    :param alias_name: Полное название файла без расширения
    :return: Название группы

    Notes
    -----
    Берется крайнее правое значение после разбивки .split по '_'
    Если значения нет, то возвращается 'static'

    Examples
    --------
    models_do_params  ->  params

    models_do         ->  static
    """
    splitted_name = alias_name.rsplit('_', -1)
    return splitted_name[-1] if len(splitted_name) > 1 else 'static'


def get_tables_dict() -> Dict:
    """Получение словаря с перечислением имен физических таблиц и их параметров

    :return: Словарь {'name_of_table_in_db':
                                        {'alias': 'alias_name',
                                         'table_class': 'name_of_class_in_models',
                                         'group': 'alias_group'}
                    ... }

    Examples
    --------
    {'rs1c_cons_catalog_cfo': {'alias': 'cons',
                               'table_class': 'CatalogCfo',
                               'group': 'static'}
     ... }
    """
    table_dict = {}
    for module_name, module_path in get_modules_names(MODELS_DIR_PATH).items():
        with open(module_path, encoding='utf-8') as f:
            tree = ast.parse(f.read())

        for node in tree.body:
            if isinstance(node, ast.ClassDef):
                for node_body in node.body:
                    if isinstance(node_body, ast.Assign) and len(node_body.targets) == 1:
                        target = node_body.targets[0]
                        if isinstance(target, ast.Name) and target.id == '__tablename__':
                            alias = module_name.split('_', 1)[1]
                            table_dict[ast.literal_eval(node_body.value)] = {'alias': alias,
                                                                             'table_class': node.name,
                                                                             'group': get_alias_group(alias)}
    return table_dict


def get_alias_from_tablename(tablename: str) -> Dict:
    """Получение словаря с параметрами для одной таблицы

    :param tablename: Имя физической таблицы в БД
    :return: Словарь вида :get_tables_dict()
    """
    return get_tables_dict().get(tablename, None)
