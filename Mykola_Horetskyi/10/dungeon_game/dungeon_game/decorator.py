import functools
import inspect
import threading
from game_logger import logger
import config


def debug_decorator(func):
    """
    Logs input and output of functions.
    """
    @functools.wraps(func)
    def debug_wrapper(*args, **kwargs):
        if config.function_debug:
            bound_arguments = inspect.signature(func).bind(*args, **kwargs)
            bound_arguments.apply_defaults()

            debug_string = ["Calling {} with arguments:".format(func.__name__)]

            for key, value in bound_arguments.arguments.items():
                debug_string.append("{} = {}".format(key, value))

            debug_string = "\n".join(debug_string)
            logger.debug(debug_string)

            result = func(*args, **kwargs)

            logger.debug("{} returns {}".format(func.__name__, result))

        else:
            result = func(*args, **kwargs)

        return result

    return debug_wrapper


def thread_lock_decorator(func):
    """
    Locks execution of a function.
    """
    @functools.wraps(func)
    def thread_lock_wrapper(*args, **kwargs):

        lock = threading.Lock()
        lock.acquire()

        try:
            result = func(*args, **kwargs)
        finally:
            lock.release()

        return result

    return thread_lock_wrapper
