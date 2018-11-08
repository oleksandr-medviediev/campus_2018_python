def print_map(world_map):
    """
    Prints world map

    :param world_map: world
    :return: nothing
    :rtype: None
    """

    for i in world_map:
        line = ''.join(i)
        print('|', line, '|')


def print_map_hide_secrets(world_map, secrets, default):
    """
    Prints world map without secrets

    :param world_map: map
    :param secrets: object to hide
    :param default: what will be printed instead of secrets
    :return:
    """

    for i in world_map:

        print('|', sep='', end='')
        for j in i:

            if j in secrets:
                print(default, sep='', end='')
            else:
                print(j, sep='', end='')

        print('|', sep='')


def warn_player(treasure=False, trap=True):
    """
    Prints warning message

    :param treasure: message about treasure
    :param trap:  message about trap
    :return: nothing
    :rtype: None
    """

    if treasure:
        print('Warning: there is a treasure within one square from you!')

    if trap:
        print('Warning: there is a trap within one square from you!')


if __name__ == "__main__":
    w = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', '@', ' ', '@', ' ', ' ', ' ', ' '],
         [' ', ' ', '@', '#', '#', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', '@', ' ', ' ', ' '],
         [' ', ' ', '#', ' ', ' ', '#', '@', ' ', ' ', '#'], ['#', ' ', ' ', ' ', '#', '#', ' ', ' ', ' ', ' ']]
    print_map(w)
