from game_map import cell_trap
from game_map import cell_free
from game_map import cell_player
from game_map import cell_treasure


player_position = (-1, -1)


_player_move_comand = { 1:'Up', 2:'Dawn', 3:'Right', 4:'Left'}
_player_move_finctions = {
    1:lambda point: [point[0], point[1] + 1],
    2:lambda point: [point[0], point[1] - 1],
    3:lambda point: [point[0] + 1, point[1]],
    4:lambda point: [point[0] - 1, point[1]]}


def _player_input(game_map):
    global player_position

    print("Your action : ", *[f'{key} - {val},' for key, val in _player_move_comand.items()])
    move_type = int(input('-> '))

    player_position_new = _player_move_finctions[move_type](player_position)
    cell_type = game_map[player_position_new[1]][player_position_new[0]]

    result = True
    if cell_type == cell_treasure or cell_type == cell_trap:
        result = False
    else:
        game_map[player_position[1]][player_position[0]] = cell_free
        player_position = player_position_new
        game_map[player_position[1]][player_position[0]] = cell_player
    
    return result


def _spell_game_state(game_map):
    global player_position

    for val in _player_move_finctions.values():
        player_neighbored_point = val(player_position)
        if game_map[player_neighbored_point[1]][player_neighbored_point[0]] == cell_trap:
            print('Trap is near')
        elif game_map[player_neighbored_point[1]][player_neighbored_point[0]] == cell_treasure:
            print('Treasure is near')


def loop(game_map):
    global player_position

    while _player_input(game_map):
        _spell_game_state(game_map)
    
    cell_type = game_map[player_position[1]][player_position[0]]
    if cell_type == cell_treasure :
        print('You WON!')
    else:
        print('You lose...')