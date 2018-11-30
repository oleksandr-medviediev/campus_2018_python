from random import choice
from math import floor
from .game_logger import log_decorator
from .game_logger import debug_decorator
from .custom_exeption import InvalidMapSizeError

class GameMap:

    @log_decorator
    @debug_decorator
    def __init__(self, map_size, percent_of_traps, percent_of_treasures):
        """
        Function creates map
        Args:
            map_size(list(int)): map size
            percent_of_traps(float): percent of traps
            percent_of_treasures(float): percent of treasures
        Returns:
            none
        """
        if map_size[0] < 5 and map_size[1] < 5:
            raise InvalidMapSizeError("Map size must be greater than 4.")
        
        self.size = map_size
        self.map_ = [[0] * map_size[1] for _ in range(map_size[0])]
        self.generatemap_(map_size, percent_of_traps, percent_of_treasures)


    @log_decorator
    @debug_decorator
    def generatemap_(self, map_size, percent_of_traps, percent_of_treasures):
        """
        Function generate map for dungeon game
        Args:
            map_size(list(int)): map size
            percent_of_traps(float): percent of traps
            percent_of_treasures(float): percent of treasures
        Returns:
            list(list(int))
        """

        number_of_traps = max(3, floor(map_size[0] * map_size[1] * percent_of_traps))
        number_of_treasures = max(3, floor(map_size[0] * map_size[1] * percent_of_treasures))

        self.generate_specific_item(number_of_traps, 1)
        self.generate_specific_item(number_of_treasures, 2)


    @log_decorator
    @debug_decorator
    def generate_specific_item(self, number_of_item, game_item):
        """
        Function generate number_of_item game_item on map_
        Args:
            number_of_item(int): number of item
            game_item(int): 1 - trap, 2 - treasure
        Returns:
            none
        """
        for i in range(number_of_item):

            coordinates = self.generate_coordinates()

            self.map_[coordinates[0]][coordinates[1]] = game_item


    @log_decorator
    @debug_decorator
    def generate_coordinates(self):
        """
        Function generate coordinates without traps and treasure on map_
        Returns:
            list(int)
        """
        row = choice(range(self.size[0]))
        column = choice(range(self.size[1]))

        while self.map_[row][column] != 0:
            row = choice(range(self.size[0]))
            column = choice(range(self.size[1]))

        return [row, column]

