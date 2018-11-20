from game_step import GameStep
import pickle
from player import Player

from logger import debug_decorator
from logger import info_decorator
from logger import set_debug_logging
from logger import set_info_logging


class DungeonGame:

    def __init__(self):
        self.my_game_step = GameStep()
        self.my_player = Player()


    @debug_decorator
    @info_decorator
    def save_game(self):

        file = open('savefile.txt', 'wb')
        to_save = (self.my_game_step.get_to_save_data(), self.my_player.name, self.my_player.position)

        pickle.dump(to_save, file)

        file.close()


    @debug_decorator
    @info_decorator
    def load_game(self):

        file = open('savefile.txt', 'rb')
        loaded = pickle.load(file)

        self.my_game_step.set_loaded_data(loaded[0]) 
        self.my_player.name = loaded[1]
        self.my_player.position = loaded[2]

        file.close()


    @debug_decorator
    @info_decorator
    def new_game(self):

        self.my_game_step.setup_map()
        player_name = input("Please, enter your name: ")
        self.my_player.set_player_name(player_name)
        self.my_player.spawn_player(self.my_game_step.my_game_map)


    @debug_decorator
    @info_decorator
    def is_game_ended(self):

        game_ended = False

        if self.my_player.islost:
            game_ended = True
            print("Sorry! You lost this game!")

        if self.my_player.iswon:
            game_ended = True
            print("Congratulations! You won this game!")

        return game_ended


    @debug_decorator
    @info_decorator
    def process_game(self):

        print("\nWelcome to dungeon game! Let's play!\n\nYou can save your game in any time by typing 'save'"+
            "\n\nRemember, you can move up, down, left or right. Your aim is to get to treasure\n")

        while not self.is_game_ended():
            
            self.my_game_step.notify_player_about_traps(self.my_player.position)
            self.my_game_step.notify_player_about_treasures(self.my_player.position)

            print(f'You are on position ({self.my_player.position[1]}, {self.my_player.position[0]})\n')

            direction = self.my_player.input_direction()

            if direction == 'save':
                self.save_game()
            elif direction == 'exit':
                exit()
            else:
                self.my_game_step.perform_next_step(direction, self.my_player)
            
        self.my_game_step.print_game_result(self.my_player)
        self.my_game_step.print_game_map(self.my_player.position)


set_debug_logging()
set_info_logging()

game = DungeonGame()

new_or_load = input("Do you want to play a new game or load old one?\nEnter your choice [new / load]: ")
new_or_load = new_or_load.casefold()

while new_or_load not in ['n', 'l', 'new', 'load']:
    
    new_or_load = input("Try again\nEnter your choice [new / load]: ")
    new_or_load = new_or_load.casefold()

if new_or_load == 'n' or new_or_load == 'new':
    game.new_game()

else:
    game.load_game()

game.process_game()
