import logging
import MyGameLogic


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

debug_formatter = logging.Formatter('%(asctime)s - %(name)s - %(message)s')
info_formatter = logging.Formatter('%(message)s')

file_handler = logging.FileHandler('DebugLog.txt')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(debug_formatter)

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)
stream_handler.setFormatter(info_formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)


logger.debug('Game initialized')

MyGameLogic.run_game_cycle()
