from character import Character
from random import randint
import logger_decorator

class Enemy(Character):

    @logger_decorator.time_logger_decorator
    @logger_decorator.debug_logger_decorator
    def __init__(self, position):
        
        Character.__init__(self, 'Enemy', position)


    @logger_decorator.time_logger_decorator
    @logger_decorator.debug_logger_decorator
    def reinit(self, position):
        """
        Assigns new values to class attributes
        :param position: loaded position
        :paramtype position: list(int,int)
        """
        self.position = position


    @logger_decorator.time_logger_decorator
    @logger_decorator.debug_logger_decorator
    def check_enemy_status(self, player_position):
        """
        Checks if enemy's is in the same place as player
        :param player_position: current position of player
        :paramtype: list(int,int)
        :return: enemy's position equals to player's position
        :returntype: bool
        """
        enemy_is_here = False
        
        if self.position[0] == player_position[0] and self.position[1] == player_position[1]:
            enemy_is_here = True

        return enemy_is_here


    @logger_decorator.time_logger_decorator
    @logger_decorator.debug_logger_decorator
    def spawn_in_random_position(self, borders):
        """
        Spawns enemy in random position 
        :param borders: map size
        :paramtype: tuple(int,int)
        """

        self.position[0] = randint(0, borders[1] - 1)
        self.position[1] = randint(0, borders[0] - 1)
        
