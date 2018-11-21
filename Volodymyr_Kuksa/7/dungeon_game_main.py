import logging.config
from dungeon_game import DungeonGame
import dungeon_game_decorators

logging.config.fileConfig('dungeon_game_logger.config')


@dungeon_game_decorators.log_decor
@dungeon_game_decorators.debug_decor
def query_logging_mode():
    """
    Query logging mode and set corresponding global variable.

    :return: None.
    """
    mode = input('Select logging mode:\n1. Debug\n2. Useful\n3. Both\n(press 1-3 or any key to skip)\n')

    if not mode.isdigit():
        return

    mode = int(mode)

    if mode == 1 or mode == 3:
        dungeon_game_decorators.mode_debug = True
    if mode == 2 or mode == 3:
        dungeon_game_decorators.mode_log = True


if __name__ == '__main__':

    query_logging_mode()

    game = DungeonGame()

    game.run_game()
