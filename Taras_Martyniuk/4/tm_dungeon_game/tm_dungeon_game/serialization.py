import pickle
from logging_decors import log_decor
from os.path import isfile


SAVE_FILE = 'save.pkl'

@log_decor
def save_exists():
    '''
        True if save_file exists on distk
    '''
    return isfile(SAVE_FILE)


@log_decor
def save(player, curr_pos):
    '''
        saves current state to file
        :param player: Player
        :param curr_pos: current tile of player
    '''
    state = (player, curr_pos)
    with open(SAVE_FILE, 'wb') as sf:
        pickle.dump(state, sf)


@log_decor
def load():
    '''
        loads game state from file
        :returns: tuple (DungeonMap, Player)
    '''
    with open(SAVE_FILE, 'rb') as sf:
        state = pickle.load(sf)
        return state
