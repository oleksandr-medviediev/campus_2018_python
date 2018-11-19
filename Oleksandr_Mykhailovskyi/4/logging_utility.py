import logging


def logging_setup(logger):
    """
    Sets everything up for logging

    Args:
        logger (Logger): loggerinstance
    """
    # setup filestream handler
    logging_fh = logging.FileHandler('game.log')
    logging_fh.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logging_fh.setFormatter(formatter)
    logger.addHandler(logging_fh)

    # Setup stream handler
    logging_ch = logging.StreamHandler()
    logging_ch.setLevel(logging.INFO)
    logger.addHandler(logging_ch)


# Logger, handlers
logger = logging.getLogger('Utilities_app')
logger.setLevel(logging.DEBUG)
logging_setup(logger)
debug_mode = False


def logging_debug_decorator(function_to_decorate):
    """
    This is decorator.

    Args:
        function_to_decorate (function object)

    Returns:
        function object - wrapper.
    """
    global logger

    def wrapper(*args):
        """
        Wrapper function. Prints function name + arguments if debug_mode is True, 
        itherwise just function name on start, end.

        Args:
            *args : variable length unnamed arguments.
        Returns:
            whatever decorated function returns.
        """
        mstr = ""
        if debug_mode:
            mstr = " with: " + str(args)

        logger.debug(function_to_decorate.__name__ + mstr)
        result = function_to_decorate(*args)
        logger.debug(function_to_decorate.__name__ + " ended.")
        return result
    return wrapper


def logging_info_decorator(function_to_decorate):
    """
    This is decorator.

    Args:
        function_to_decorate (function object)

    Returns:
        function object - wrapper.
    """
    global logger

    def wrapper(*args):
        """
        Wrapper function. Prints function name on before and after start.
        Uses logger.info

        Args:
            *args : variable length unnamed arguments.
        Returns:
            whatever decorated function returns.
        """

        logger.info(function_to_decorate.__name__)
        result = function_to_decorate(*args)
        logger.info(function_to_decorate.__name__ + " ended.")
        return result
    return wrapper
