from UpdateList import UpdateList
import DungeonGameSaveLoad
from enum import Enum
from LoggerDecorator import logger_decorator
import logging
from DungeonMap import DungeonCell
import DungeonGameConfig


class PlayerCommand(Enum):
    UP = 0
    LEFT = 1
    DOWN = 2
    RIGHT = 3
    SAVE = 4


class Character(UpdateList):
    def __init__(self, name, hp, dungeon_map):
        '''
        Constructor of a character class.
        :param name: a name of character;
        :param hp: a start number of health points of a character;
        :param dungeon_map: a map for dungeon game that will be used by character to move;
        :type name: str;
        :type hp: int;
        :type dungeon_map: DungeonMap;
        '''
        super().__init__()
        self.name = name
        self.__hp = hp
        self.__treasures_number = 0
        self.__dungeon_map = dungeon_map
        self.__position = dungeon_map.get_player_position()
        self.__move_commands = (
            PlayerCommand.UP,
            PlayerCommand.LEFT,
            PlayerCommand.DOWN,
            PlayerCommand.RIGHT
        )
        self.__text_to_command = {
            'w' : PlayerCommand.UP,
            'a' : PlayerCommand.LEFT,
            's' : PlayerCommand.DOWN,
            'd' : PlayerCommand.RIGHT,
            'save' : PlayerCommand.SAVE
        }
        self.__direction_to_vector = {
            PlayerCommand.UP : (-1, 0),
            PlayerCommand.LEFT : (0, -1),
            PlayerCommand.DOWN: (1, 0),
            PlayerCommand.RIGHT: (0, 1)
        }


    def get_hp(self):
        '''
        Returns current hp.
        :return: current hp;
        :rtype: int.
        '''
        return self.__hp


    def is_alive(self):
        '''
        Function is used to know if character is alive.
        :return: True if alive, False if dead;
        :rtype: bool.
        '''
        return self.__hp > 0


    def get_treasures_number(self):
        '''
        Function is used to get a number of treasures for player.
        :return: a number of treasures;
        :rtype: int
        '''
        return self.__treasures_number

    
    @logger_decorator
    def __get_player_command(self):
        '''
        Function is used get the user's input;
        :param position: a position on map;
        :param map_size: a size of map;
        :return: a user's command;
        :type map_size: int;
        :type position: a tuple of 2 ints;
        :rtype: str
        '''
        while True:
            logging.info('Please, input your command. Use "w", "a", "s", "d" and "save" commands: ')
            input_command = input()
            logging.debug(f'User command is:{input_command}')
            if input_command in self.__text_to_command.keys():
                command = self.__text_to_command[input_command]

                map_size = self.__dungeon_map.get_size()

                if command in self.__move_commands:
                    can_go_there = True
                    x, y = self.__position
                    if command is PlayerCommand.UP and x is 0:
                        can_go_there = False
                    elif command is PlayerCommand.DOWN and x is map_size - 1:
                        can_go_there = False
                    elif command is PlayerCommand.LEFT and y is 0:
                        can_go_there = False
                    elif command is PlayerCommand.RIGHT and y is map_size - 1:
                        can_go_there = False

                    if not can_go_there:
                        logging.debug('User can\'t go in direction')
                        logging.info('Unfortunately you can\'t go there. Try again.')
                        continue

                return command
            else:
                logging.info('Wrong input. Try again.')


    def update(self):
        super().update()
        player_command = self.__get_player_command()
        if player_command in self.__move_commands:
            old_x, old_y = self.__position

            sum_vectors = lambda a, b: (a[0] + b[0], a[1] + b[1])

            self.__position = sum_vectors(self.__position, self.__direction_to_vector[player_command])
            
            current_cell = self.__dungeon_map.move_player(self.__position)

            if current_cell is DungeonCell.TREASURE:
                logging.info('You got 1 treasure! Gratz! :)')
                self.__treasures_number += 1
                if self.__treasures_number is DungeonGameConfig.NUMBER_OF_TREASURES_TO_WIN:
                    logging.info('Congratulations! You won!')
                
            elif current_cell is DungeonCell.TRAP:
                logging.info('You lose 1 HP!')
                self.__hp -= 1
                if self.__hp is 0:
                    logging.info('You lost:(')
            else:
                logging.info('You found nothing. Keep exploring the map!:)')

        else:
            DungeonGameSaveLoad.save_game(self.__position, self.__dungeon_map.dungeon_map)
            logging.debug('Game if saved.')
            logging.info('Game is saved.')
