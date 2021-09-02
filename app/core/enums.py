from enum import Enum


class Direction(Enum):
    FORWARD = 1
    BACKWARD = -1


class ORMOperations(Enum):
    CLEAR = 'УДАЛЕНИЕ'
    LOAD = 'ДОБАВЛЕНИЕ'
