import logging


my_logger = logging.getLogger(__name__)
my_logger.setLevel(logging.DEBUG)

handler_info_stream = logging.StreamHandler()
formater_stream = logging.Formatter('%(message)s')
handler_info_stream.setLevel(logging.INFO)
handler_info_stream.setFormatter(formater_stream)

handler_debug_file = logging.FileHandler('debug_log.txt')
formater_file = logging.Formatter('%(asctime)s: %(funcName)s from %(module)s at %(lineno)d says: %(message)s')
handler_debug_file.setLevel(logging.DEBUG)
handler_debug_file.setFormatter(formater_file)

my_logger.addHandler(handler_info_stream)
my_logger.addHandler(handler_debug_file)
