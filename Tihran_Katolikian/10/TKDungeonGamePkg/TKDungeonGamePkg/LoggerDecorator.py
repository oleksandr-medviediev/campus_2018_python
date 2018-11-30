from functools import wraps
import DungeonGameConfig
import logging
import inspect


def logger_decorator(func):
    '''
    The function is used to log some functional data. Is config variable IS_DEBUG_MODE is true, it will log a little
    bit more.
    :param func: a decorated function
    :return: a decorator;
    :rtype: function
    '''
    @wraps(func)
    def wrapper(*args, **kwargs):
        '''
        Logs a functional data
        :return: whatever func returns
        :rtype: type of func return value
        '''
        log_text = f'\'{func.__name__}\' started!\n'

        if DungeonGameConfig.IS_DEBUG_MODE:
            argument_names = list(inspect.signature(func).parameters.keys())
            evaluated_arguments = dict(zip(argument_names, args))
            log_text += f'\tParams: {evaluated_arguments}\n'
            
        logging.debug(log_text)
        
        return_value = func(*args, **kwargs)
        log_text = f'\'{func.__name__}\' ended!\n'
        if DungeonGameConfig.IS_DEBUG_MODE:
            log_text += f'\treturn value: \'{return_value}\''

        logging.debug(log_text)
        return return_value
    
    return wrapper
