import logging
import pickle
from dungeon_game_maps import game_map_to_string

FILE_NAME = 'save_file.dg'

LOAD_COMMAND = 'load'
SAVE_COMMAND = 'save'


def deserialize():
    """
    Unpickle game map and player coordinates from save file with FILE_NAME.

    :return: game_map, player_x, player_y.
    :rtype: list, int, int.
    """
    with open(FILE_NAME, 'rb') as save_file:

        logging.debug(f'Calling pickle.load("{FILE_NAME}")')
        data = pickle.load(save_file)
        logging.debug(f'Deserialized map:\n{game_map_to_string(data[0])}\nPlayer pos: ({data[1]};{data[2]})')

    return tuple(data)


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

        logging.debug(f'Calling pickle.dump(data, "{FILE_NAME}", protocol=3)')
        pickle.dump(data, save_file, protocol=3)
