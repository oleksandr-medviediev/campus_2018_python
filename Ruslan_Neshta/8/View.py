from DungeonLogger import main_logger
from DungeonLogger import debugger_output


@debugger_output()
def warn_player(treasure=False, trap=True):
    """
    Prints warning message

    :param treasure: message about treasure
    :param trap:  message about trap
    :return: nothing
    :rtype: None
    """

    if treasure:
        main_logger.info('Warning: there is a treasure within one square from you!')

    if trap:
        main_logger.info('Warning: there is a trap within one square from you!')
