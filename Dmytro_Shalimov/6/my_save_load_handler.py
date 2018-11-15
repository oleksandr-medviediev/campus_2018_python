import logging
from my_decorator import log_wrapper, debug_wrapper
import os.path
import pickle


@log_wrapper
@debug_wrapper
def process_save_game(current_data):
    """
    Prompts user to enter file name to serialize his current game state using pickle

    :param tuple current_data: current game data (map,
        left treasures amount, player position and trapped state)
    """
    
    user_input = input('Enter save file name: ')

    with open(f'{user_input}.pickle', 'wb') as save_file:
        pickle.dump(current_data, save_file)

    print(f'Game saved in {user_input}.pickle')  


@log_wrapper
@debug_wrapper
def process_load_game():
    """
    Prompts user to enter file name to load game from

    :return: tuple with loaded game data
    :rtype: tuple
    """

    current_data = ()

    while True:

        user_input = input('Enter file name: ')
        if os.path.exists(f'{user_input}.pickle'):
            break

        else:
            print('No such file exists! Try again')

    with open(f'{user_input}.pickle', 'rb') as load_file:
        current_data = pickle.load(load_file)

    return current_data
