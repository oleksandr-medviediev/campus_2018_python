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
    def generate_traps(self):

        traps_amount = self.mapsize * self.mapsize // 10
        traps = [choice(range(self.mapsize * self.mapsize)) for i in range(traps_amount)]    

        return traps


    @debug_decorator
    @info_decorator
    def generate_treasures(self):

        treasures_amount = self.mapsize * self.mapsize // 20
        treasures = [choice(range(self.mapsize * self.mapsize)) for i in range(treasures_amount)]

        return treasures


    @debug_decorator
    @info_decorator
    def generate_map(self):

        traps = self.generate_traps()
        treasures = self.generate_treasures()
        traps_replacement = [-1 for i in traps]
        treasures_replacement = [1 for i in treasures] 

        gamemap = [ 0 for i in range(self.mapsize) for j in range(self.mapsize)]

        for (trap, replacement) in zip(traps, traps_replacement):
            gamemap[trap] = replacement

        for (treasure, replacement) in zip(treasures, treasures_replacement):
            gamemap[treasure] = replacement

        gamemap = [ gamemap [i * self.mapsize: (i + 1) * self.mapsize] for i in range(self.mapsize) ]

        return gamemap


    @debug_decorator
    @info_decorator
    def input_map_size(self):

        print("Enter size of game map: ")
        map_size = input()

        # 8 - to give player chance to win
        while (not map_size.isdigit()) or int(map_size) < 8:

            print("Something wrong entered\nTry again: ")
            map_size = input()

        return int(map_size)
