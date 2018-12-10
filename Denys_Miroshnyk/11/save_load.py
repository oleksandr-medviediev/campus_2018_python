from pickle import Pickler
from pickle import load
from os.path import isfile
from custom_logger import logger as log


def save_game(current_map):
    """saves game to "save.txt"

    Arguments:
        current_map {list} -- current game map state
    """
    try:
        file = open("save.txt", 'rb')
    except IOError:
        log.info("unable to save game")
    else:
        Pickler(file).dump(current_map)
        log.info("game saved!")


def load_game():
    """loads game map if file "save.txt" exists 

    Returns:
        list -- saved game map
    """
    try:
        file = open("save.txt", 'rb')
    except IOError:
        log.info("unable to load game")
    else:
        save = load(file)

        log.info("game loaded")
        return save
