import custom_log

is_debug = False

def debug_decorator(func):
    """
    Decorator for printing info about function.

    :param func: function that need decorating.
    :func type: function.
    :returns: decorated function.
    :rtype: function.
    """   
    
    def func_wrapper(*args, **kwargs):
        
        global is_debug

        if is_debug:

            custom_log.logger.info(f'Called function: "{func.__name__}"')
            custom_log.logger.info(f"Arguments {args, kwargs}")

            result = func(*args, **kwargs) 

        else:

            result = func(*args, **kwargs)

        return result

    return func_wrapper


def toggle_debug():
    """
    Toggles debug setting.

    :returns: None.
    :rtype: None.
    """
    global is_debug

    is_debug = not is_debug
