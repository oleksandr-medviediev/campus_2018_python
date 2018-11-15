import pickle
import dungeon_game_decorators

FILE_NAME = 'save_file.dg'

LOAD_COMMAND = 'load'
SAVE_COMMAND = 'save'


@dungeon_game_decorators.log_decor
@dungeon_game_decorators.debug_decor
def deserialize():
    """
    Unpickle game map and player coordinates from save file with FILE_NAME.

    :return: game_map, player_x, player_y.
    :rtype: list, int, int.
    """
    with open(FILE_NAME, 'rb') as save_file:
        data = pickle.load(save_file)

    return tuple(data)


@dungeon_game_decorators.log_decor
@dungeon_game_decorators.debug_decor
def serialize(game_map, player_x, player_y):
    """
    Pickle game_map, player_x, player_y into a save file with FILE_NAME.

    :param game_map: generated game map.
    :type game_map: square 2d list of single-character strings.

    :param player_x: x coordinate of the player.
    :type player_x: int.

    :param player_y: y coordinate of the player.
    :type player_y: int.

    :return: None.
    """
    data = [game_map, player_x, player_y]

    with open(FILE_NAME, 'wb') as save_file:
        pickle.dump(data, save_file, protocol=3)
