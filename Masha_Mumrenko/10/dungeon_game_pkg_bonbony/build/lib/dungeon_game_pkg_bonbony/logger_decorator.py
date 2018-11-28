import functools
import logging
import logger
import inspect
import datetime


is_debug_mode = False


def time_logger_decorator(func_to_log):
    """
    Extends function's responsibilities by logging time of the function call
    :param: decorating function
    :paramtype: function

    :return: return from func_to_log
    """
    @functools.wraps(func_to_log)
    def time_logger_wrapper(*args,**kwargs):
        
        if is_debug_mode:
            
            logger.logging_object.info(datetime.datetime.now())
            wrapper_result = func_to_log(*args,**kwargs)
            logger.logging_object.info(datetime.datetime.now())
            
        else:
            wrapper_result = func_to_log(*args,**kwargs)

        return wrapper_result

    return time_logger_wrapper
            

def debug_logger_decorator(func_to_log):
    """
    Extends function's responsibilities by debug logging the function
    call in debug mode.
    :param: decorating function
    :paramtype: function

    :return: return from func_to_log
    """
    @functools.wraps(func_to_log)
    def debug_logger_wrapper(*args,**kwargs):

        if is_debug_mode:
            
            arguments_dict = inspect.signature(func_to_log).bind(*args,**kwargs)
            arguments_dict.apply_defaults()

            debug_output = [f'The function {func_to_log.__name__} was called:']

            for k, v in arguments_dict.arguments.items():
                debug_output.append(f'parameter {k} with value {v},')

            debug_output = ' '.join(debug_output)

            logger.logging_object.debug(debug_output)

            wrapper_result = func_to_log(*args, **kwargs)

            logger.logging_object.debug(f'{func_to_log.__name__} returned {wrapper_result}')

        else:
            wrapper_result = func_to_log(*args, **kwargs)

        return wrapper_result

    return debug_logger_wrapper
            
