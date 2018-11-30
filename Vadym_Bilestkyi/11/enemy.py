from dungeon_logging import logger

import time
import random


class Enemy:

    def __init__(self):
        self.position = [0, 0]
        self._moving_interval = 3
        self._is_alive = True

    def kill(self):
        self._is_alive = False

    def run_logic(self, world):
        while self._is_alive:
            time.sleep(self._moving_interval)

            neighbors = world.get_neighbor_cells(self.position)
            self.position = random.choice(neighbors)

            player = world.get_player()
            if self.position == player.position:
                player.hurt('ugly enemy')
                world.spawn_enemy(self)

                if player.is_dead():
                    logger.warning('Enemy has killed you. Provide input to finish the game.')
                    self.kill()
            else:
                logger.warning('Enemy is looking for you!')
