import logging


my_logger = logging.getLogger(__name__)
my_logger.setLevel(logging.DEBUG)

handler_info_stream = logging.StreamHandler()
formater_stream = logging.Formatter('%(message)s')
handler_info_stream.setLevel(logging.INFO)
handler_info_stream.setFormatter(formater_stream)

handler_debug_file = logging.FileHandler('debug_log.txt')
formater_file = logging.Formatter('%(asctime)s: %(funcName)s from %(module)s: %(message)s')
handler_debug_file.setLevel(logging.DEBUG)
handler_debug_file.setFormatter(formater_file)

my_logger.addHandler(handler_info_stream)
my_logger.addHandler(handler_debug_file)


def logger_decorator_maker(is_debug = ''):

    if is_debug == '':

        while(True):

            is_debug = input('Print "y" if you want to enter in debug mode. "n" otherwise\n')

            if is_debug == 'y':

                handler_info_stream.setLevel(logging.DEBUG)
                break

            elif is_debug == 'n':

                break


    def debug_deco(my_func):

        def debug_wraper(*args):

            my_logger.debug(f"Function {my_func.__name__} has been called with args:")

            for arg in args:

                my_logger.debug(f"{type(arg)}")

            ret_value = my_func(*args)

            my_logger.debug(f"Function {my_func.__name__} has exited")

            return ret_value

        return debug_wraper

    return debug_deco


log_decorator = logger_decorator_maker();
