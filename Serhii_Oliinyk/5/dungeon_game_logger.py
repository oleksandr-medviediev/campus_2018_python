import logging
import functools


DEBUGMODE = False

logger = logging.getLogger(__name__)
level_type = logging.INFO

logger.setLevel(logging.INFO)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_format = logging.Formatter('[%(levelname)s] %(message)s')
console_handler.setFormatter(console_format)

file_handler = logging.FileHandler(filename='example.log')
file_handler.setLevel(logging.DEBUG)
file_format = logging.Formatter('[%(levelname)s][%(asctime)s] %(message)s')
file_handler.setFormatter(file_format)

logger.addHandler(console_handler)
logger.addHandler(file_handler)


def info_decorator(func):
    """
    Decorator for function, create inner function.

    :param func: function.

    :return: inner function
    :rtype: func return type

    """
    def inner(*args, **kwargs):
        """
        Wrapper for func, call the func.

        :param *args: list of arguments.
        :param **kwargs: map of arguments.

        :return: func
        :rtype: func return type

        """
        return func(*args, **kwargs)
    
    return inner


def debug_decorator(func):
    """
    Decorator for function, create inner function.

    :param func: function.

    :return: inner function
    :rtype: func return type

    """
    def inner(*args, **kwargs):
        """
        Log the info about call function and its arguments, call the func.

        :param *args: list of arguments.
        :param **kwargs: map of arguments.

        :return: func
        :rtype: func return type

        """
        if DEBUGMODE:
            args_list = [str(i) for i in args]
            kwarg_list = [str(k) + ":" + str(v) for k, v in kwargs]

            debug_string = func.__name__ + " \nargs:" + ', '.join(args_list) + "; \nkwargs:" + ', '.join(kwarg_list)
            log_data(debug_string)
        
        return func(*args, **kwargs)
    
    return inner


@info_decorator
def log_data(info_data):
    """
    Log info_data. Send as parameter to decorator info_decorator

    :param info_data: info fo logger.
    :type info_data: str.

    :return: None
    """
    logger.info(info_data)
