from enum import Enum


class Direction(Enum):
    FORWARD = 1
    BACKWARD = -1


class Operations(Enum):
    MAIN = 'работы приложения.'
    TABLE = 'работы с таблицей'
    TASK = 'операции'
    CLEAR = 'Очистка таблицы'
    EXTRACT = 'Получение данных'
    LOAD = 'Добавление данных'
    SQL = 'Выполнение SQL-запроса'
