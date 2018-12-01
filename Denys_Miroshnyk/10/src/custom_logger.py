import logging

logger = logging.getLogger('logger')
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

console_format = logging.Formatter('%(message)s')
console_handler.setFormatter(console_format)


file_handler = logging.FileHandler('logs.txt')
file_handler.setLevel(logging.DEBUG)

file_format = logging.Formatter('[%(asctime)s][%(levelname)s] %(message)s')
file_handler.setFormatter(file_format)

logger.addHandler(console_handler)
logger.addHandler(file_handler)
