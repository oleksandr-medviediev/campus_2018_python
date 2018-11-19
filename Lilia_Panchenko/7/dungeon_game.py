import game_step
import pickle
import player

from logger import debug_decorator
from logger import info_decorator
from logger import set_debug_logging


class DungeonGame:

    def __init__():
        print('ok')
        self.my_game_step = GameStep()

    @debug_decorator
    @info_decorator
    def save_game():

        file = open('savefile.txt', 'wb')
        to_save = (my_game_step.get_to_save_data(), my_player.position)

        pickle.dump(to_save, file)

        file.close()


    @debug_decorator
    @info_decorator
    def load_game():

        file = open('savefile.txt', 'rb')
        loaded = pickle.load(file)

        my_game_step.set_loaded_data(loaded[0]) 
        my_game_step.player_position = loaded[1]

        file.close()


    @debug_decorator
    @info_decorator
    def new_game():
        my_game_step.init_game()


    @debug_decorator
    @info_decorator
    def is_game_ended():

        game_ended = False

        if my_player.islost:
            game_ended = True
            print("Sorry! You lost this game!")

        if my_player.iswon:
            game_ended = True
            print("Congratulations! You won this game!")


    @debug_decorator
    @info_decorator
    def process_game():

        print("\nWelcome to dungeon game! Let's play!\n\nYou can save your game in any time by typing 'save'\n\nRemember, you can move up, down, left or right. Your aim is to get to treasure\n")
        player_name = input("Please, enter your name: ")

        my_player = Player(player_name, my_game_step.get_map())

        while not is_game_ended():
            
            my_game_step.notify_player_about_traps()
            my_game_step.notify_player_about_treasures()

            print(f'You are on position ({my_game_step.player_position[1]},{my_game_step.player_position[0]})\n')

            direction = my_player.input_player_choice()
            if direction != None:
                my_game_step.perform_next_step(direction)
            
        my_game_step.print_game_result()
        my_game_step.print_game_map()


print('ok3')
game = DungeonGame()
game.init_game()

set_debug_logging()

new_or_load = input("Do you want to play a new game or load old one?\nEnter your choice [N / L]:")
new_or_load = new_or_load.casefold()

while new_or_load not in ['n', 'l']:
    
    new_or_load = input("Try again\nEnter your choice [N / L]: ")
    new_or_load = new_or_load.casefold()

if new_or_load == 'n':
    game.new_game()

else:
    game.load_game()

game.process_game()
