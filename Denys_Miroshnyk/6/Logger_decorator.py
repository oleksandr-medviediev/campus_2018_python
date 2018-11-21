from Custom_logger import logger as log
import inspect
import functools

debug_mode = False


def debug_log_decorator(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if debug_mode:

            if len(args) > 0:
                debug_out = "Arguments:"
                arg_names = inspect.signature(func).parameters
                arg_name_value = {k: v for (k, v) in zip(arg_names, args)}

                for name, value in arg_name_value.items():
                    debug_out = debug_out + '\n' + f"{name}: {value}"

                log.debug(debug_out)

            result = func(*args, **kwargs)
            log.debug(f"{func.__name__} returns {result}")

        else:
            result = func(*args, **kwargs)

        return result
    return wrapper
