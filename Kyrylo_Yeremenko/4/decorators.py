"""
This module lists decorators for task 6.1 from Coding Campus 2018 Python course
(Dungeon Game)
"""

import logging
import log
import config
import inspect
import functools


logger = logging.getLogger(log.LOGGER_NAME)


def log_decorator(func):
    """
    Decorator for function call logger
    :param func:
    :return:
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):

        return_value = None

        if config.IS_DEBUG:

            logger.info(f"Calling {func.__name__}")
            bound = inspect.signature(func).bind(*args, **kwargs)

            log_string_arg_list = ["Arguments passed:"]
            for key, value in bound.arguments.items():
                log_string_arg_list.append(f"{key} : {value}")

            logger.info(' '.join(log_string_arg_list))

            return_value = func(*args, **kwargs)
            logger.info(f"Function {func.__name__} returned {return_value}")

        else:

            logger.debug(f"Calling {func.__name__}")
            return_value = func(*args, **kwargs)
            logger.debug(f"Function {func.__name__} returned {return_value}")

        return return_value

    return wrapper


