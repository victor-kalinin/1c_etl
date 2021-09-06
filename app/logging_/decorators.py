from time import time
from functools import wraps

from app.logging_.logger import get_logger
from app.core.enums import Operations


logger = get_logger('')


def try_except_wrap(func):
    @wraps(func)
    def inner_func(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            logger.warning(e)
        except Exception as e:
            logger.error(e)
    return inner_func


def logging_this(operation: Operations = None, task: Operations = None, summary=False, timing=False):
    def inner_func(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if kwargs.get('no_decor') is True:
                return func(*args, **kwargs)

            header_message = ['Начало', ]
            footer_message = ['Завершение', ]

            if operation is not None:
                header_message.append(operation.value)
                footer_message.append(operation.value)

            if operation is operation.MAIN:
                header_message.append(f'Используется окружение [{args[0].env}].')
                header_message.append(f'Выбран режим обработки')
                if args[0].table_name is not None:
                    mode_message = 'одной таблицы.'
                else:
                    mode_message = f'массива таблиц {args[0].groups}.'
                header_message.append(mode_message)

            if kwargs.get('msg') is not None:
                header_message.append(kwargs.get('msg'))
                footer_message.append(kwargs.get('msg'))

            if task is not None:
                header_message.append(f'"{task.value}".')
                footer_message.append(f'"{task.value}".')
                if task is Operations.SQL:
                    header_message.append(f'<{args[1][:42]}{" ..." if len(args[1]) > 42 else ""}>')

            logger.info(' '.join(header_message))
            start_time = time()
            res = func(*args, **kwargs)
            work_time = time() - start_time

            if summary and isinstance(res, int) and operation is not Operations.MAIN:
                footer_message.extend(['Количество строк:', f'{res}.'])
            if timing:
                footer_message.extend(['Затрачено времени:', str(round(work_time, 4)), 'сек.'])

            logger.info(' '.join(footer_message))
            return res
        return wrapper
    return inner_func
