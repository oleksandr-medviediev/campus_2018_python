import pickle
from dungeon_game_maps import print_map

FILE_NAME = 'save_file.dg'

LOAD_COMMAND = 'load'
SAVE_COMMAND = 'save'


def deserialize():

    with open(FILE_NAME, 'rb') as save_file:
        data = pickle.load(save_file)

    return tuple(data)


def serialize(game_map, player_x, player_y):

    data = [game_map, player_x, player_y]

    with open(FILE_NAME, 'wb') as save_file:
        pickle.dump(data, save_file, protocol=3)
