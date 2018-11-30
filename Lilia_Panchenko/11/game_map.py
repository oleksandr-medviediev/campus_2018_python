from random import choice
from logger import my_logger
import logging
from custom_exception import MapSizeError


class GameMap:
    """
    Class to control game map. Responsible for setting up map, generating traps and treasures, input map size
    """

    def __init__(self):
        """
        Constructor for GameMap class
        """
        self.mapsize = 0
        self.game_map = []

    @my_logger.debug_decorator
    @my_logger.info_decorator
    def setup_map(self):
        """
        Function called to set initial values for map and generate it
        : return : nothing
        """
        self.mapsize = self.input_map_size()
        self.game_map = self.generate_map()


    @my_logger.debug_decorator
    @my_logger.info_decorator
    def get_to_save_data(self):
        """
        Function called to get save data
        : return : map size and map 
        : rtype : tuple
        """
        return self.mapsize, self.game_map


    @my_logger.debug_decorator
    @my_logger.info_decorator
    def generate_cells(self, num):
        """
        Function called to generate defined amount of cells 
        : param : num - divisor to calculate amount of cells by formula mapsize / num
        : ptype : int
        : return : generated cells' indeces 
        : rtype : list
        """
        try:
            cell_amount = self.mapsize * self.mapsize // num
            
        except ZeroDivisionError:

            print("ZeroDivisionError!!!")
            return

        cells = [choice(range(self.mapsize * self.mapsize)) for i in range(cell_amount)]    

        return cells


    @my_logger.debug_decorator
    @my_logger.info_decorator
    def replace_cells(self, gamemap, num, replacement_value):
        """
        Function called to replace random list of cells by given value in given map
        : param1 : gamemap - game map
        : param2 : num - divisor to calculate amount of cells by formula mapsize / num
        : param3 : replacement_value - value to replace generated cells' values 
        : ptype1 : list
        : ptype2 : int
        : ptype3 : int
        : return : modified gamemap
        : rtype : list
        """
        cells = self.generate_cells(num)
        cells_replacement = [replacement_value for i in cells]
        for (cell, replacement) in zip(cells, cells_replacement):
            gamemap[cell] = replacement

        return gamemap


    @my_logger.debug_decorator
    @my_logger.info_decorator
    def generate_map(self):
        """
        Function called to generate map. Generate traps, then cells then divide gamemap list for list to make square
        two-dimentional array
        : return : modified gamemap
        : rtype : list of lists
        """
        gamemap = [ 0 for i in range(self.mapsize) for j in range(self.mapsize)]
        gamemap = self.replace_cells(gamemap, 10, -1)
        gamemap = self.replace_cells(gamemap, 20, 1)
        gamemap = [ gamemap [i * self.mapsize: (i + 1) * self.mapsize] for i in range(self.mapsize) ]

        return gamemap


    @my_logger.debug_decorator
    @my_logger.info_decorator
    def input_map_size(self):
        """
        Function called to input map size
        : return : game map size
        : rtype : int
        """
        while True:
            map_size = input("Enter size of game map (greater than 8): ")
            try:
                map_size = int(map_size)

            except ValueError as error:
                logging.error(error)
                logging.info("You inputed something wrong! Try again...")

                continue

            try:    
                if map_size < 8:
                    raise MapSizeError("Too small map size!")
                else:
                    break

            except MapSizeError as error:
                logging.error(error)

        return int(map_size)
