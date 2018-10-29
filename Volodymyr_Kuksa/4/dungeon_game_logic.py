from random import randint
from dungeon_game_maps import GAME_CHARACTERS

AVAILABLE_MOVES = {'up': (0, -1),
                   'down': (0, 1),
                   'left': (-1, 0),
                   'right': (1, 0)}

VECTORS_TO_ADJACENT_TILES = tuple(AVAILABLE_MOVES.values())

MOVE_NAMES = tuple(AVAILABLE_MOVES.keys())


def query_player_move():

    move = input(f'Where to go next? {MOVE_NAMES}: ').lower()

    while not MOVE_NAMES.count(move):
        move = input('Wrong! Try again: ').lower()

    return move


def execute_player_move(map_size, player_x, player_y, move_name):

    new_x = player_x + AVAILABLE_MOVES[move_name][0]
    new_y = player_y + AVAILABLE_MOVES[move_name][1]

    if 0 <= new_x < map_size and 0 <= new_y < map_size:
        player_x, player_y = new_x, new_y
    else:
        print('That path is blocked!')

    return player_x, player_y


def check_end_game_condition(game_map, player_x, player_y):

    is_game_running = False
    player_tile = game_map[player_y][player_x]

    if player_tile == GAME_CHARACTERS['Treasure']:
        print('You Won!')
    elif player_tile == GAME_CHARACTERS['Trap']:
        print('You Lost(')
    else:
        is_game_running = True

    return is_game_running


def output_game_state(treasures, traps):

    if treasures and traps:
        print('There is a treasure and a trap nearby!')
    elif treasures:
        print('There is a treasure nearby!')
    elif traps:
        print('There is a trap nearby!')
    else:
        print('There is nothing nearby.')


def update_game_state(game_map, player_x, player_y):

    map_size = len(game_map[0])
    treasures = 0
    traps = 0

    for vector in VECTORS_TO_ADJACENT_TILES:

        adjacent_x = player_x + vector[0]
        adjacent_y = player_y + vector[1]

        if not 0 <= adjacent_x < map_size or not 0 <= adjacent_y < map_size:
            continue

        adjacent_tile = game_map[adjacent_y][adjacent_x]

        if adjacent_tile == GAME_CHARACTERS['Treasure']:
            treasures += 1
        elif adjacent_tile == GAME_CHARACTERS['Trap']:
            traps += 1

    output_game_state(treasures, traps)


def run_game(game_map):

    map_size = len(game_map[0])
    player_x = randint(0, map_size - 1)     # TODO: Check that the player spawns on empty tiles only.
    player_y = randint(0, map_size - 1)
    is_game_running = True

    while is_game_running:

        move = query_player_move()
        player_x, player_y = execute_player_move(map_size, player_x, player_y, move)
        print(f'Your position is ({player_x}, {player_y}).')
        is_game_running = check_end_game_condition(game_map, player_x, player_y)
        update_game_state(game_map, player_x, player_y)
        # TODO: Place dots on the tiles where player has been.
