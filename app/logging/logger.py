import logging
from os import environ
from os.path import join

from app.core.consts import LOG_FILE, LOGFILE_KEY


_log_format = f'%(asctime)s - [%(levelname)s] - %(name)s - %(message)s'


def get_file_handler():
    file_handler = logging.FileHandler(join(environ[LOGFILE_KEY]))
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(logging.Formatter(_log_format))
    return file_handler


def get_stream_handler():
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG)
    stream_handler.setFormatter(logging.Formatter(_log_format))
    return stream_handler


def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(get_file_handler())
    logger.addHandler(get_stream_handler())
    return logger
