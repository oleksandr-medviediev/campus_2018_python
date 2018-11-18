import random
from enum import Enum
from LoggerDecorator import logger_decorator


class DungeonCell(Enum):
    EMPTY = 0
    PLAYER = 1
    TREASURE = 2
    TRAP = 3


@logger_decorator
def choose_random_index_and_remove(array2D):
    '''
    Function chooses a random row and column in 2D array, returns it and removed it's cell from the array2D;
    :param array2D: a 2D array;
    :return: a pair of row and column index;
    :type array2D: a list of lists;
    :rtype: a tuple of 2 integers.
    '''
    chosen_row = random.choice(range(len(array2D)))
    chosen_column = random.choice(array2D[chosen_row])
    array2D[chosen_row].remove(chosen_column)
    return chosen_row, chosen_column


@logger_decorator
def generate_map(map_size):
    '''
    Function generates a map for Dungeon Game. map_size should be >= 5;
    :param map_size: a size of map. Map will we a 2D array and it's size will be map_size * map_size;
    :return: a generated map with treasures, traps and player and player position;
    :type map_size: an integer;
    :rtype: a tuple with tuple with two integers (player position) and list of lists of enums (map)
    If looks like this: tuple(tuple(int, int), list(list(DungeonCell)))
    '''
    dungeon_map = [[DungeonCell.EMPTY] * map_size for i in range(map_size)]

    free_map_cells = [list(range(map_size)) for i in range(map_size)]

    traps_number = int(map_size ** 2 / 10)
    for i in range(traps_number):
        row, column = choose_random_index_and_remove(free_map_cells)
        dungeon_map[row][column] = DungeonCell.TRAP

    treasures_number = int(map_size ** 2 / 20)
    for i in range(treasures_number):
        row, column = choose_random_index_and_remove(free_map_cells)
        dungeon_map[row][column] = DungeonCell.TREASURE

    player_start_row, player_start_column = choose_random_index_and_remove(free_map_cells)
    dungeon_map[player_start_row][player_start_column] = DungeonCell.PLAYER

    return (player_start_row, player_start_column), dungeon_map
