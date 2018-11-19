from pickle import Pickler
from pickle import load
from os.path import isfile
from Custom_logger import logger as log
from Logger_decorator import debug_log_decorator


@debug_log_decorator
def save_game(current_map):
    """saves game to "save.txt"

    Arguments:
        current_map {list} -- current game map state
    """

    Pickler(open("save.txt", 'wb')).dump(current_map)
    log.info("game saved!")


@debug_log_decorator
def load_game():
    """loads game map if file "save.txt" exists 

    Returns:
        list -- saved game map
    """

    if isfile("save.txt"):
        save = load(open("save.txt", 'rb'))
        log.info("game loaded")
        return save
    else:
        log.info("unable to load game")
