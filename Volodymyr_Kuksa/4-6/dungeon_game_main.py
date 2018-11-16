import logging
import logging.config
from random import randint
from dungeon_game_maps import GAME_CHARACTERS, generate_map, game_map_to_string
from dungeon_game_serialization import deserialize
from dungeon_game_logic import run_game
import dungeon_game_decorators


START_OPTIONS = ('1', '2')

logging.config.fileConfig('dungeon_game_logger.config')


@dungeon_game_decorators.log_decor
@dungeon_game_decorators.debug_decor
def query_map_size():
    """
    Query player for the size of the game map and return integer representing player's input.

    :return: game map size.
    :rtype: int.
    """
    size = input('Enter map size (5 - 20): ')

    while not size.isdigit() or not 5 <= int(size) <= 20:
        size = input('Wrong! Try again: ')

    return int(size)


@dungeon_game_decorators.log_decor
@dungeon_game_decorators.debug_decor
def query_game_load():
    """
    Query game start mode and return player input.

    :return: entered game mode.
    :rtype: str.
    """
    player_input = input('Choose option:\n1. New Game\n2. Load Game\n')

    while not START_OPTIONS.count(player_input):
        player_input = input('Wrong! Try again: ')

    return player_input


@dungeon_game_decorators.log_decor
@dungeon_game_decorators.debug_decor
def spawn_player(game_map):
    """
    Return coordinates of a random empty tile on game_map.

    :param game_map: generated game map.
    :type game_map: square 2d list of single-character strings.

    :return: x, y.
    :rtype: int, int.
    """
    map_size = len(game_map)

    x, y = randint(0, map_size - 1), randint(0, map_size - 1)

    while game_map[y][x] != GAME_CHARACTERS['Empty']:
        x, y = randint(0, map_size - 1), randint(0, map_size - 1)

    return x, y


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


@dungeon_game_decorators.log_decor
@dungeon_game_decorators.debug_decor
def main():
    """
    Entry point. Starts up and runs Dungeon Game.

    :return: None.
    """
    query_logging_mode()

    logging.info('Welcome to the Dungeon Game!')

    if query_game_load() == '2':
        dungeon_game_map, player_x, player_y = deserialize()

    else:

        size_of_map = query_map_size()
        dungeon_game_map = generate_map(size_of_map)
        player_x, player_y = spawn_player(dungeon_game_map)

    run_game(dungeon_game_map, player_x, player_y)
    logging.info(game_map_to_string(dungeon_game_map))


if __name__ == '__main__':

    try:
        main()

    except OSError as e:

        if isinstance(e, FileNotFoundError):
            logging.info('Save file not found')
        else:
            logging.error(e.strerror)
