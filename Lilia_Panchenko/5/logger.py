import logging

m_logger = logging.getLogger(__name__)
m_logger.setLevel(logging.DEBUG)

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)
stream_format = logging.Formatter('%(message)s')
stream_handler.setFormatter(stream_format)


file_handler = logging.FileHandler("dungeon_game.log")
file_handler.setLevel(logging.DEBUG)
file_format = logging.Formatter('%(asctime)s // %(message)s')
file_handler.setFormatter(file_format)

m_logger.addHandler(stream_handler)
m_logger.addHandler(file_handler)
