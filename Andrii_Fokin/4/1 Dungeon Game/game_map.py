from random import randint as rint


game_map_size = 10
cell_free = 0
cell_trap = -1
cell_treasure = 1


def fill_free_cell(game_map, cell_type):
    while (True):
        i = rint(0, game_map_size - 1)
        j = rint(0, game_map_size - 1)

        if game_map[i][j] == cell_free:
            game_map[i][j] == cell_type
            break



def new_map():
    game_map = [[cell_free for j in range(game_map_size)] for i in range(game_map_size)]
    
    for i in range((game_map_size**2) / 20):
        fill_free_cell(game_map, cell_trap)
        fill_free_cell(game_map, cell_trap)
        fill_free_cell(game_map, cell_treasure)
    
    return game_map
