import random
import math


def generate_level(size):
    """
    generating level for dungeon game
        :param int size: size of level that should be generated
        :return: string representation of level
        :rtype: str
    """

    num_of_traps = (size * size) // 10
    num_of_treasures = (size * size) // 20
    num_of_empty_space = (size * size) - num_of_traps - num_of_treasures

    lvl = '!' * num_of_traps + '$' * num_of_treasures + '_' * num_of_empty_space
    cells = list(lvl)
    random.shuffle(cells)
    lvl = ''.join(cells)

    return lvl


def validate(lvl):
    """
    validating whether lvl is valid representation of dungeon game level
        :param str lvl: string representation of level
        :return: whether level is valid
        :rtype: bool
    """

    lvl_size = size(lvl)
    is_valid = isinstance(lvl_size, int) and lvl_size > 0 and len(lvl) > 0

    return is_valid


def get_cell(lvl, x, y):
    """
    retrieves string representation of cell in coords (x, y)
        :param str lvl: string representation of level
        :param int x: x-coord of cell
        :param int y: y-coord of cell
        :return: cell of level in coords (x, y)
        :rtype: str
    """

    lvl_size = size(lvl)
    cell = '#' if x < 0 or y < 0 or x >= lvl_size or y >= lvl_size else lvl[x + y * lvl_size]

    return cell


def size(lvl):
    """
    calculates dimension of level
        :param str lvl: string representation of level
        :return: dimension of level
        :rtype: int
    """

    size = int(math.sqrt(len(lvl)))

    return size


def print_level(lvl, player_x, player_y):
    """
    docstring here
        :param str lvl: string representation of level
        :param int player_x: player x-position
        :param int player_y: player y-position
    """

    lvl_size = size(lvl)
    for row in range(lvl_size):

        lvl_row = lvl[row * lvl_size: row * lvl_size + lvl_size]
        print(lvl_row)
