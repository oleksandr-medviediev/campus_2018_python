from functools import wraps
import logging
import inspect


class Logger:
    """
    Logger class. Makes info or debug logs according to info and debug decorators and player's choice about log or not
    his actions and game functions calls
    """
    def __init__(self):
        """
        Constructor for Logger class
        """
        self.m_debugLogger = logging.getLogger("debuglogger")
        self.m_debugLogger.setLevel(logging.DEBUG)

        self.m_infoLogger = logging.getLogger("infologger")
        self.m_infoLogger.setLevel(logging.INFO)

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

        self.m_infoLogger.addHandler(info_file_handler)
        self.m_infoLogger.addHandler(info_stream_handler)

        self.m_debugLogger.addHandler(debug_file_handler)

        self.is_debug = False
        self.is_info = False


    def set_debug_logging(self):
        """
        Function to setup log debug flag based on player's input.
        : param : nothing
        : return : nothing
        : rtype : None
        """
        self.is_debug

        inp_debug = input("Do you want to debug game? [(Y)es / (N)o]: ")
        inp_debug = inp_debug.casefold()

        available_answer = ['y', 'n', 'yes', 'no']
        while inp_debug not in available_answer:
            inp_debug = input("Something wrong, try again: ")
            inp_debug = inp_debug.casefold()

        if inp_debug == 'y' or inp_debug == 'yes':
            self.is_debug = True

        else:
            self.is_debug = False



    def set_info_logging(self):
        """
        Function to setup log info flag based on player's input.
        : param : nothing
        : return : nothing
        : rtype : None
        """
        self.is_info

        inp_info = input("Do you want to output logs for game? [(Y)es / (N)o]: ")
        inp_info = inp_info.casefold()

        available_answer = ['y', 'n', 'yes', 'no']
        while (inp_info not in available_answer):
            inp_info = input("Something wrong, try again: ")
            inp_info = inp_info.casefold()

        if inp_info == 'y' or inp_info == 'yes':
            self.is_info = True

        else:
            self.is_info = False


    def form_args_string(self, args_dict):
        """
        Function to form info about decorated function arguments.
        : param : arguments represented by dict
        : ptype : dict
        : return : string, which represents arguments from passed dictionary
        : rtype : str
        """
        args_str = ''
        for name, value in args_dict.items():
            args_str = args_str + '\n' + '\t'*5 + f'{name}: {value}'

        return args_str 


    def debug_decorator(self, f):

        @wraps(f)
        def wrapped(*args, **kwargs):

            if self.is_debug:

                self.m_debugLogger.debug(f"Function {f.__name__} started")

                if len(args) > 0:
                    f_args_names = inspect.signature(f).parameters
                    args_with_names = {k: v for (k, v) in zip(f_args_names, args)}
                    self.m_debugLogger.debug("Arguments:" + self.form_args_string(args_with_names))

                to_return = f(*args, **kwargs)
                self.m_debugLogger.debug("Result value:" + str(to_return))

                self.m_debugLogger.debug(f"Function {f.__name__} ended")

                return to_return

            else:
                return f(*args, **kwargs)

        return wrapped


    def info_decorator(self, f):

        @wraps(f)
        def wrapped(*args, **kwargs):

            if self.is_info:

                self.m_infoLogger.info(f"Function {f.__name__} started")

                to_return = f(*args, **kwargs)

                self.m_infoLogger.info(f"Function {f.__name__} ended")

                return to_return

            else:
                return f(*args, **kwargs)

        return wrapped

my_logger = Logger()
