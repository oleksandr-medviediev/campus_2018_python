import pickle


SAVE_FILE = 'save.dg'


def serialize_dungeon_game(game):
    """
    :param game: game to serialize
    :type game: Game class
    """

    save_file = open(SAVE_FILE, "wb")

    pickle.dump(game, save_file)
    


def deserialize_dungeon_game():
    """
    :return: deserialized game
    :rtype: class Game
    """

    save_file = open(SAVE_FILE, "rb")

    data = pickle.load(save_file)

    return data
