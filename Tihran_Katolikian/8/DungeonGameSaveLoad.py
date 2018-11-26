from contextlib import contextmanager
import pickle
import logging
from LoggerDecorator import logger_decorator
from sys import exit
from NoSavedDataFileError import NoSavedDataFileError
from CannotSaveGameError import CannotSaveGameError


SAVE_DATA_FILENAME = 'save.data'


@logger_decorator
def save_game(player_position, dungeon_map):
    '''
    Function saves the game;
    :param player_position: position of player to save;
    :param dungeon_map: a map to save;
    :type player_position: a tuple of ints: (int, int);
    :type dungeon_map: a list of lists of DungeonCells.
    '''
    logging.debug('Method called')
    try:
        with open (SAVE_DATA_FILENAME, 'wb') as save_file:
            position_and_map = player_position, dungeon_map
            pickle.dump(position_and_map, save_file)
    except OSError as error:
        logging.critical(f'Cannot save game due to an exception: {error}.')
        raise CannotSaveGameError(SAVE_DATA_FILENAME, error)

@logger_decorator
def load_game():
    '''
    Function loads the game from a file. If there is not save data, throws 'FileNotFoundError'.
    :return: deserialized player position and dungeon map;
    :rtype: a tuple of tuple of ints: (int, int) and a list of lists of DungeonCells.
    '''
    try:
        with open (SAVE_DATA_FILENAME, 'rb') as load_file:
            return pickle.load(load_file)
    except FileNotFoundError as error:
        logging.critical(f'Can\'t read save file {SAVE_DATA_FILENAME}')
        raise NoSavedDataFileError(SAVE_DATA_FILENAME)
