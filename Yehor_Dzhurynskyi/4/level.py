import random
import math


def generate_level(size):

    num_of_traps = (size * size) // 10
    num_of_treasures = (size * size) // 20
    num_of_empty_space = (size * size) - num_of_traps - num_of_treasures

    lvl = '!' * num_of_traps + '$' * num_of_treasures + '_' * num_of_empty_space
    cells = list(lvl)
    random.shuffle(cells)
    lvl = ''.join(cells)

    return lvl


def validate(lvl):

    lvl_size = size(lvl)
    is_valid = isinstance(lvl_size, int) and lvl_size > 0 and len(lvl) > 0

    return is_valid


def get_cell(lvl, x, y):

    lvl_size = size(lvl)
    cell = '#' if x < 0 or y < 0 or x >= lvl_size or y >= lvl_size else lvl[x + y * lvl_size]

    return cell


def size(lvl):

    size = int(math.sqrt(len(lvl)))

    return size


def print_level(lvl, player_x, player_y):

    lvl_size = size(lvl)
    for row in range(lvl_size):

        lvl_row = lvl[row * lvl_size: row * lvl_size + lvl_size]
        print(lvl_row)
