import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)
FORMAT = logging.Formatter('%(message)s')
stream_handler.setFormatter(FORMAT)
logger.addHandler(stream_handler)

file_handler = logging.FileHandler("debug_log.log")
file_handler.setLevel(logging.DEBUG)
FORMAT = logging.Formatter('%(asctime)s - %(message)s')
file_handler.setFormatter(FORMAT)
logger.addHandler(file_handler)

