import logging

logging_object = logging.getLogger('Global dungeon game logger')

logging.basicConfig(
    filename='information.log',
    level = logging.DEBUG,
    format = '%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s',
    datefmt="%Y-%m-%d %H:%M:%S")

stream_logger = logging.StreamHandler()
stream_logger.setLevel(logging.INFO)
stream_formatter = logging.Formatter('%(message)s')
stream_logger.setFormatter(stream_formatter)

logging_object.addHandler(stream_logger)
