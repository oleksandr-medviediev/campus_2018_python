import math
import random
import level
import logging
import dungeon_game_logger
from dungeon_game_logger import debug_decorator
from dungeon_game_logger import log_decorator


MOVES = {
    'left': (-1, 0),
    'right': (1, 0),
    'up': (0, -1),
    'down': (0, 1)
}


@debug_decorator
@log_decorator('offering moves to player...', logging.INFO)
def offer_moves(lvl, player_x, player_y):
    """
    offer player to do move
        :param str lvl: string representation of level
        :param int player_x: current x-position of player
        :param int player_y: current y-position of player
        :return: delta x, y coords
        :rtype: tuple
    """

    lvl_size = level.size(lvl)

    up_cell = level.get_cell(lvl, player_x, player_y - 1)
    down_cell = level.get_cell(lvl, player_x, player_y + 1)
    left_cell = level.get_cell(lvl, player_x - 1, player_y)
    right_cell = level.get_cell(lvl, player_x + 1, player_y)

    message = f'\n# - wall (dead end)\n$ - treasure\n! - trap\n_ - empty space\np - player\n'
    env_message = '\n{:^3}\n{}p{}\n{:^3}\n'.format(up_cell, left_cell, right_cell, down_cell)

    dungeon_game_logger.logger.info(message)

    if up_cell == '!' or down_cell == '!' or left_cell == '!' or right_cell == '!':
        dungeon_game_logger.logger.info('Trap somewhere!')

    if up_cell == '$' or down_cell == '$' or left_cell == '$' or right_cell == '$':
        dungeon_game_logger.logger.info('Treasure somewhere!')

    dungeon_game_logger.logger.info(env_message)

    while True:

        move = input('Enter your move (`left`, `right`, `up`, `down` or `save`): ')

        if move == 'save':
            level.save(lvl, player_x, player_y)
        elif move not in MOVES:
            dungeon_game_logger.logger.warn('Wrong input! It should be one of this: `left`, `right`, `up`, `down`')
        else:
            break

    return MOVES[move]


@debug_decorator
@log_decorator('Main game loop started...', logging.INFO)
def loop(lvl, player_x, player_y):
    """
    main loop of dungeon game
        :param str lvl: string representation of level
        :param int player_x: initial x-position of player
        :param int player_y: initial y-position of player
        :return: last player position
        :rtype: tuple
    """

    while True:

        dx, dy = offer_moves(lvl, player_x, player_y)
        destination_cell = level.get_cell(lvl, player_x + dx, player_y + dy)

        if destination_cell == '#':

            dungeon_game_logger.logger.info('Can\'t move in this way\n')
            continue

        player_x += dx
        player_y += dy

        if destination_cell == '!':

            dungeon_game_logger.logger.info('You fell into trap, GAME OVER =<')
            break
        elif destination_cell == '$':

            dungeon_game_logger.logger.info('You found a treasure, VICTORY!')
            break

    return player_x, player_y


@debug_decorator
@log_decorator('spawning player...', logging.INFO)
def spawn_player(lvl):
    """
    reserve valid location for player on level
        :param str lvl: string representation of level
        :return: x and y coord of spawned player
        :rtype: tuple
    """

    lvl_size = level.size(lvl)
    while True:

        cell_pos = random.randint(0, len(lvl) - 1)
        if lvl[cell_pos] == '_':

            player_x, player_y = cell_pos % lvl_size, cell_pos // lvl_size
            break

    return player_x, player_y
