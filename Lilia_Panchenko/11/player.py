from logger import my_logger
from random import choice
import logging

from custom_exception import PlayerInputError


class Player:
    """
    Player class. Responsible for spawn player on map, input player's choices, regulate player's hp and bag
    """

    def __init__(self):
        """
        Constructor for Player class
        """
        self.bag = 0
        self.hp = 3
        self.islost = False
        self.iswon = False


    @my_logger.debug_decorator
    @my_logger.info_decorator
    def set_player_name(self, name):
        """
        Function to setup player name
        : param : name - string which represents player name 
        : ptype : str  
        : return : None
        """
        self.name = name


    @my_logger.debug_decorator
    @my_logger.info_decorator
    def pick_treasure(self):
        """
        Function to make player pick treasure, checks if player won
        : return : None
        """
        self.bag += 1
        if self.bag >= 3:
            self.iswon = True


    @my_logger.debug_decorator
    @my_logger.info_decorator
    def lose_hp(self):
        """
        Function to make player lose 1 health point, checks if player lost
        : return : None
        """
        self.hp -= 1
        if self.hp <= 0:
            self.islost = True


    @my_logger.debug_decorator
    @my_logger.info_decorator

    def input_direction(self):
        """
        Function to get some player"s input 
        : return : string, which represents player"s choice
        : rtype : str
        """
        available_choices = ['up', 'down', 'left', 'right', 'save', 'exit']
        while True:

            player_choice = input('Where do you want to move:\n')
            player_choice.casefold()
            try:
                if player_choice not in available_choices:
                    raise PlayerInputError(player_choice)
                else:
                    break

            except PlayerInputError as error:
                logging.error(error)
                logging.info("Something wrong entered! Try again...")

        return player_choice


    @my_logger.debug_decorator
    @my_logger.info_decorator
    def spawn_player(self, game_map):
        """
        Function to get some player"s input 
        : param : game_map, game map represented by list of lists of integers in [-1, 0, 1]
        : return : nothing
        : rtype : None
        """
        self.position = choice(range(game_map.mapsize * game_map.mapsize))

        row, col = self.position // game_map.mapsize, self.position % game_map.mapsize

        while game_map.game_map[row][col] == -1 or game_map.game_map[row][col] == 1:

            self.position = choice(range(game_map.mapsize * game_map.mapsize))
            row, col = self.position // game_map.mapsize, self.position % game_map.mapsize

        self.position = []
        self.position.append(row)
        self.position.append(col)
