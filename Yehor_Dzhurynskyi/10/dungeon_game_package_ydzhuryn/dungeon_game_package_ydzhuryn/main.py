import os
import pickle
from . import game
from . import level
from . import dungeon_game_logger
from . import dungeon_game_error


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

def create_new_game():
    """
    creates new dungeon game
    :return: generated level of selected size
    :rtype: Level
    """

    while True:

        level_size = input('Enter level size (N x N): ')

        try:
            level_size = int(level_size)

            if level_size < 5:
                raise dungeon_game_error.WrongInputDungeonGameError(f'{level_size}', '>= 5 integer')

            break

        except (ValueError, dungeon_game_error.WrongInputDungeonGameError) as error:
            dungeon_game_logger.logger.warning(f'{error}')
            continue

    return level.Level.generate(level_size)

def run():
    option = choose_option()

    if option == 1:
        game_level = create_new_game()
    elif option == 2:

        try:
            game_level = level.Level.load()

        except (FileNotFoundError, pickle.UnpicklingError) as error:
            dungeon_game_logger.logger.warning(f'{error}')
            game_level = create_new_game()

    game_process = game.Game(game_level)
    game_process.loop()
    game_process.on_game_finished()
