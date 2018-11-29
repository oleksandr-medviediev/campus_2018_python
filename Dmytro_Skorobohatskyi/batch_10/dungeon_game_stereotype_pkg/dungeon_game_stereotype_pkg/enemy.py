from random import randint
from time import sleep

from .decorators import DebugDecorator, InfoDecorator
from .utilities import Utilities
from .constants import directions
from .player import Player
from .logging_system import logger

class Enemy:

    def __init__(self, x, y, map_size):
        self.x = x
        self.y = y
        self.map_size = map_size
        self.moving_interval = 3


    def __str__(self):
        
        return "Enemy" 

    
    @DebugDecorator()
    def get_coordinates(self):

        """ Function return enemy's coordinates.

            Return: 
                (int, int): specified coordinates.
        """

        x, y = self.x, self.y

        return x, y


    @DebugDecorator()
    def is_possible_to_move(self, direction_index):

        """ Function return enemy's coordinates.
            Args:
                direction_index(int): direction presenting by constant
            
            Return:
                (bool): return True if enemy can move in specified direction.
        """
        new_x, new_y = Utilities.get_new_coordinates(direction_index, self.x, self.y)

        is_possible = (new_x >= 0 and new_x < self.map_size) and (new_y >= 0 and new_y < self.map_size)

        return is_possible


    @DebugDecorator()
    def random_move(self):

        """ Function shifts enemy in random direction """

        direction_index = randint(0, len(directions) - 1)

        while not self.is_possible_to_move(direction_index):
            direction_index = randint(0, len(directions) - 1)

        shift_x, shift_y = Utilities.get_shift_by_direction(direction_index)

        self.x += shift_x
        self.y += shift_y


    @DebugDecorator()
    def damage(self, player):
        """ Function damage player by increasing of its hp by 1 point 
            Args:
                player(Player): object presenting player
            Return: 
                (none)
        """
        player.hp -= 1
        logger.info('Player has damaged. Now {} hp'.format(player.hp))


    @InfoDecorator('Enemy has respawned')
    @DebugDecorator()
    def respawn(self):
        """ Function place current enemy at random place """

        self.x, self.y = randint(0, self.map_size - 1), randint(0, self.map_size - 1)


    @DebugDecorator()
    def update(self, player, game_finished_event):
        """ Function present main enemy update loop 
            Args:
                player(Player): object presenting player
                game_finished_event(threading.Event): event which need to set if player dead or won
        """

        while player.is_alive() and not player.is_winner():
            sleep(self.moving_interval)
            
            self.random_move()
            if (player.get_coordinates()) == (self.get_coordinates()):
                self.damage(player)
                if not player.is_alive():
                    game_finished_event.set()
                else:
                    self.respawn()
            else:

                x, y = player.get_coordinates()

                for _, index in enumerate(directions.values()):

                    temp_x, temp_y = Utilities.get_new_coordinates(index, x, y)
                    
                    if (temp_x, temp_y) == (self.x, self.y):
                        logger.info('The enemy near. Run away.')
