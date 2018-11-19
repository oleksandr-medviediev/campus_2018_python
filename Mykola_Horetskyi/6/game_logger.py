import logging
import config


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

stream_handler = logging.StreamHandler()

if config.debug_mode:
    stream_handler.setLevel(logging.DEBUG)
else:
    stream_handler.setLevel(logging.INFO)

FORMAT = logging.Formatter('%(message)s')
stream_handler.setFormatter(FORMAT)
logger.addHandler(stream_handler)

file_handler = logging.FileHandler("dungeon_game_debug.log")
file_handler.setLevel(logging.DEBUG)
FORMAT = logging.Formatter('%(asctime)s - %(message)s')
file_handler.setFormatter(FORMAT)
logger.addHandler(file_handler)

