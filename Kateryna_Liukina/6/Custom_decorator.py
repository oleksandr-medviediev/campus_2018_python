import functools
import logging

def print_in_out_decorator(logger, func):
    """
    Decorator that returns wrapper that prints info in logger before and after start of the func
    Args:
        logger(logging.Logger): logger where logs will be printed
        func(function): function that will be decorated
    Returns:
         wrapper that prints info in logger before and after start of the func
    """
    @functools.wraps(func)
    def print_in_out_wrapper(*args, **kwargs):
        """Prints info before and after start of the function"""
        list_of_args = [str(arg) for arg in args]
        list_of_kwargs = [str(name) + ':' + str(arg) for name, arg in kwargs]

        debug_string = "Start of " + func.__name__ + " function with args: "\
                       + ','.join(list_of_args) + "; and kwargs: " + ','.join(list_of_kwargs)

        logger.log(logging.DEBUG, debug_string)

        result = func(*args, **kwargs)

        logger.log(logging.DEBUG, "End of " + func.__name__ + " function.")
        return result
    return print_in_out_wrapper
