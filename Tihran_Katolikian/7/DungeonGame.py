from enum import Enum
from UpdateList import UpdateList
from Character import Character
from LoggerDecorator import logger_decorator
import logging
from DungeonMap import DungeonMap
import DungeonGameConfig
import DungeonGameSaveLoad


class GameStartMode(Enum):
    NEW_GAME = 0
    LOAD_GAME = 1


class DungeonGameState(Enum):
    GAME_MENU = 0
    GAMEPLAY = 1


class DungeonGame:

    def __init__(self):
        '''
        Constructor of DungeonGame.
        :param game_start_mode: the way how game should start.
        :type game_start_mode: GameStartMode
        '''
        self.__dungeon_map = DungeonMap()
        self.__character = None
        self.__game_start_mode = None
        self.__current_game_state = DungeonGameState.GAME_MENU

        self.__text_to_menu = {
            'new game' : GameStartMode.NEW_GAME,
            'load' : GameStartMode.LOAD_GAME
        }

        self.__update_list = UpdateList()


    @logger_decorator
    def should_run(self):
        '''
        Function is used to undestand if game should continue.
        :return: True if should, False otherwise;
        :rtype: bool.
        '''
        player_is_alive = self.__character.is_alive()
        player_collected_all_treasures = self.__character.get_treasures_number() is\
        DungeonGameConfig.NUMBER_OF_TREASURES_TO_WIN

        return player_is_alive and not player_collected_all_treasures

    
    @logger_decorator
    def process_game_start(self):
        '''
        Function is used to process game start. It is an equivalent of menu in normal games.
        :return: a function that player have chosen in menu;
        :rtype: StartMenu.
        '''
        while True:
            logging.info('Type \'new game\' to start a new game or \'load\' to old game from save: ')
            input_command = input()
            if input_command in self.__text_to_menu.keys():
                break
        self.__game_start_mode = self.__text_to_menu[input_command]


    @logger_decorator
    def run_game(self):
        '''
        This method implements a single game frame.
        It will work depends on 
        '''
        if self.__current_game_state is DungeonGameState.GAME_MENU:
            if self.__game_start_mode is GameStartMode.LOAD_GAME:
                player_position, dungeon_map = DungeonGameSaveLoad.load_game()
                self.__dungeon_map.init_from_load(player_position, dungeon_map)
            else:
                map_size = int(input('Map size (>= 5): '))
                self.__dungeon_map.generate_new_map(map_size)

            self.__character = Character('User', DungeonGameConfig.PLAYER_HP, self.__dungeon_map)
            self.__current_game_state = DungeonGameState.GAMEPLAY
            self.__update_list.add_children(self.__dungeon_map, self.__character)

        elif self.__current_game_state is DungeonGameState.GAMEPLAY:
            logging.info(f'Current character stats: hp - {self.__character.get_hp()}, num of treasures - \
            {self.__character.get_treasures_number()}')
            self.__update_list.update()
