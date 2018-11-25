import level
import game
import dungeon_game_logger
import os
import error as dungeon_game_error


def choose_option():
    """
    choose option from stdin
    :return: selected option
    :rtype: int
    """

    while True:

        option = input('1. New game\n2. Load game\nSelect option: ')

        try:
            option = int(option)
            if option != 1 and option != 2:
                raise dungeon_game_error.WrongInputDungeonGameError(f'{option}', '`1` or `2`')

            break

        except (ValueError, dungeon_game_error.WrongInputDungeonGameError) as error:
            dungeon_game_logger.logger.warning(f'{error}')
            continue

    return option


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
