from random import choice
from logger import debug_decorator
from logger import info_decorator

from custom_exception import MapSizeError


class GameMap:

    def __init__(self):
        self.mapsize = 0
        self.game_map = []

    @debug_decorator
    @info_decorator
    def setup_map(self):
        self.mapsize = self.input_map_size()
        self.game_map = self.generate_map()


    @debug_decorator
    @info_decorator
    def get_to_save_data(self):
        return self.mapsize, self.game_map


    @debug_decorator
    @info_decorator
    def generate_cells(self, num):
        try:
            cell_amount = self.mapsize * self.mapsize // num
            
        except ZeroDivisionError:

            print("ZeroDivisionError!!!")
            return

        cells = [choice(range(self.mapsize * self.mapsize)) for i in range(cell_amount)]    

        return cells


    @debug_decorator
    @info_decorator
    def replace_cells(self, gamemap, num, replacement_value):

        cells = self.generate_cells(num)
        cells_replacement = [replacement_value for i in cells]
        for (cell, replacement) in zip(cells, cells_replacement):
            gamemap[cell] = replacement

        return gamemap


    @debug_decorator
    @info_decorator
    def generate_map(self):

        gamemap = [ 0 for i in range(self.mapsize) for j in range(self.mapsize)]
        gamemap = self.replace_cells(gamemap, 10, -1)
        gamemap = self.replace_cells(gamemap, 20, 1)
        gamemap = [ gamemap [i * self.mapsize: (i + 1) * self.mapsize] for i in range(self.mapsize) ]

        return gamemap


    @debug_decorator
    @info_decorator
    def input_map_size(self):

        while True:
            map_size = input("Enter size of game map (greater than 8): ")
            try:
                map_size = int(map_size)

            except ValueError:
                print("You inputed something wrong! Try again...")
                continue

            try:    
                if map_size < 8:
                    raise MapSizeError("Too small map size!")
                else:
                    break

            except MapSizeError:
                print("Looks like value, you have entered, is too small. Try to input something greater than 8...")

        return int(map_size)
