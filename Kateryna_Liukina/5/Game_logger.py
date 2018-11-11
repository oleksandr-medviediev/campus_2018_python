import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

stdout_handler = logging.StreamHandler()
stdout_handler.setLevel(logging.INFO)
stdout_formatter = logging.Formatter('[%(levelname)s] %(message)s')
stdout_handler.setFormatter(stdout_formatter)

logger.addHandler(stdout_handler)