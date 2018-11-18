"""
This module generates map for task 4.1 from Coding Campus 2018 Python course
(Dungeon Game)
"""

import logging
import random
import utils
import log
from decorators import log_decorator

SYMBOL_TILE = '*'
SYMBOL_TRAP = '#'
SYMBOL_TREASURE = '@'
SYMBOL_PLAYER = '+'
SYMBOL_LASTPOS = 'X'

RATIO_TRAPS = 10.0
RATIO_TREASURE = 20.0

game_map = None
logger = logging.getLogger(log.LOGGER_NAME)


@log_decorator
def generate(size):
    """
    Generates map for Dungeon Game
    :param size: Map square size
    :return: None
    """

    global game_map

    if isinstance(game_map, list):
        game_map.clear()

    trap_count = int((size ** 2) / RATIO_TRAPS)
    treasure_count = int((size ** 2) / RATIO_TREASURE)

    game_map = [[SYMBOL_TILE for j in range(size)] for i in range(size)]

    for trap_index in range(trap_count):

        while True:

            row = random.randint(0, size - 1)
            column = random.randint(0, size - 1)

            if game_map[row][column] == SYMBOL_TILE:

                game_map[row][column] = SYMBOL_TRAP
                break

    for treasure_index in range(treasure_count):

        while True:

            row = random.randint(0, size - 1)
            column = random.randint(0, size - 1)

            if game_map[row][column] == SYMBOL_TILE:

                game_map[row][column] = SYMBOL_TREASURE
                break

    logger.debug(f"Generated map; {size} x {size} tiles, {trap_count} traps and {treasure_count} treasures")


@log_decorator
def is_index_valid(index):
    """
    Checks if index is valid
    :param index: Tuple or list containing pair of indexes (X, Y) to be checked
    :return: Bool value identifying validity of index
    """

    map_size = len(game_map)
    is_x_valid = False
    is_y_valid = False

    if 0 <= index[0] <= (map_size - 1):
        is_x_valid = True
    if 0 <= index[1] <= (map_size - 1):
        is_y_valid = True

    return is_x_valid and is_y_valid


@log_decorator
def check_nearby_tiles(position):
    """
    Checks if any traps or treasures exist in one tile radius from player (ignoring diagonal tile)
    :param position: Player position
    :return: Tuple containing two bool values, if there is a trap nearby, and if there is treasure nearby
    """

    logger.info("Checking nearby tiles...")

    offset_left = (0, -1)
    offset_right = (0, +1)
    offset_up = (-1, 0)
    offset_down = (+1, 0)

    offsets = [offset_left, offset_right, offset_up, offset_down]
    offsets = [utils.vector_sum(position, offset) for offset in offsets if is_index_valid(utils.vector_sum(position, offset))]

    is_trap_nearby = False
    is_treasure_nearby = False

    for offset in offsets:

        if game_map[offset[0]][offset[1]] == SYMBOL_TRAP:

            is_trap_nearby = True
            logger.debug(f"Nearby tile at {offset} contains trap")

        if game_map[offset[0]][offset[1]] == SYMBOL_TREASURE:

            is_treasure_nearby = True
            logger.debug(f"Nearby tile at {offset} contains treasure")

        if is_treasure_nearby and is_trap_nearby:
            break

    return is_trap_nearby, is_treasure_nearby


@log_decorator
def check_current_tile(position):
    """
    Check if player position contains trap or treasure
    :param position: Player position
    :return: Tuple containing two bool values, if position contains trap, and if position contains treasure
    """

    logger.info(f"Checking current tile at {position}...")

    is_trap = False
    is_treasure = False

    if game_map[position[0]][position[1]] is SYMBOL_TRAP:

        is_trap = True
        logger.debug("Current tile contains trap")

    elif game_map[position[0]][position[1]] is SYMBOL_TREASURE:

        is_treasure = True
        logger.debug("Current tile contains treasure")

    else:
        logger.debug("Current tile is normal tile")

    return is_trap, is_treasure


@log_decorator
def print_map():
    """
    Outputs dungeon map
    :return:
    """

    output_map = []

    for row in game_map:
        output_map.append(' '.join(row))

    print('\n'.join(output_map))
    print(f"\nLEGEND:\n{SYMBOL_TILE} - Regular tile\n{SYMBOL_TRAP} - Trap\n{SYMBOL_TREASURE} - Treasure")
    print(f"{SYMBOL_PLAYER} - Player Path\n{SYMBOL_LASTPOS} - Last position")
