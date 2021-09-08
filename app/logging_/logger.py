import logging

from app.core.consts import LOG_PATH
from .handlers import BufferingSMTPHandler

_log_format = f'%(asctime)s - [%(levelname)s] - %(message)s'


def get_file_handler():
    """Хэндлер логгера для записи в файл"""
    file_handler = logging.FileHandler(LOG_PATH, encoding='utf-8')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(logging.Formatter(_log_format))
    return file_handler


def get_stream_handler():
    """Хэндлер логгера для записи в консоль"""
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG)
    stream_handler.setFormatter(logging.Formatter(_log_format))
    return stream_handler


def get_smtp_handler():
    """Хэндлер логгера для записи в буфер и отправки по SMTP"""
    smtp_handler = BufferingSMTPHandler(1000)
    smtp_handler.setLevel(logging.DEBUG)
    smtp_handler.setFormatter(logging.Formatter(_log_format))
    return smtp_handler


def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(get_file_handler())
    logger.addHandler(get_stream_handler())
    logger.addHandler(get_smtp_handler())
    return logger
