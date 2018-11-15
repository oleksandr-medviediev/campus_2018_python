import functools
import logging
import inspect

mode_log = True
mode_debug = True


def log_decor(func):

    @functools.wraps(func)
    def log_wrapper(*args, **kwargs):

        if mode_log:

            logging.debug(f'Some "useful" debug log before call to {func.__name__}')

            result = func(*args, **kwargs)

            logging.debug(f'Some other "useful" debug log after call to {func.__name__}')

        else:
            result = func(*args, **kwargs)

        return result

    return log_wrapper


def debug_decor(func):
    
    @functools.wraps(func)
    def debug_wrapper(*args, **kwargs):

        if mode_debug:

            bound_arguments = inspect.signature(func).bind(*args, **kwargs)
            bound_arguments.apply_defaults()

            debug_string = [f'Call to {func.__name__} with arguments:']

            for key, value in bound_arguments.arguments.items():
                debug_string.append(f'{key}::{value}')

            debug_string = ' '.join(debug_string)
            logging.debug(debug_string)

            result = func(*args, **kwargs)

            logging.debug(f'{func.__name__} returned {result}')

        else:
            result = func(*args, **kwargs)

        return result

    return debug_wrapper
