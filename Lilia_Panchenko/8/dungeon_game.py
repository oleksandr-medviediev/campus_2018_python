import pickle
import logging

from game_step import GameStep
from player import Player

from logger import debug_decorator
from logger import info_decorator
from logger import set_debug_logging
from logger import set_info_logging

from custom_exception import PlayerInputError
from custom_exception import PlayerNameError


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

        try: 
            file = open('savefile.txt', 'rb')
        except IOError:
            print("Some troubles with opening savefile.txt! Are you sure, it really exists?")

        loaded = pickle.load(file)

        self.my_game_step.set_loaded_data(loaded[0]) 
        self.my_player.name = loaded[1]
        self.my_player.position = loaded[2]

        file.close()


    @debug_decorator
    @info_decorator
    def new_game(self):

        self.my_game_step.setup_map()
        while True:

            player_name = input("Please, enter your name: ")

            try:
                if player_name in ['', '\n', 't']:
                    raise PlayerNameError(player_name)
                else:
                    break

            except PlayerNameError as error:
                logging.error(error)
                logging.info("Your name looks strange. Try again...")

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

        print(f"\nWelcome to dungeon game, {self.my_player.name}! Let's play!\n\nYou can save your game in any time by typing 'save'"+
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

while True:

    new_or_load = input("Do you want to play a new game or load old one? [(N)ew / (L)oad]: ")
    new_or_load = new_or_load.casefold()

    try:
        if new_or_load not in ['n', 'l', 'new', 'load']:
            raise PlayerInputError(new_or_load)
        else:
            break

    except PlayerInputError as error:
        logging.error(error)
        logging.info("Something wrong inputed. Try again...")

if new_or_load == 'n' or new_or_load == 'new':
    game.new_game()

else:
    game.load_game()

game.process_game()
