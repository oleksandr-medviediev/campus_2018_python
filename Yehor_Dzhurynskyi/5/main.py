import level
import dungeon_game
import os


def choose_option():

    while True:

        option = input('1. New game\n2. Load game\nSelect option: ')
        if option.isnumeric() and (int(option) == 1 or int(option) == 2):
            break

        print('Wrong input! It should be `1` or `2`')

    return int(option)


save_exists = os.path.isfile('save.pickable')
option = choose_option() if save_exists else 1

if option == 1:

    while True:
        size_str = input('Enter level size (N x N): ')
        if size_str.isnumeric() and int(size_str) >= 5:

            size = int(size_str)
            break

        print('Wrong input! It should be integer >= 5 number')

    lvl = level.generate_level(size)
    lvl_is_valid = level.validate(lvl)

    player_x, player_y = dungeon_game.spawn_player(lvl)

elif option == 2:
    lvl, player_x, player_y = level.load()

player_x, player_y = dungeon_game.loop(lvl, player_x, player_y)

level.print_level(lvl, player_x, player_y)
