import logging
import functools

from Config import DEBUG_MODE

main_logger = logging.getLogger(__name__)
logging.basicConfig(filename='debug.log', filemode='w', level=logging.DEBUG,
                    format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s')

info_logger = logging.StreamHandler()
info_logger.setLevel(logging.INFO)
stream_formatter = logging.Formatter('%(message)s')
info_logger.setFormatter(stream_formatter)

main_logger.addHandler(info_logger)


def debugger_output(debug_mode_on=DEBUG_MODE):
    """
    Wraps function for debug output

    :param debug_mode_on: defines if debug is enabled
    :return: decorator function
    :rtype: function
    """

    if not debug_mode_on:
        return lambda x: x

    def decorate(func):
        """
        Decorates given function

        :param func: function to decorate
        :return: wrapper function
        :rtype: function
        """

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            """
            Clojure on decoration target function

            :param args: decoration target function arguments
            :param kwargs: decoration target function arguments
            :return: decoration target function invoking result
            """

            invoked_report = f'invoked {wrapper.__name__} with {args}, {kwargs}'
            main_logger.debug(invoked_report)
            main_logger.info(invoked_report)

            result = func(*args, **kwargs)

            executed_report = f'{wrapper.__name__} returned {result}'
            main_logger.debug(executed_report)
            main_logger.info(executed_report)
            return result

        return wrapper

    return decorate


if __name__ == "__main__":
    main_logger.info('some text here')
