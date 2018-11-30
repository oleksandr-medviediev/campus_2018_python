"""module provides logging functions for the game
"""

import logging
from decorators import debug_decorator
from decorators import info_decorator

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

_message_handler = logging.StreamHandler()
_message_handler.setLevel(logging.INFO)

logger.addHandler(_message_handler)

_file_handler = logging.FileHandler("log.txt", mode='w')
_file_handler.setLevel(logging.DEBUG)

_FILE_FORMAT = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
_file_handler.setFormatter(_FILE_FORMAT)

logger.addHandler(_file_handler)


def log_debug(message):
    """log message with severity DEBUG

    Arguments:
        message str -- message to log
    """

    logger.debug(message)


def log_info(message):
    """log message with severity INFO

    Arguments:
        message str -- message to log
    """

    logger.info(message)
