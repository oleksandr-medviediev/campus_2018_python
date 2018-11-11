"""
This module log init for task 5.1 from Coding Campus 2018 Python course
(Dungeon Game)
"""

import logging
import sys

LOGGER_NAME = "gameLogger"
LOGGER_PATH = "game.log"
logger = logging.getLogger(LOGGER_NAME)


def init_logger():
    """
    Initializes logger
    :return:
    """

    logger = logging.getLogger(LOGGER_NAME)
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    file_handler = logging.FileHandler(LOGGER_PATH)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setLevel(logging.INFO)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    logger.debug("Logger init complete")

