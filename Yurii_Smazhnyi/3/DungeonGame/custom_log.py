import logging


is_debug = False
warning = None
error = None
info = None


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

console_formatter = logging.Formatter('%(message)s')
console_handler.setFormatter(console_formatter)

log_file = open('dungeon_game.log', "w")
file_handler = logging.StreamHandler(log_file)
file_handler.setLevel(logging.DEBUG)
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)

info_logger = logging.getLogger("Info")

def debug_decorator(func):
    """
    Decorator for printing info about function.

    :param func: function that need decorating.
    :func type: function.
    :returns: decorated function.
    :rtype: function.
    """
    global is_debug

    return_func = None

    if is_debug:
    
        def func_wrapper(msg, *args, **kwargs):

            logger.info(f'Called from function: "{func.__name__}"')
            logger.info(f"Arguments {msg, args, kwargs}")
            func(msg, *args, **kwargs)
        
        return_func = func_wrapper
    
    else:
        
        return_func = func

    return return_func


def toggle_debug():
    """
    Toggles debug setting.

    :returns: None.
    :rtype: None.
    """
    global is_debug

    is_debug = not is_debug

    create_decorators()


def create_decorators():
    """
    Creates decorators with new setting.

    :returns: None.
    :rtype: None.
    """
    global warning
    global info
    global error

    warning = debug_decorator(logger.info)
    info = debug_decorator(logger.info)
    error = debug_decorator(logger.error)
