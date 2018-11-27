from random import randint
from dungeon_logger import my_logger
from dungeon_logger import log_decorator


class Enemy:

    @log_decorator
    def __init__(self):

        self.enemy_x = 0
        self.enemy_y = 0


    @log_decorator
    def randomize_initial_position(self, dungeon_map):
        """
        Enemy position randomize. Used at start and after biting player
        """
        my_logger.debug("Trying to find empty place for enemy...")

        while True:

            self.enemy_x = randint(0, dungeon_map.map_size[0] - 1)
            self.enemy_y = randint(0, dungeon_map.map_size[1] - 1)

            if dungeon_map.get_cell_content(self.enemy_y, self.enemy_x) != '-':

                continue

            else:

                break

        my_logger.debug("Empty place for enemy has been found")

        return None


    @log_decorator
    def make_move(self, move_direction, width, height):
        """
        Used to change coordinates of enemy
        A little bit redundant method, however clear enough.
        Enemy moves in any case, through repelling from walls if the way has been blocked by the wall
        """
        if move_direction == 'w':

            if self.enemy_y > 0:

                self.enemy_y -=1
                my_logger.debug('Enemy have moved up')

            else:

                self.enemy_y +=1
                my_logger.debug('Enemy have moved down')

        elif move_direction == 'd':

            if self.enemy_x < width - 1:

                self.enemy_x +=1
                my_logger.debug('Enemy have moved right')

            else:

                self.enemy_x -=1
                my_logger.debug('Enemy have moved left')

        elif move_direction == 's':

            if self.enemy_y < height - 1:

                self.enemy_y +=1
                my_logger.debug('Enemy have moved down')

            else:

                self.enemy_y -=1
                my_logger.debug('Enemy have moved up')

        elif move_direction == 'a':

            if self.enemy_x > 0:

                self.enemy_x -=1
                my_logger.debug('Enemy have moved left')

            else:

                self.enemy_x +=1
                my_logger.debug('Enemy have moved right')

        return None
