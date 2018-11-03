import logging
import os.path
import pickle


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

debug_formatter = logging.Formatter('%(asctime)s - %(name)s - %(message)s')
info_formatter = logging.Formatter('%(message)s')

file_handler = logging.FileHandler('DebugLog.txt')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(debug_formatter)

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)
stream_handler.setFormatter(info_formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)


def process_save_game(current_data):
    """
    Prompts user to enter file name to serialize his current game state using pickle

    :param tuple current_data: current game data (map,
        left treasures amount, player position and trapped state)
    """
    
    logger.debug('Entering process_save_game(current_data) function')
    
    user_input = input('Enter save file name: ')

    with open(f'{user_input}.pickle', 'wb') as save_file:
        pickle.dump(current_data, save_file)

    logger.info(f'Game saved in {user_input}.pickle')
    logger.debug('Returning from process_save_game(current_data) function')


def process_load_game():
    """
    Prompts user to enter file name to load game from

    :return: tuple with loaded game data
    :rtype: tuple
    """

    logger.debug('Entering process_load_game() function')
    current_data = ()

    while True:

        user_input = input('Enter file name: ')
        if os.path.exists(f'{user_input}.pickle'):
            break

        else:
            logger.info('No such file exists! Try again')

    with open(f'{user_input}.pickle', 'rb') as load_file:
        current_data = pickle.load(load_file)

    logger.debug('Returning from process_load_game() function')
    return current_data
