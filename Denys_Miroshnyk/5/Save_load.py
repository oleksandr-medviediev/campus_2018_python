from pickle import Pickler
from pickle import load
from os.path import isfile


def save_game(current_map):
    """saves game to "save.txt"

    Arguments:
        current_map {list} -- current game map state
    """

    Pickler(open("save.txt", 'wb')).dump(current_map)
    print("game saved!")


def load_game():
    """loads game map if file "save.txt" exists 

    Returns:
        list -- saved game map
    """

    if isfile("save.txt"):
        save = load(open("save.txt", 'rb'))
        return save
    else:
        print("unable to load game")
