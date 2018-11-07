import game
import dg_logging
import game_map as gmap

from IO import game_load
from dg_logging import DG_loger as log


g_map = []


def new_game():
    global g_map
    log.debug('new_game function was called')
    g_map = gmap.new_map()
    game.player_position = gmap.fill_free_cell(g_map, gmap.cell_player)


def saved_game():
    global g_map
    log.debug('saved_game function was called')
    g_map = game_load()
    game.player_position = gmap.find_player_position(g_map)


while (True):
    log.debug('Main loop')
    player_answer = input("Start the Game? y/n : ")
    log.debug(f'Player amsver to "Start the Game? y/n : " is {player_answer}')

    if player_answer == 'y':
        player_answer = input('(1) new game or (2) saved game : ')
        log.debug(f'Player amsver to "(1) new game or (2) saved game : " is {player_answer}')

        if player_answer == '1':
            new_game()
        elif player_answer == '2':
            saved_game()
        else:
            #To 'Start the Game?'
            log.info('incorect input')
            continue

        #Game logic
        game.loop(g_map)

        #End game
        log.info(f'You {gmap.cell_player} at position {game.player_position}')
        log.info(f'Treasure {gmap.cell_treasure}')
        log.info(f'Trap {gmap.cell_trap}')
        for line in g_map[::-1]:
            log.info(''.join(line))

    else:
        break
