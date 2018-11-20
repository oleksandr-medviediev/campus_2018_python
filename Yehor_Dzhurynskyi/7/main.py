import level
import game
import dungeon_game_logger
import os


def choose_option():
    """
    choose option from stdin
    :return: selected option
    :rtype: int
    """

    while True:

        option = input('1. New game\n2. Load game\nSelect option: ')
        if option.isnumeric() and (int(option) == 1 or int(option) == 2):
            break

        dungeon_game_logger.logger.warning('Wrong input! It should be `1` or `2`')

    return int(option)


save_exists = os.path.isfile('save.pickable')
option = choose_option() if save_exists else 1

if option == 1:

    while True:
        size_str = input('Enter level size (N x N): ')
        if size_str.isnumeric() and int(size_str) >= 5:

            size = int(size_str)
            break

        dungeon_game_logger.logger.warning('Wrong input! It should be integer >= 5 number')

    game_level = level.Level.generate(size)

elif option == 2:
    game_level = level.Level.load()

game_process = game.Game(game_level)
game_process.loop()
game_process.on_game_finished()
