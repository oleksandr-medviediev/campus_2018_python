"""module provides logger for the game
"""

import logging

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
