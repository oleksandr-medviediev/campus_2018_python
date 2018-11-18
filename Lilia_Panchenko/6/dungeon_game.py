import game_step as gs
import pickle
from logger import debug_decorator
from logger import info_decorator
from logger import set_debug_logging


@debug_decorator
@info_decorator
def input_player_choice():
    
    print('Where do you want to move: ')
    player_choice = input()
    player_choice.casefold()

    if player_choice == 'save':
        save_game()

    else:    
        DIRECTIONS = ['up', 'down', 'left', 'right']
        while not player_choice in DIRECTIONS:

            print("I'm sorry, I don't understand where do you want to go.\nTry once more: ")
            player_choice = input()
            player_choice.casefold()

        return player_choice


@debug_decorator
@info_decorator
def save_game():

    file = open('savefile.txt', 'wb')
    to_save = (gs.get_to_save_data(), gs.player_position)

    pickle.dump(to_save, file)

    file.close()


@debug_decorator
@info_decorator
def load_game():

    file = open('savefile.txt', 'rb')
    loaded = pickle.load(file)

    gs.set_loaded_data(loaded[0])
    gs.player_position = loaded[1]

    file.close()


@debug_decorator
@info_decorator
def new_game():
    gs.init_game()


set_debug_logging()

print("Do you want to play a new game or load old one?\nEnter your choice [N/L]:")

new_or_load = input()
new_or_load = new_or_load.casefold()

while new_or_load not in ['n', 'l']:
    print(new_or_load)
    new_or_load = input("Try again\nEnter your choice [N / L]: ")
    new_or_load = new_or_load.casefold()

if new_or_load == 'n':
    new_game()

else:
    load_game()


print("\nWelcome to dungeon game! Let's play!\n\nYou can save your game in any time by typing 'save'\n\nRemember, you can move up, down, left or right. Your aim is to get to treasure\n")

while not gs.is_game_ended():
    
    gs.notify_player_about_traps()
    gs.notify_player_about_treasures()

    print(f'You are on position ({gs.player_position[1]},{gs.player_position[0]})\n')

    direction = input_player_choice()
    if direction != None:
        gs.perform_next_step(direction)
    
gs.print_game_result()
gs.print_game_map()