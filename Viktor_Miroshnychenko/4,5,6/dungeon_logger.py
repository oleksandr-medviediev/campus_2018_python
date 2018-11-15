import logging


DEBUG_LOG_FILE = 'dungeon_debug.log'


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

debug_file = open(DEBUG_LOG_FILE, 'w')
debug_handler = logging.FileHandler(DEBUG_LOG_FILE)
debug_handler.setLevel(logging.DEBUG)
debug_formater = logging.Formatter('[%(asctime)s][%(levelname)s] %(message)s')
debug_handler.setFormatter(debug_formater)

info_handler = logging.StreamHandler()
info_handler.setLevel(logging.INFO)
info_formatter = logging.Formatter('%(message)s')
info_handler.setFormatter(info_formatter)

logger.addHandler(debug_handler)
logger.addHandler(info_handler)

