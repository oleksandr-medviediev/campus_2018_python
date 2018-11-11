import pickle


SAVE_FILE = 'save.dg'


def serialize_dungeon_game(dun_map, position):
    """
    :param dun_map: game map
    :type dun_map: list[list[str]]

    :param position: position of player on the map
    :type: list[int, int]
    """

    save_file = open(SAVE_FILE, "wb")

    data = [dun_map, position]
    pickle.dump(data, save_file)
    


def deserialize_dungeon_game():
    """
    :return: game map and position of player
    :rtype: list[list[list[str]], list[int, int]]
    """

    save_file = open(SAVE_FILE, "rb")

    data = pickle.load(save_file)

    return data
