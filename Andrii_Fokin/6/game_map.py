from random import randint as rint
from dg_logging import DG_loger as log
from dg_decorators import decorator_start_end_logging
from dg_decorators import decorator_logigng_param_and_result_of_function

game_map_size = 10
cell_free = '-'
cell_trap = '#'
cell_treasure = '@'
cell_player = 'P'

@decorator_start_end_logging
@decorator_logigng_param_and_result_of_function
def fill_free_cell(game_map, cell_type):
    while (True):
        i = rint(1, game_map_size)
        j = rint(1, game_map_size)

        if game_map[i][j] == cell_free:
            game_map[i][j] = cell_type
            return [j, i]

@decorator_start_end_logging
@decorator_logigng_param_and_result_of_function
def find_player_position(game_map):
    for i in range(1, game_map_size + 2):
        for j in range(1, game_map_size + 2):
            if game_map[i][j] == cell_player:
                return [j, i]


@decorator_start_end_logging
def new_map():
    game_map = [[cell_free for j in range(game_map_size + 2)] for i in range(game_map_size + 2)]
    
    for i in range(game_map_size + 2):
        game_map[i][0] = cell_trap
        game_map[0][i] = cell_trap

        game_map[i][game_map_size + 1] = cell_trap
        game_map[game_map_size + 1][i] = cell_trap
    
    for i in range((game_map_size**2) // 20):
        fill_free_cell(game_map, cell_trap)
        fill_free_cell(game_map, cell_trap)
        fill_free_cell(game_map, cell_treasure)

    return game_map
