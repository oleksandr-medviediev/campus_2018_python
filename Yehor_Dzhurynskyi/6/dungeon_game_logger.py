import logging
import functools

DEBUG_MODE = True

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

    def inner(*args, **kwargs):

        result = func(*args, **kwargs)
        arguments = ', '.join(str(arg) for arg in args)

        logger.debug(f'Call: `{func.__name__}({arguments})`, Result: `{result}`')

        return result

    return func if logger.level > logging.DEBUG else inner


def log_decorator(log_message, log_level=logging.DEBUG):

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
