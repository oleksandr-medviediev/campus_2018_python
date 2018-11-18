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
    :param func: Function to decorate with call logger
    :return: Wrapper function
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):

        return_value = None

        log_level = 0

        if config.IS_DEBUG:
            log_level = 20
        else:
            log_level = 10

        logger.log(log_level, f"Calling {func.__name__}")
        return_value = func(*args, **kwargs)
        logger.log(log_level, f"Function {func.__name__} executed successfully")

        return return_value

    return wrapper


def debug_log_decorator(func):
    """
    Debug decorator for function call logger
    :param func: Function to decorate with debug call logger
    :return: Wrapper function
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):

        return_value = None
        log_level = 0

        if config.IS_DEBUG:
            log_level = 20
        else:
            log_level = 10

        bound = inspect.signature(func).bind(*args, **kwargs)
        log_string_arg_list = ["Arguments passed:"]
        for key, value in bound.arguments.items():
            log_string_arg_list.append(f"{key} : {value}")

        logger.log(log_level, ' '.join(log_string_arg_list))

        return_value = func(*args, **kwargs)

        logger.log(log_level, f"Function {func.__name__} returned {return_value}")

        return return_value

    return wrapper
