from random import choice
from logger import debug_decorator
from logger import info_decorator


global mapsize
global game_map
game_map = []


@debug_decorator
@info_decorator
def init():

    set_map_size()
    generate_map()


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

    global game_map
    game_map = [ 0 for i in range(mapsize) for j in range(mapsize)]

    for (trap, replacement) in zip(traps, traps_replacement):
        game_map[trap] = replacement

    for (treasure, replacement) in zip(treasures, treasures_replacement):
        game_map[treasure] = replacement

    game_map = [ game_map [i * mapsize: (i + 1) * mapsize] for i in range(mapsize) ]


@debug_decorator
@info_decorator
def spawn_player():

    player_position = choice(range(mapsize * mapsize))

    row, col = player_position // mapsize, player_position % mapsize

    while game_map[row][col] == -1 or game_map[row][col] == 1:

        player_position = choice(range(mapsize * mapsize))
        row, col = player_position // mapsize, player_position % mapsize

    return row, col


@debug_decorator
@info_decorator
def set_map_size():

    global mapsize

    print("Enter size of game map: ")
    mapsize = input()

    while (not mapsize.isdigit()) or int(mapsize) < 5:

        print("Something wrong entered\nTry again: ")
        mapsize = input()

    mapsize = int(mapsize)
