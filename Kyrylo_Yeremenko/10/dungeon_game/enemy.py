"""
This module defines enemy class for task 9.1 from Coding Campus 2018 Python course
(Dungeon Game)
"""

import random
import logging
import datetime
import threading
from dungeon_game.dungeon_map import DungeonMap
import dungeon_game.utils as utils
import dungeon_game.log as log
import dungeon_game.config as config
from dungeon_game.decorators import log_decorator, debug_log_decorator

logger = logging.getLogger(log.LOGGER_NAME)


class Enemy:

    def __init__(self, active_map, active_player):

        self.position = [0, 0]
        self.player = active_player
        self.dungeon_map = active_map
        self.init_position(active_map, active_player.position)

    @log_decorator
    @debug_log_decorator
    def update_loop(self):
        """
        Updates enemy position every 3 seconds
        :return:
        """

        last_update = datetime.datetime.now()
        dt = datetime.timedelta()

        while self.player.get_hitpoints() > 0 and self.player.bag < config.PLAYER_BAG_SIZE:

            if dt >= datetime.timedelta(seconds=3):

                self.move(self.dungeon_map)
                dt = datetime.timedelta()
                last_update = datetime.datetime.now()

            else:
                dt = datetime.datetime.now() - last_update

    @log_decorator
    @debug_log_decorator
    def move(self, active_map):
        """
        Moves enemy to random tile
        :param active_map: DungeonMap instance
        :return: None
        """

        directions = ["U", "L", "R", "D"]

        while True:

            direction = random.choice(directions)
            position_offset = None

            if direction == "U":
                position_offset = (-1, 0)
            elif direction == "L":
                position_offset = (0, -1)
            elif direction == "R":
                position_offset = (0, +1)
            elif direction == "D":
                position_offset = (+1, 0)

            if active_map.is_index_valid(utils.vector_sum(self.position, position_offset)):

                self.position = utils.vector_sum(self.position, position_offset)
                logger.debug(f"Enemy moved to {self.position}")

                if self.attempt_attack_player():
                    self.reset()

                break

            else:
                directions.remove(direction)

    @log_decorator
    @debug_log_decorator
    def init_position(self, active_map, position_player):
        """
        Randomly chooses enemy position on map; should be called after dungeon map was initialized
        :param active_map: DungeonMap instance
        :param position_player: Player position
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

                if not (position_player[0] == row and position_player[1] == column):

                    position = [row, column]
                    logger.debug(f"Initialized enemy position at {position}")
                    break

        self.position = position

    @log_decorator
    @debug_log_decorator
    def attempt_attack_player(self):
        """
        Attacks player if standing in the same tile
        :return: Bool, if player was attacked
        """

        return_value = False

        self.player.lock_position.acquire()

        if self.player.position[0] == self.position[0] and self.player.position[1] == self.position[1]:

            self.player.decrease_hitpoints()

            logger.info(f"Enemy found player and hit him for 1 hitpoint.")

            print("Something lashes out on you from the dungeon's shadows.")
            print("You suffer minor damage.")

            return_value = True

        self.player.lock_position.release()

        return return_value

    @log_decorator
    @debug_log_decorator
    def reset(self):
        self.init_position(self.dungeon_map, self.player.position)


class ThreadEnemyWrapper(threading.Thread):

    def __init__(self, active_map, active_player):

        super().__init__()
        self.enemy = Enemy(active_map, active_player)

    def run(self):

        self.enemy.update_loop()
