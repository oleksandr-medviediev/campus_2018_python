from dg_logging import DG_loger as dec_log


DEBUG_MODE = False


def __decorator_debug_mode_checker(func, func_wraper):
    global DEBUG_MODE

    def __debug_mode_cheker(*args, **kvargs):

        global DEBUG_MODE
        result = None

        if DEBUG_MODE:
            result = func_wraper(*args, **kvargs)
        else:
            result = func(*args, **kvargs)
        return result
    
    return __debug_mode_cheker


def decorator_start_end_logging(func):
    
    def start_end_wraper(*args, **kvargs):
        
        dec_log.debug(f'{func.__name__} : started')
        result = func(*args, **kvargs)
        dec_log.debug(f'{func.__name__} : ended')
        return result

    result = __decorator_debug_mode_checker(func, start_end_wraper)
    return result


def decorator_logigng_param_andresult_of_function(func):

    def logigng_param_and_result_of_function(*args, **kvargs):

        for param in args:
            dec_log.debug(param)
        for param in kvargs:
            dec_log.debug(param)

        result = func(*args, **kvargs)
        dec_log.debug(result)

        return result

    result = __decorator_debug_mode_checker(func, logigng_param_and_result_of_function)
    return result
