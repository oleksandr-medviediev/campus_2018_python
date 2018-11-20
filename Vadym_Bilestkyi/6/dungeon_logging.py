import logging
import functools

import settings


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_format = logging.Formatter('[%(levelname)s] %(message)s')
console_handler.setFormatter(console_format)

file_handler = logging.FileHandler(filename='log.txt')
file_handler.setLevel(logging.DEBUG)
file_format = logging.Formatter('[%(levelname)s][%(asctime)s] %(message)s')
file_handler.setFormatter(file_format)

logger.addHandler(console_handler)
logger.addHandler(file_handler)


def with_logging(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):

        if settings.DEBUG_ENABLED:
            debug_header_string = '\nFunction \'{}\' was called\nWith args: {}, kwargs: {}'.format(fn.__name__, args, kwargs)
            logger.warning(debug_header_string)
            logger.debug(debug_header_string)

        returned_value = fn(*args, **kwargs)

        if settings.DEBUG_ENABLED:
            debug_trailing_string = '\nFunction {} returned {}'.format(fn.__name__, returned_value)
            logger.warning(debug_trailing_string)
            logger.debug(debug_trailing_string)

        return returned_value

    return wrapper
