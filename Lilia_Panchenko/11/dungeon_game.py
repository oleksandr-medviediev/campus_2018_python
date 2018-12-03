import pickle
import logging

from game_step import GameStep
from player import Player

from logger import my_logger

from custom_exception import PlayerInputError
from custom_exception import PlayerNameError

from enemy import Enemy
from thread_enemy import EnemyThread


class DungeonGame:
    """
    Class to process game. Responsible for saving, loading and creating new game. Also to check game finished condition and 
    run game cycle.
    """ 

    def __init__(self):
        """
        Constructor for DungeonGame class
        """
        self.my_game_step = GameStep()
        self.my_player = Player()
        self.my_enemy = Enemy()


    @my_logger.debug_decorator
    @my_logger.info_decorator
    def save_game(self):
        """
        Function to save game
        : return : None
        """
        file = open('savefile.txt', 'wb')
        to_save = (self.my_game_step.get_to_save_data(), self.my_player.name, self.my_player.position,
        self.my_enemy.position)

        pickle.dump(to_save, file)

        file.close()


    @my_logger.debug_decorator
    @my_logger.info_decorator
    def load_game(self):
        """
        Function to load game
        : return : None
        """   
        try: 
            file = open('savefile.txt', 'rb')
        except IOError as error:
            logging.error(error)
            logging.info("Some troubles with opening savefile.txt! Are you sure, it really exists?")

        loaded = pickle.load(file)

        self.my_game_step.set_loaded_data(loaded[0]) 
        self.my_player.name = loaded[1]
        self.my_player.position = loaded[2]
        self.my_enemy.position = loaded[3]

        file.close()


    @my_logger.debug_decorator
    @my_logger.info_decorator
    def new_game(self):
        """
        Function to create new game. Initializes game step, player and enemy
        : return : None
        """
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
        self.my_enemy.spawn(self.my_game_step.my_game_map)


    @my_logger.debug_decorator
    @my_logger.info_decorator
    def is_game_ended(self):
        """
        Function to check if game ended
        : return : game_ended flag. True if game ended, False otherwise
        : rtype : bool
        """
        game_ended = False

        if self.my_player.islost:
            game_ended = True
            print("Sorry! You lost this game!")

        if self.my_player.iswon:
            game_ended = True
            print("Congratulations! You won this game!")

        return game_ended


    @my_logger.debug_decorator
    @my_logger.info_decorator
    def process_game_cycle(self):
        """
        Function to run game cycle
        : return : None
        """
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
                self.my_game_step.perform_next_step(direction, self.my_player, self.my_enemy)
            
        self.my_game_step.print_game_result(self.my_player)
        self.my_game_step.print_game_map(self.my_player.position)


    @my_logger.debug_decorator
    @my_logger.info_decorator
    def start(self):    
        """
        Function to start game. Call to start all processes
        : return : None
        """
        my_logger.set_debug_logging()
        my_logger.set_info_logging()

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
            self.new_game()

        else:
            self.load_game()

        enemy_move_thread = EnemyThread(1, "Enemy_Move_Thread", self.my_enemy, self.my_game_step.my_game_map.mapsize)
        enemy_move_thread.start()
        self.process_game_cycle()
