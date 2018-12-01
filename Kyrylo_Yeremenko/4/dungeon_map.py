"""
This module generates map for task 4.1 from Coding Campus 2018 Python course
(Dungeon Game)
"""

import logging
import random
import utils
import log
import config
from decorators import log_decorator, debug_log_decorator
from exceptions import MapInitError

logger = logging.getLogger(log.LOGGER_NAME)


class DungeonMap:

    SYMBOL_TILE = '*'
    SYMBOL_TRAP = '#'
    SYMBOL_TREASURE = '@'
    SYMBOL_PLAYER = '+'
    SYMBOL_LASTPOS = 'X'

    RATIO_TRAPS = 10.0
    RATIO_TREASURE = 20.0

    def __init__(self, size, do_generate=True):
        """
        Class constructor
        :param size: Generated map size
        :param do_generate: Whether to initiate map generation
        """

        if do_generate:
            self.game_map = self.generate(size)
        else:
            self.game_map = []

    @log_decorator
    @debug_log_decorator
    def generate(self, size):
        """
        Generates map for Dungeon Game
        :param size: Map square size
        :return: None
        """

        trap_count = int((size ** 2) / DungeonMap.RATIO_TRAPS)
        treasure_count = int((size ** 2) / DungeonMap.RATIO_TREASURE)

        if trap_count <= 0:
            raise MapInitError("Error initializing trap count. Try larger map size.")
        if treasure_count < config.PLAYER_BAG_SIZE:
            raise MapInitError("Error initializing treasure count. Try larger map size.")

        return_map = [[DungeonMap.SYMBOL_TILE for j in range(size)] for i in range(size)]

        for trap_index in range(trap_count):

            while True:

                row = random.randint(0, size - 1)
                column = random.randint(0, size - 1)

                if return_map[row][column] == DungeonMap.SYMBOL_TILE:

                    return_map[row][column] = DungeonMap.SYMBOL_TRAP
                    break

        for treasure_index in range(treasure_count):

            while True:

                row = random.randint(0, size - 1)
                column = random.randint(0, size - 1)

                if return_map[row][column] == DungeonMap.SYMBOL_TILE:

                    return_map[row][column] = DungeonMap.SYMBOL_TREASURE
                    break

        logger.debug(f"Generated map; {size} x {size} tiles, {trap_count} traps and {treasure_count} treasures")
        return return_map

    @log_decorator
    @debug_log_decorator
    def is_index_valid(self, index):
        """
        Checks if index is valid
        :param index: Tuple or list containing pair of indexes (X, Y) to be checked
        :return: Bool value identifying validity of index
        """

        map_size = len(self.game_map)
        is_x_valid = False
        is_y_valid = False

        if 0 <= index[0] <= (map_size - 1):
            is_x_valid = True
        if 0 <= index[1] <= (map_size - 1):
            is_y_valid = True

        return is_x_valid and is_y_valid

    @log_decorator
    @debug_log_decorator
    def check_nearby_tiles(self, position):
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
        offsets = [utils.vector_sum(position, offset) for offset in offsets if self.is_index_valid(utils.vector_sum(position, offset))]

        is_trap_nearby = False
        is_treasure_nearby = False

        for offset in offsets:

            if self.game_map[offset[0]][offset[1]] == DungeonMap.SYMBOL_TRAP:

                is_trap_nearby = True
                logger.debug(f"Nearby tile at {offset} contains trap")

            if self.game_map[offset[0]][offset[1]] == DungeonMap.SYMBOL_TREASURE:

                is_treasure_nearby = True
                logger.debug(f"Nearby tile at {offset} contains treasure")

            if is_treasure_nearby and is_trap_nearby:
                break

        return is_trap_nearby, is_treasure_nearby

    @log_decorator
    @debug_log_decorator
    def check_current_tile(self, position):
        """
        Check if player position contains trap or treasure
        :param position: Player position
        :return: Tuple containing two bool values, if position contains trap, and if position contains treasure
        """

        logger.info(f"Checking current tile at {position}...")

        is_trap = False
        is_treasure = False

        if self.game_map[position[0]][position[1]] is DungeonMap.SYMBOL_TRAP:

            is_trap = True
            logger.debug("Current tile contains trap")

        elif self.game_map[position[0]][position[1]] is DungeonMap.SYMBOL_TREASURE:

            is_treasure = True
            logger.debug("Current tile contains treasure")

        else:
            logger.debug("Current tile is normal tile")

        return is_trap, is_treasure

    @log_decorator
    @debug_log_decorator
    def print_map(self):
        """
        Outputs dungeon map
        :return:
        """

        output_map = []

        for row in self.game_map:
            output_map.append(' '.join(row))

        print('\n'.join(output_map))
        print(f"\nLEGEND:\n{DungeonMap.SYMBOL_TILE} - Regular tile\n{DungeonMap.SYMBOL_TRAP} - Trap\n{DungeonMap.SYMBOL_TREASURE} - Treasure")
        print(f"{DungeonMap.SYMBOL_PLAYER} - Player Path\n{DungeonMap.SYMBOL_LASTPOS} - Last position")
