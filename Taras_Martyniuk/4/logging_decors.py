import logging  
import logging.config
import json
import inspect
import inspect, itertools


DEBUG = True


# they said it on the docs that dict config is cooler than file config, 
# but i still wanted the config to stay in file.
with open('log_config.json') as f:
    config_dict = json.load(f)
    logging.config.dictConfig(config_dict)


DEBUG_FILE_NAME = 'Debug Log File'
DEBUG_FILE_CONSOLE_NAME = 'Debug Log File Console'
OUTPUT_NAME = 'Output Log'

# for tracing debug info, writes to console and file, more heavy on message metadata 
debug_file_logger = logging.getLogger(DEBUG_FILE_NAME)
debug_file_console_logger = logging.getLogger(DEBUG_FILE_CONSOLE_NAME)
# for writing output to user - outputs message to console and file, with no metadata
output_logger = logging.getLogger(OUTPUT_NAME)

debug_file_console_logger.debug('Inited loggers')


def log_decor(func):
    '''
        a decorator that logs info to debug
        logs the name of the function to the file before and after it is executed
        if DEBUG variable is set, also logs to console,
        and adds info about all variables passed to func and their values 

        :returns: a decorator function object
    '''
    def log_wrapper(*args):
        start_str = f'Started \'{func.__name__}\''

        if DEBUG:
            arg_names = list(inspect.signature(func).parameters.keys())
            arg_names_values = dict(zip(arg_names, args))
            start_str += f' with params: {arg_names_values}'

            debug_file_console_logger.debug(start_str)
        else:
            debug_file_logger.debug(start_str)
            
        retval = func(*args)

        end_str = f'\'{func.__name__}\' finished executing'
        if DEBUG:
            end_str += f', yielding result : \'{retval}\''
            debug_file_console_logger.debug(end_str)
        else:
            debug_file_logger.debug(end_str)

        return retval
    
    return log_wrapper
