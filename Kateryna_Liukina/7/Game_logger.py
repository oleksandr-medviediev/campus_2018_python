import logging
import Custom_decorator


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

stdout_handler = logging.StreamHandler()
stdout_handler.setLevel(logging.INFO)
stdout_formatter = logging.Formatter('[%(levelname)s] %(message)s')
stdout_handler.setFormatter(stdout_formatter)

file_handler = logging.FileHandler('dungeon_game.log')
file_handler.setLevel(logging.DEBUG)
file_formatter = logging.Formatter('[%(levelname)s][%(asctime)s] %(message)s')
file_handler.setFormatter(file_formatter)

logger.addHandler(stdout_handler)
logger.addHandler(file_handler)


log_decorator = Custom_decorator.log_decorator_factory(logger)
debug_decorator = Custom_decorator.debug_decorator_factory(logger)