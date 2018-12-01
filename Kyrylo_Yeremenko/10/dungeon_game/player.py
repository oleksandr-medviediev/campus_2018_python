"""
This module handles player movement and state for task 4.1 from Coding Campus 2018 Python course
(Dungeon Game)
"""

import random
import logging
import threading
from copy import copy
from dungeon_game.dungeon_map import DungeonMap
import dungeon_game.utils as utils
import dungeon_game.log as log
import dungeon_game.config as config
from dungeon_game.decorators import log_decorator, debug_log_decorator

logger = logging.getLogger(log.LOGGER_NAME)


class Player:

    def __init__(self, active_map):

        self.position = self.init_position(active_map)
        self.bag = 0
        self.hitpoints = config.PLAYER_HEALTH
        self.lock_position = threading.Lock()
        self.lock_health = threading.Lock()

    @log_decorator
    @debug_log_decorator
    def move(self, direction, active_map):
        """
        Attempts to move player in specified direction
        :param direction: String containing direction character: U, L, R, D
        :param active_map: DungeonMap instance
        :return: Bool, if player moved to new location
        """

        logger.debug(f"Attempting to move player at {self.position} to {direction}...")

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

        if active_map.is_index_valid(utils.vector_sum(self.position, position_offset)):

            position = utils.vector_sum(self.position, position_offset)

            if active_map.game_map[position[0]][position[1]] == DungeonMap.SYMBOL_TILE:
                active_map.game_map[position[0]][position[1]] = DungeonMap.SYMBOL_PLAYER

            self.lock_position.acquire()
            self.position = position
            self.lock_position.release()

            is_position_changed = True
            logger.debug("Player moved successfully")

        else:
            logger.debug(f"Invalid position, couldn't move player to {direction}")

        return is_position_changed

    @log_decorator
    @debug_log_decorator
    def init_position(self, active_map):
        """
        Randomly chooses player position on map; should be called after dungeon map was initialized
        :param active_map: DungeonMap instance
        :return: None
        """

        position = None

        map_size = len(active_map.game_map)

        if map_size == 0:
            position = [0, 0]
        else:

            while True:

                row = random.randint(0, map_size - 1)
                column = random.randint(0, map_size - 1)

                if active_map.game_map[row][column] == DungeonMap.SYMBOL_TILE:

                    position = [row, column]
                    logger.debug(f"Initialized player position at {position}")
                    break

        return position

    @log_decorator
    @debug_log_decorator
    def mark_last_pos(self, active_map):
        """
        Marks last player position before Game Over on map
        :param active_map: DungeonMap instance
        :return: None
        """

        active_map.game_map[self.position[0]][self.position[1]] = DungeonMap.SYMBOL_LASTPOS
        logger.debug(f"Marking last player position at {self.position}")

    def is_dead(self):
        """
        Checks if player is dead
        :return: Bool, if player is dead
        """
        return self.get_hitpoints() <= 0

    def is_bag_full(self):
        """
        Checks if treasure bag is full
        :return: Bool, if treasure bag is full
        """
        return self.bag >= config.PLAYER_BAG_SIZE

    def get_hitpoints(self):
        return copy(self.hitpoints)

    def decrease_hitpoints(self, damage=1):
        """
        Decrease player hitpoints thread-safely
        :param damage: Amount of damage, defaults to 1
        :return: None
        """
        self.lock_health.acquire()
        self.hitpoints -= damage
        self.lock_health.release()
