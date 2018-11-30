import functools
import json
import logging


DEBUG_MODE = False
logger = logging.getLogger(__name__)

log_level = logging.DEBUG if DEBUG_MODE else logging.INFO

logger.setLevel(log_level)

stdout_handler = logging.StreamHandler()
stdout_handler.setLevel(log_level)
stdout_formatter = logging.Formatter('[%(levelname)s] %(message)s')
stdout_handler.setFormatter(stdout_formatter)

file_handler = logging.FileHandler('dungeon_game.log')
file_handler.setLevel(logging.DEBUG)
file_formatter = logging.Formatter('[%(levelname)s][%(asctime)s] %(message)s')
file_handler.setFormatter(file_formatter)

logger.addHandler(stdout_handler)
logger.addHandler(file_handler)


def debug_decorator(func):
    """
    decorator which adds call debug info if `DEBUG_MODE` is `True`
        :param function func: desired callback
        :return: callback with optional wrapper
        :rtype: function
    """

    def inner(*args, **kwargs):

        result = func(*args, **kwargs)
        arguments = ', '.join(str(arg) for arg in args)

        logger.debug(f'Call: `{func.__name__}({arguments})`, Result: `{result}`')

        return result

    return inner if DEBUG_MODE else func


def log_decorator(log_message, log_level=logging.DEBUG):
    """
    decorator which adds logging message with desired logging level
        :param str func: desired callback
        :param int log_level: logging level
        :return: callback with wrapper
        :rtype: function
    """

    HANDLERS = {
        logging.DEBUG: logger.debug,
        logging.INFO: logger.info,
        logging.WARN: logger.warn,
        logging.ERROR: logger.error,
        logging.CRITICAL: logger.critical
    }

    def actual_decorator(func):

        @functools.wraps(func)
        def inner(*args, **kwargs):

            log = HANDLERS[log_level]
            log(log_message)
            result = func(*args, **kwargs)

            return result

        return inner

    return actual_decorator
