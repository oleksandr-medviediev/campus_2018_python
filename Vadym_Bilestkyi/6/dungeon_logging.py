import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_format = logging.Formatter('[%(levelname)s] %(message)s')
console_handler.setFormatter(console_format)

file_handler = logging.FileHandler(filename='log.txt')
file_handler.setLevel(logging.DEBUG)
file_format = logging.Formatter('[%(levelname)s][%(asctime)s] %(message)s')
file_handler.setFormatter(file_format)

logger.addHandler(console_handler)
logger.addHandler(file_handler)
