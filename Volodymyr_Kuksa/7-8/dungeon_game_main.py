import logging.config
from dungeon_game import DungeonGame
import dungeon_game_decorators
import dungeon_game_exceptions

logging.config.fileConfig('dungeon_game_logger.config')


@dungeon_game_decorators.log_decor
@dungeon_game_decorators.debug_decor
def query_logging_mode():
    """
    Query logging mode and set corresponding global variable.

    :return: None.
    """
    mode = input('Select logging mode:\n1. Debug\n2. Useful\n3. Both\n(press 1-3 or any key to skip)\n')

    try:
        mode = int(mode)
    except ValueError as error:
        logging.error(error)
        logging.info('Default logging mode is set')
    else:

        if mode == 1 or mode == 3:
            dungeon_game_decorators.mode_debug = True
        if mode == 2 or mode == 3:
            dungeon_game_decorators.mode_log = True


if __name__ == '__main__':

    query_logging_mode()

    game = DungeonGame()

    try:
        game.run_game()
    except dungeon_game_exceptions.DungeonGameError as error:
        logging.error(error)
    finally:
        game.on_game_end()
