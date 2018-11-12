"""
This module handles player movement and state for task 4.1 from Coding Campus 2018 Python course
(Dungeon Game)
"""

import random
import logging
import dungeon_map
import utils
import log

position = None
logger = logging.getLogger(log.LOGGER_NAME)


def move(direction):
    """
    Attempts to move player in specified direction
    :param direction: String containing direction character: U, L, R, D
    :return: Bool, if player moved to new location
    """

    global position

    logger.debug(f"Attempting to move player at {position} to {direction}...")

    direction = direction.upper()

    position_offset = None
    is_position_changed = False

    if direction == "U":
        position_offset = (-1, 0)
    elif direction == "L":
        position_offset = (0, -1)
    elif direction == "R":
        position_offset = (0, +1)
    elif direction == "D":
        position_offset = (+1, 0)

    if dungeon_map.is_index_valid(utils.vector_sum(position, position_offset)):

        position = utils.vector_sum(position, position_offset)

        if dungeon_map.game_map[position[0]][position[1]] == dungeon_map.SYMBOL_TILE:
            dungeon_map.game_map[position[0]][position[1]] = dungeon_map.SYMBOL_PLAYER

        is_position_changed = True
        logger.debug("Player moved successfully")

    else:
        logger.debug(f"Invalid position, couldn't move player to {direction}")

    return is_position_changed


def init_position():
    """
    Randomly chooses player position on map; should be called after dungeon map was initialized
    :return: None
    """

    global position

    map_size = len(dungeon_map.game_map)

    while True:

        row = random.randint(0, map_size - 1)
        column = random.randint(0, map_size - 1)

        if dungeon_map.game_map[row][column] == dungeon_map.SYMBOL_TILE:

            position = [row, column]
            logger.debug(f"Initialized player position at {position}")
            break


def mark_last_pos():
    """
    Marks last player position before Game Over on map
    :return: None
    """

    dungeon_map.game_map[position[0]][position[1]] = dungeon_map.SYMBOL_LASTPOS
    logger.debug(f"Marking last player position at {position}")
