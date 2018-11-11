import logging


DEBUG_LOG_FILE = 'dungeon_debug.log'


logger = logging.getLogger(__name__)

debug_file = open(DEBUG_LOG_FILE, 'w')
debug_handler = logging.StreamHandler(debug_file)
debug_handler.setLevel(logging.DEBUG)

debug_formater = logging.Formatter('[%(asctime)s][%(levelname)s] %(message)s')
debug_handler.setFormatter(debug_formater)

logger.addHandler(debug_handler)
