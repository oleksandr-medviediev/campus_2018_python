import math
import random
import level

MOVES = {
    'left': (-1, 0),
    'right': (1, 0),
    'up': (0, -1),
    'down': (0, 1)
}


def offer_moves(lvl, player_x, player_y):

    lvl_size = level.size(lvl)

    up_cell = level.get_cell(lvl, player_x, player_y - 1)
    down_cell = level.get_cell(lvl, player_x, player_y + 1)
    left_cell = level.get_cell(lvl, player_x - 1, player_y)
    right_cell = level.get_cell(lvl, player_x + 1, player_y)

    message = f'# - wall (dead end)\n$ - treasure\n! - trap\n_ - empty space\np - player\n'
    move_message = '{:^3}\n{}p{}\n{:^3}\n'.format(up_cell, left_cell, right_cell, down_cell)

    print(message)
    print(move_message)

    while True:

        move = input('Enter your move (`left`, `right`, `up`, `down`): ')
        if move not in MOVES:

            print('Wrong input! It should be one of this: `left`, `right`, `up`, `down`')
            continue

        break

    return MOVES[move]


def loop(lvl, player_x, player_y):

    while True:

        dx, dy = offer_moves(lvl, player_x, player_y)
        destination_cell = level.get_cell(lvl, player_x + dx, player_y + dy)

        if destination_cell == '#':

            print('Can\'t move in this way\n')
            continue

        player_x += dx
        player_y += dy

        if destination_cell == '!':

            print('You fell into trap, GAME OVER =<')
            break
        elif destination_cell == '$':

            print('You found a treasure, VICTORY!')
            break

    return player_x, player_y


def spawn_player(lvl):

    lvl_size = level.size(lvl)
    while True:

        cell_pos = random.randint(0, len(lvl) - 1)
        if lvl[cell_pos] == '_':

            player_x, player_y = cell_pos % lvl_size, cell_pos // lvl_size
            break

    return player_x, player_y
