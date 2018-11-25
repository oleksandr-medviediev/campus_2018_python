from functools import wraps
import logging
import inspect


is_debug = False
is_info = True


def set_debug_logging():

    global is_debug

    inp_debug = input("Do you want to debug game? [yes / no]: ")
    inp_debug = inp_debug.casefold()

    available_answer = ['y', 'n', 'yes', 'no']
    while inp_debug not in available_answer:
        inp_debug = input("Something wrong, try again: ")
        inp_debug = inp_debug.casefold()

    if inp_debug == 'y' or inp_debug == 'yes':
        is_debug = True

    else:
        is_debug = False



def set_info_logging():

    global is_info

    inp_info = input("Do you want to output logs for game? [yes / no]: ")
    inp_info = inp_info.casefold()

    available_answer = ['y', 'n', 'yes', 'no']
    while (inp_info not in available_answer):
        inp_info = input("Something wrong, try again: ")
        inp_info = inp_info.casefold()

    if inp_info == 'y' or inp_info == 'yes':
        is_info = True

    else:
        is_info = False


def form_args_string(args_dict):
    args_str = ''
    for name, value in args_dict.items():
        args_str = args_str + '\n' + '\t'*5 + f'{name}: {value}'

    return args_str 


def debug_decorator(f):
    @wraps(f)
    def wrapped(*args, **kwargs):

        if is_debug:

            m_debugLogger.debug(f"Function {f.__name__} started")

            if len(args) > 0:
                f_args_names = inspect.signature(f).parameters
                args_with_names = {k: v for (k, v) in zip(f_args_names, args)}
                m_debugLogger.debug("Arguments:" + form_args_string(args_with_names))

            to_return = f(*args, **kwargs)
            m_debugLogger.debug("Result value:" + str(to_return))

            m_debugLogger.debug(f"Function {f.__name__} ended")

            return to_return

        else:
            return f(*args, **kwargs)

    return wrapped


def info_decorator(f):
    @wraps(f)
    def wrapped(*args, **kwargs):

        if is_info:

            m_infoLogger.info(f"Function {f.__name__} started")

            to_return = f(*args, **kwargs)

            m_infoLogger.info(f"Function {f.__name__} ended")

            return to_return

        else:
            return f(*args, **kwargs)

    return wrapped


m_debugLogger = logging.getLogger("debuglogger")
m_debugLogger.setLevel(logging.DEBUG)

m_infoLogger = logging.getLogger("infologger")
m_infoLogger.setLevel(logging.INFO)

info_stream_handler = logging.StreamHandler()
info_stream_handler.setLevel(logging.INFO)

info_file_handler = logging.FileHandler("dungeon_game_info.log")
info_file_handler.setLevel(logging.INFO)
info_file_format = logging.Formatter('[info] %(asctime)s -- %(message)s')
info_file_handler.setFormatter(info_file_format)

debug_file_handler = logging.FileHandler("dungeon_game_debug.log")
debug_file_handler.setLevel(logging.DEBUG)
debug_file_format = logging.Formatter('[debug] %(asctime)s // %(message)s')
debug_file_handler.setFormatter(debug_file_format)

m_infoLogger.addHandler(info_file_handler)
m_infoLogger.addHandler(info_stream_handler)

m_debugLogger.addHandler(debug_file_handler)
