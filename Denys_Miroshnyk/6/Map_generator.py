from random import randint
from Custom_logger import logger as log
from Logger_decorator import debug_log_decorator

empty_cell = '🟋'
trap = '◉'
treasure = '⭐'
player = '웃'
wall = '⏹'


@debug_log_decorator
def init_free_cell(game_map, cell_type):
    while (True):
        i = randint(1, len(game_map[1])-2)
        j = randint(1, len(game_map[1])-2)

        if game_map[i][j] == empty_cell:
            game_map[i][j] = cell_type
            return [j, i]


@debug_log_decorator
def generate_map(map_size):
    terrain = [[empty_cell for j in range(map_size + 2)]
               for i in range(map_size + 2)]

    # generating walls
    for i in range(map_size + 2):
        terrain[i][0] = wall
        terrain[0][i] = wall

        terrain[i][map_size + 1] = wall
        terrain[map_size + 1][i] = wall

    # generating treasures
    for i in range((map_size**2) // 20):
        init_free_cell(terrain, treasure)

    # generating traps
    for i in range((map_size**2) // 10):
        init_free_cell(terrain, trap)

    return terrain


@debug_log_decorator
def find_player_position(game_map, field_size):
    for i in range(1, field_size + 2):
        for j in range(1, field_size + 2):
            if game_map[i][j] == player:
                log.debug(
                    f'find_player_position: player position is x = {j}, y = {i}')
                return (j, i)
