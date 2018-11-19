from random import choice
from logger import debug_decorator
from logger import info_decorator


class GameMap:

    def __init__():
        print('ok2')
        self.mapsize = input_map_size()
        self.game_map = generate_map()


    @debug_decorator
    @info_decorator
    def get_to_save_data():
        return mapsize, game_map


    @debug_decorator
    @info_decorator
    def generate_traps():

        traps_amount = mapsize * mapsize // 10
        traps = [choice(range(mapsize * mapsize)) for i in range(traps_amount)]    

        return traps


    @debug_decorator
    @info_decorator
    def generate_treasures():

        treasures_amount = mapsize * mapsize // 20
        treasures = [choice(range(mapsize * mapsize)) for i in range(treasures_amount)]

        return treasures


    @debug_decorator
    @info_decorator
    def generate_map():

        traps = generate_traps()
        treasures = generate_treasures()
        traps_replacement = [-1 for i in traps]
        treasures_replacement = [1 for i in treasures] 

        game_map = [ 0 for i in range(mapsize) for j in range(mapsize)]

        for (trap, replacement) in zip(traps, traps_replacement):
            game_map[trap] = replacement

        for (treasure, replacement) in zip(treasures, treasures_replacement):
            game_map[treasure] = replacement

        game_map = [ game_map [i * mapsize: (i + 1) * mapsize] for i in range(mapsize) ]

        return game_map


    @debug_decorator
    @info_decorator
    def input_map_size():

        print("Enter size of game map: ")
        map_size = input()

        while (not map_size.isdigit()) or int(map_size) < 5:

            print("Something wrong entered\nTry again: ")
            map_size = input()

        return int(map_size)
