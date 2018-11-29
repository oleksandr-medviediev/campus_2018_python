from functools import wraps

from .logging_system import logger

DEBUG_MODE = True

class DebugDecorator:

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if DEBUG_MODE:
                params = ', '.join(map(str, args))
                logger.debug(func.__name__ + " was called with params {params}".format(params=params))

            result = func(*args, **kwargs)

            if DEBUG_MODE:
                logger.debug(func.__name__ + " was successfully finished. Return: {}".format(result))

            return result

        return wrapper


class InfoDecorator:
    def __init__(self, message):
        self.message = message


    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            logger.info(self.message)
            return result

        return wrapper

