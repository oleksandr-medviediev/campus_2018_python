from random import choice
from logger import debug_decorator
from logger import info_decorator


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

        cell_amount = self.mapsize * self.mapsize // num
        cells = [choice(range(self.mapsize * self.mapsize)) for i in range(cell_amount)]    

        return cells


    @debug_decorator
    @info_decorator
    def replace_cells(num, replacement_value):

        cells = self.generate_cells(num)
        cells_replacement = [replacement_value for i in cells]
        for (cell, replacement) in zip(cells, cells_replacement):
            gamemap[cell] = replacement

        return gamemap


    @debug_decorator
    @info_decorator
    def generate_map(self):

        gamemap = [ 0 for i in range(self.mapsize) for j in range(self.mapsize)]
        gamemap = replace_cells(10, -1)
        gamemap = replace_cells(20, 1)
        gamemap = [ gamemap [i * self.mapsize: (i + 1) * self.mapsize] for i in range(self.mapsize) ]

        return gamemap


    @debug_decorator
    @info_decorator
    def input_map_size(self):

        map_size = input("Enter size of game map: ")

        while (not map_size.isdigit()) or int(map_size) < 8:
            map_size = input("Something wrong entered\nTry again: ")

        return int(map_size)
