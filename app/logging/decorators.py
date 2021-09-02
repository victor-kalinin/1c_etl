from time import time
from functools import wraps

from app.logging.logger import get_logger


def logging_this(func):
    logger = get_logger('ETL')

    @wraps(func)
    def inner_func(*args, **kwargs):
        start_time = time()
        try:
            res = func(*args, **kwargs)
            work_time = time() - start_time
            message = f'{args[0].get("operation").value} :: {args[0].get("table_name")} :: ' \
                      f'Количество записей: {args[0].get("count_rows")} :: ' \
                      f'Затрачено времени: {work_time} сек.'
            logger.info(message)
            return res
        except ValueError as e:
            logger.warning(e)
        except Exception as e:
            logger.error(e)
    return inner_func
