import logging
from functools import wraps
import inspect
import my_config_variables


formatter = logging.Formatter('%(asctime)s - %(message)s')

log_logger = logging.getLogger('log_logger')
log_logger.setLevel(logging.DEBUG)

log_file_handler = logging.FileHandler('LogOutput.txt')
log_file_handler.setLevel(logging.DEBUG)
log_file_handler.setFormatter(formatter)

log_logger.addHandler(log_file_handler)


debug_logger = logging.getLogger('debug_logger')
debug_logger.setLevel(logging.DEBUG)

debug_file_handler = logging.FileHandler('DebugOutput.txt')
debug_file_handler.setLevel(logging.DEBUG)
debug_file_handler.setFormatter(formatter)

debug_logger.addHandler(debug_file_handler)



def my_wrapper(func):
  
    @wraps(func)
    def wrapper(*args, **kwargs):

        if my_config_variables.is_logging_active:
            log_logger.debug(f'Entered {func.__name__}')

        if my_config_variables.is_debug_active:

            debug_logger.debug(f'Entered {func.__name__}')
            args_name = inspect.getargspec(func)[0]

            if len(args_name) == 0:
                debug_logger.debug(f'No arguments')

            else:

                args_dict = {key: value for (key, value) in zip(args_name, args)}
                debug_logger.debug(f'Arguments:')

                for key, value in args_dict.items():
                    debug_logger.debug(f'\t{key} - {value}')
                    

        to_return = func(*args, **kwargs)

        if my_config_variables.is_logging_active:
            log_logger.debug(f'Exited {func.__name__}')

        if my_config_variables.is_debug_active:
            debug_logger.debug(f'Exited {func.__name__}')

        return to_return

    return wrapper
