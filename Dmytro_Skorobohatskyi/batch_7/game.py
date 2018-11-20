import constants
from level_map import LevelMap
from player import Player
from random import randint
from logging_system import logger
from game_saver import GameSaver
from utilities import Utilities

class Game:

    game_objects = [LevelMap.TRAP, LevelMap.TREASURE]

    def __init__(self):

        self.init_game()


    def init_game(self):

        """ Function init player and game map. Show the game rules. """

        self.show_game_rules()
        logger.debug('The game is started.')

        if self.check_start_new_game():
            side = self.__get_side_of_field()
            logger.debug('The field side is {}.'.format(side))
           
            self.level_map = LevelMap(side)
            logger.debug('The map was generated.')

            x, y = self.get_random_start_point()
            self.player = Player(x, y)
            logger.debug('The player places at ({0}, {1})'.format(x, y))
        else:
            self.load_game()
            logger.debug('The game was loaded successfully.')
            logger.debug('The start point is ({0}, {1})'.format(*self.player.get_coordinates()))


    def run(self):

        """ Function realize main logic of game """

        while self.player.is_alive() and not self.player.is_winner():

            logger.debug('The turn was started.')

            self.warn_situation()
            logger.debug('The situation was warned successfully.')
                
            choice = self.recognize_input()
            if choice == constants.SAVE_COMMAND_INDEX:
                self.save_game()
                while choice == constants.SAVE_COMMAND_INDEX:
                    choice = self.recognize_input()
                    
            logger.debug('The direction index is {}.'.format(choice))

            if not self.is_direction_blocked(choice):
                self.player.move_to(choice)
                logger.debug('The player moved to ({0}, {1})'.format(*self.player.get_coordinates()))

                if self.is_game_object_picked_up():
                    is_winning = self.check_game_win()

                    if is_winning:
                        self.player.increase_treasure_amount()
                        logger.info('The treasure picked up.')
                    else:
                        self.player.get_trapped()
                        logger.info('The player got trapped')

                    self.level_map.clear_cell(*self.player.get_coordinates())
                        
            else:
                logger.warning("You can't move there")
                    
            logger.debug('The turn was finished successfully.')

        self.show_game_result(self.player.is_winner())
        x, y = self.player.get_coordinates()
        self.level_map.level_matrix[x][y] = LevelMap.PLAYER
        self.level_map.show()

        logger.debug('The game is finished successfully.')
        

    @staticmethod
    def show_game_rules():

        """ Funtion shows game rules in its beginning. """
        
        print('''Rules:
                Player can move up, down, left and right
                (if it's not an edge of the map).
                If you get trapped - you lost.
                If you find a treasure - you won.''')


    def __get_side_of_field(self):

        """ Function recognize player's input to specify side of field.

            Args:
                (none)

            Returns:
                int: specified side

        """
        
        number_string = input('Enter the side of field(>= 8): ')

        while not number_string.isdigit() or int(number_string) < 8:
            number_string = input('Wrong input. Side: ')

        side = int(number_string)

        return side

    
    def get_random_start_point(self):

        """ Function return random start point for player.
            This point must be not a trap and not a treasure.

            Args:
                (none)

            Returns:
                (int, int): coordinates of start point

        """
        
        level_matrix = self.level_map.level_matrix

        line = randint(0, len(level_matrix) - 1)
        column = randint(0, len(level_matrix[line]) - 1)

        while level_matrix[line][column] in self.game_objects:
            line = randint(0, len(level_matrix) - 1)
            column = randint(0, len(level_matrix[line]) - 1)

        return line, column


    def get_new_coordinates(self, direction_index, x, y):

        """ Function returns new coordinates of player shifted in specified direction

            Args:
                direction_index(int): index presenting direction
                x(int): coordinate by columns of current player position
                y(int): coordinate by rows of current player position

            Returns:
                (int, int): new player's coordinates

        """
        
        shift_x, shift_y = Utilities.get_shift_by_direction(direction_index)
        new_x, new_y = shift_x + x, shift_y + y

        return new_x, new_y


    def warn_situation(self):

        """ Function warns the player if there's a trap or a treasure
            within one square from him.  """

        level_matrix = self.level_map.level_matrix
        x, y = self.player.get_coordinates()

        for _, index in enumerate(constants.directions.values()):
            
            if self.is_direction_blocked(index):
                continue

            temp_x, temp_y = self.get_new_coordinates(index, x, y)
            
            if level_matrix[temp_x][temp_y] == LevelMap.TRAP:
                logger.info('Near a trap. Be careful.')
            elif level_matrix[temp_x][temp_y] == LevelMap.TREASURE:
                logger.info('Near a treasure. Good luck.')


    def recognize_input(self):

        """ Function recognize player's input with possible save variant.

            Args:
                (none)

            Returns:
                int: index of direction or save command
        """
        
        player_choice = input('Enter the direction(r, l, u, d) or save: ')
        while player_choice == '':
            player_choice = input()

        while player_choice not in ['r', 'l', 'u', 'd', 'save']:
            player_choice = input('Wrong input. Direction: ')
        
        if player_choice == 'save':
            return constants.SAVE_COMMAND_INDEX

        direction = constants.directions.get(player_choice, None)

        return direction


    def is_direction_blocked(self, direction_index):

        """ Function checks possibility to move in specified direction
            from current position

            Args:
                direction_index(int): index presenting direction

            Returns:
                (bool): return True if player can NOT in specified direction
        """

        x, y = self.player.get_coordinates()
        new_x, new_y = self.get_new_coordinates(direction_index, x, y)
        
        level_matrix = self.level_map.level_matrix
        is_cell_blocked = new_x < 0 or new_y < 0 or \
                        new_x == len(level_matrix[0]) or \
                        new_y == len(level_matrix)

        return is_cell_blocked


    def is_game_object_picked_up(self):

        """ Function checks game over as winning or losing

            Args:
                (none)

            Returns:
                (bool): return True if player stand on a trap or treasure
        """

        x, y = self.player.get_coordinates()
        is_cell_contain_object = self.level_map.level_matrix[x][y] in self.game_objects

        return is_cell_contain_object


    def check_game_win(self):

        """ Function recognize result of pick uping by comparing game object with treasure.

            Args:
                (none)

            Returns:
                bool: return True if symbol is treasure
        """
        
        x, y = self.player.get_coordinates()
        symbol = self.level_map.level_matrix[x][y]

        is_winning = symbol == LevelMap.TREASURE
        
        return is_winning


    def show_game_result(self, is_winning):

        """ Function shows result of game

            Args:
                is_winning(bool): true if winning, otherwise - if losing

            Returns:
                (none)
        """
        
        result_string = 'You lose!'
        
        if is_winning:
            result_string = 'You won!'
            
        logger.info(result_string)


    def save_game(self):

        """ Function saves play map and player position to file  """

        save_object = {
            'map': self.level_map,
            'player': self.player
        }

        GameSaver.save_to_file(save_object)


    def load_game(self):

        """ Function loads play map and player position from file """
        
        saved_object = GameSaver.load_from_file()
        
        self.level_map = saved_object['map']
        self.player = saved_object['player']


    def check_start_new_game(self):

        """ Function checks start new game or load existing saving.
            If file does not exist, start new game

            Args:
                (none)

            Returns:
                (bool): return true if chosen start new game option,
                        otherwise - return False
        """
        
        logger.info('\nPress "load" for loading game.\nAnything to start new game.\n')

        choice = input('Enter your choice: ')

        is_start_new_game = choice != 'load'

        if not is_start_new_game and not GameSaver.check_loading_file():
            is_start_new_game = True
            logger.info('Loading does not exist. Starting new game...')

        return is_start_new_game
