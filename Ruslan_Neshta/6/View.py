from DungeonLogger import main_logger
from DungeonLogger import debugger_output


@debugger_output
def print_map(world_map):
    """
    Prints world map

    :param world_map: world
    :return: nothing
    :rtype: None
    """

    for i in world_map:
        line = ''.join(['|', *i, '|'])
        main_logger.info(line)


@debugger_output
def print_map_hide_secrets(world_map, secrets, default):
    """
    Prints world map without secrets

    :param world_map: map
    :param secrets: object to hide
    :param default: what will be printed instead of secrets
    :return: nothing
    :rtype: None
    """

    for i in world_map:

        lines = ['|']
        for j in i:

            if j in secrets:
                lines.append(default)
            else:
                lines.append(j)

        lines.append('|')
        main_logger.info(''.join(lines))


@debugger_output
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


if __name__ == "__main__":
    w = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', '@', ' ', '@', ' ', ' ', ' ', ' '],
         [' ', ' ', '@', '#', '#', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', '@', ' ', ' ', ' '],
         [' ', ' ', '#', ' ', ' ', '#', '@', ' ', ' ', '#'], ['#', ' ', ' ', ' ', '#', '#', ' ', ' ', ' ', ' ']]
    print_map(w)
