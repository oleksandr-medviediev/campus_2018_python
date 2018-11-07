from dg_logging import DG_loger as log
from game_map import cell_trap
from game_map import cell_free
from game_map import cell_player
from game_map import cell_treasure
from IO import game_save


player_position = [-1, -1]


_player_move_comand = { 1:'Up', 2:'Dawn', 3:'Right', 4:'Left', 5:'Save game'}
_player_move_finctions = {
    1:lambda point: [point[0], point[1] + 1],
    2:lambda point: [point[0], point[1] - 1],
    3:lambda point: [point[0] + 1, point[1]],
    4:lambda point: [point[0] - 1, point[1]]}


def _player_input(game_map):
    log.debug(f'_player_input function was caled')
    global player_position

    log.info(f"Your action : {[f'{key} - {val},' for key, val in _player_move_comand.items()]}")
    action_type = int(input('-> '))

    result = True
    log.debug(f'_player_input: players action is {_player_move_comand[action_type]}')
    if action_type == 5:
        game_save(game_map)
    else:
        player_position_new = _player_move_finctions[action_type](player_position)
        cell_type = game_map[player_position_new[1]][player_position_new[0]]

        if cell_type == cell_treasure or cell_type == cell_trap:
            log.debug(f'_player_input: player is find a {cell_type}')
            result = False
        else:
            game_map[player_position[1]][player_position[0]] = cell_free
            player_position = player_position_new
            game_map[player_position[1]][player_position[0]] = cell_player
            log.debug(f'_player_input: players new position is x = {player_position[0]}, y = {player_position[1]}')
    
    return result


def _spell_game_state(game_map):
    log.debug(f'_spell_game_state function was called')
    global player_position

    for val in _player_move_finctions.values():
        player_neighbored_point = val(player_position)
        if game_map[player_neighbored_point[1]][player_neighbored_point[0]] == cell_trap:
            log.info('Trap is near')
        elif game_map[player_neighbored_point[1]][player_neighbored_point[0]] == cell_treasure:
            log.info('Treasure is near')


def loop(game_map):
    log.debug(f'loop function was called')
    global player_position

    _spell_game_state(game_map)
    while _player_input(game_map):
        log.debug(f'loop: game loop is running')
        _spell_game_state(game_map)
    
    log.debug(f'loop: game loop was stoped')
    cell_type = game_map[player_position[1]][player_position[0]]
    if cell_type == cell_treasure :
        log.info('You WON!')
    else:
        log.info('You lose...')