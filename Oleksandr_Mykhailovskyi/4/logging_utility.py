import logging


def logging_setup(logger):
    """
    Sets everything up for logging

    Args:
        logger (Logger): loggerinstance
    """
    # setup filestream handler
    logging_fh = logging.FileHandler('game.log')
    logging_fh.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logging_fh.setFormatter(formatter)
    logger.addHandler(logging_fh)

    # Setup stream handler
    logging_ch = logging.StreamHandler()
    logging_ch.setLevel(logging.INFO)
    logger.addHandler(logging_ch)


# Logger, handlers
logger = logging.getLogger('Utilities_app')
logger.setLevel(logging.DEBUG)
logging_setup(logger)
