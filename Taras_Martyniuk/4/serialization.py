import pickle
from logging_defs import debug_logger as dlog


SAVE_FILE = 'save.pkl'


def save(dmap, curr_pos):
    '''
        saves current state to file
        :param dmap: dungeon map
        :param curr_pos: current tile of player
    '''
    state = (dmap, curr_pos)
    dlog.debug('Trying to save...')
    with open(SAVE_FILE, 'wb') as sf:
        pickle.dump(state, sf)
        dlog.debug('Save successfull')


def load():
    '''
        loads game state from file
        :returns: tuple (dungeon map, current position of player)
    '''
    dlog.debug('Trying to load save...')
    with open(SAVE_FILE, 'rb') as sf:
        state = pickle.load(sf)
        dlog.debug('Successfully loaded save')
        return state

