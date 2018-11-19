import logging


main_logger = logging.getLogger(__name__)
logging.basicConfig(filename='debug.log', filemode='w', level=logging.DEBUG,
                    format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s')

info_logger = logging.StreamHandler()
info_logger.setLevel(logging.INFO)
stream_formatter = logging.Formatter('%(message)s')
info_logger.setFormatter(stream_formatter)

main_logger.addHandler(info_logger)


if __name__ == "__main__":
    main_logger.info('some text here')
