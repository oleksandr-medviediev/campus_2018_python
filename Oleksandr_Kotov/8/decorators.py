"""module provides decorators for the game
"""
from functools import wraps

import game_logger


def info_decorator(func):
    """decorate a function into info wrapper

    Arguments:
        func callable -- function to wrap

    Returns:
        callable -- wrapped function
    """
    @wraps(func)
    def wrapper(*args, **kwargs):

        return func(*args, **kwargs)

    return wrapper


def debug_decorator(func):
    """decorates a function into debug wrapper
    debug wrapper prints function name and arguments before call

    Arguments:
        func callable -- function to wrap

    Returns:
        callable -- wrapped function
    """
    @wraps(func)
    def wrapper(*args, **kwargs):

        from main_loop import debug_mode

        if debug_mode:

            game_logger.logging.debug("Function name: " + func.__name__)

            game_logger.logging.debug("Args: ")
            game_logger.logging.debug(args)

            game_logger.logging.debug("Kwargs: ")
            game_logger.logging.debug(kwargs)

        return func(*args, **kwargs)

    return wrapper
