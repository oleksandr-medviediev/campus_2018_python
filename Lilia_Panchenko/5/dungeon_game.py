import game_step as gs
import pickle
from logger import m_logger


def input_player_choice():
    
    m_logger.info('Where do you want to move: ')
    player_choice = input()
    m_logger.debug(f'dungeon_game : player inputed {player_choice}')
    player_choice.casefold()

    if player_choice == 'save':
        m_logger.debug('dungeon_game : player want to save game')
        save_game()

    else:    
        DIRECTIONS = ['up', 'down', 'left', 'right']
        while not player_choice in DIRECTIONS:

            m_logger.debug('dungeon_game : player typed something wrong')
            m_logger.info("I'm sorry, I don't understand where do you want to go.\nTry once more: ")
            player_choice = input()
            m_logger.debug(f'dungeon_game : player inputed {player_choice} as new direction')
            player_choice.casefold()
            
        m_logger.debug(f'dungeon_game : success! player inputed right direction')
        return player_choice


def save_game():

    m_logger.debug(f'dungeon_game : starting game saving')
    file = open('savefile.txt', 'wb')
    m_logger.debug(f'dungeon_game : opened savefile.txt in write mode')
    to_save = (gs.get_to_save_data(), gs.player_position)
    m_logger.debug(f'dungeon_game : formed data to save')
    pickle.dump(to_save, file)
    m_logger.debug(f'dungeon_game : serialized data to file')

    file.close()
    m_logger.debug(f'dungeon_game : closed file')


def load_game():

    m_logger.debug(f'dungeon_game : starting game loading')
    file = open('savefile.txt', 'rb')
    m_logger.debug(f'dungeon_game : opened file in read mode')
    loaded = pickle.load(file)
    m_logger.debug(f'dungeon_game : loaded data')
    gs.set_loaded_data(loaded[0])
    gs.player_position = loaded[1]
    m_logger.debug(f'dungeon_game : set data to game_step module')

    file.close()
    m_logger.debug(f'dungeon_game : closed file')    


def new_game():

    m_logger.debug(f'dungeon_game : starting game initialization')
    gs.init_game()
    m_logger.debug(f'dungeon_game : game initialized')


m_logger.info("Do you want to play a new game or load old one?\nEnter your choice [N/L]:")

new_or_load = input()
m_logger.debug(f'dungeon_game : player inputed {new_or_load}')
new_or_load.casefold()

while not new_or_load in ['n', 'l']:
    m_logger.debug(f'dungeon_game : player inputed something wrong')
    m_logger.info("Try again\nEnter your choice [N/L]: ")

    new_or_load = input()
    m_logger.debug(f'dungeon_game : player inputed {new_or_load}')
    new_or_load.casefold()

m_logger.debug(f'dungeon_game : player inputed successfully')

if new_or_load == 'n':
    m_logger.debug(f'dungeon_game : player want to start new game')
    new_game()
    m_logger.debug(f'dungeon_game : new game started')

else:
    m_logger.debug(f'dungeon_game : player want to load game')
    load_game()
    m_logger.debug(f'dungeon_game : game loaded')


m_logger.info("\nWelcome to dungeon game! Let's play!\n\nYou can save your game in any time by typing 'save'\n\nRemember, you can move up, down, left or right. Your aim is to get to treasure\n")

while not gs.is_game_ended():
    
    gs.notify_player_about_traps()
    m_logger.debug(f'dungeon_game : player notified about surrounding traps')
    gs.notify_player_about_treasures()
    m_logger.debug(f'dungeon_game : player notified about surrounding treasures')

    m_logger.info(f'You are on position ({gs.player_position[1]},{gs.player_position[0]})\n')

    direction = input_player_choice()
    m_logger.debug(f'dungeon_game : player inputed next action')
    if direction != None:
        m_logger.debug(f'dungeon_game : ready to perform step')
        gs.perform_next_step(direction)
        m_logger.debug(f'dungeon_game : step performing finished')
    
gs.print_game_result()
m_logger.debug(f'dungeon_game : game result printed')
gs.print_game_map()
m_logger.debug(f'dungeon_game : game map printed')
m_logger.debug(f'dungeon_game : game ended')
