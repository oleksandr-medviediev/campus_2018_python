from dungeon_logger import my_logger
from dungeon_logger import log_decorator
from random import randint


class Character:
    """
    Character provides basic functionality: health and inventory
    """
    @log_decorator
    def __init__(self):

        self.health = 3
        self.treasures = 0


    @log_decorator
    def reset(self):

        self.health = 3
        self.treasures = 0


    @log_decorator
    def apply_damage(self):

        self.health -= 1


    @log_decorator
    def add_treasure(self):

        self.treasures += 1


    @log_decorator
    def draw_character(self):

        health_info = "".join(
            ['Health: ', *["[#]" for x in range(0, self.health)], 
            *["[ ]" for x in range(self.health, 3)]])

        treasures_info = "".join(
            ['Treasures: ', *["[@]" for x in range(0, self.treasures)], 
            *["[ ]" for x in range(self.treasures, 3)]])
        
        my_logger.info(" ".join([health_info, treasures_info]))


    @log_decorator
    def is_dead(self):

        result = self.health <= 0
        return result


    @log_decorator
    def is_winner(self):

        result = self.treasures >= 3
        return result


class Player(Character):
    """
    Advanced character: able to move and randomize initial position
    """
    @log_decorator
    def randomize_initial_position(self, dungeon_map):

        my_logger.debug("Trying to find empty place for palyer...")

        while True:

            self.player_x = randint(0, dungeon_map.map_size[0] - 1)
            self.player_y = randint(0, dungeon_map.map_size[1] - 1)

            if dungeon_map.get_cell_content(self.player_y, self.player_x) != '-':

                continue

            else:

                break

        my_logger.debug("Empty place for palyer has been found")

        return None


    @log_decorator
    def make_move(self, move_direction, width, height):

        if not move_direction in set(['w', 'd', 's', 'a']):

            my_logger.info('Wrong direction! Try again!')
            return False

        old_x = self.player_x
        old_y = self.player_y

        if move_direction == 'w':

            if self.player_y > 0:

                self.player_y -=1
                my_logger.info('You have moved up')

        elif move_direction == 'd':

            if self.player_x < width - 1:

                self.player_x +=1
                my_logger.info('You have moved right')

        elif move_direction == 's':

            if self.player_y < height - 1:

                self.player_y +=1
                my_logger.info('You have moved down')

        elif move_direction == 'a':

            if self.player_x > 0:

                self.player_x -=1
                my_logger.info('You have moved left')

        if old_x == self.player_x and old_y == self.player_y:

            my_logger.info("There is a wall!")

        return True
