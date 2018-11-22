import os.path
import pickle
import my_game_constants
from my_errors import LoadDataError, MapSizeError
from my_decorator import log_wrapper, debug_wrapper
from my_player import Player
from my_map import MyMap


class MyGameFlow:

    @log_wrapper
    @debug_wrapper
    def __init__(self):
        """
        MyGameFlow class constructor
        """

        self.is_new_game = False
        self.player = Player()
        self.game_map = MyMap()


    @log_wrapper
    @debug_wrapper
    def __map_size_input(self):
        """
        Prompts user to enter map size until it meets set requirements

        :return: map size
        :rtype: int
        """

        _map_size = 0
        
        _user_input = input("Enter map size(min - 5, max - 50): ")

        try:

            _map_size = int(_user_input)

            if _map_size < 5 or _map_size > 50:
                raise MapSizeError('Invalid map size, try again')

        except ValueError:

            print('Invalid input, try again')
            _map_size = self.__map_size_input()

        except MapSizeError as map_size_error:
            
            print(map_size_error.message)
            _map_size = self.__map_size_input()

        return _map_size


    @log_wrapper
    @debug_wrapper
    def __process_save_game(self):
        """
        Prompts user to enter file name to serialize his current game state using pickle
        """
    
        
        _data_to_save = (my_game_constants.SAVE_GAME_HEADER, self.game_map, self.player)

        while True:

            _user_input = input('Enter save file name: ')

            if len(_user_input) > 0:
                break

            print('Invalid input! Try again')
        

        with open(f'{_user_input}.pickle', 'wb') as save_file:
            pickle.dump(_data_to_save, save_file)

        print(f'Game saved in {_user_input}.pickle')  

        return None


    @log_wrapper
    @debug_wrapper
    def __process_load_game(self):
        """
        Prompts user to enter file name to load game from
        """
        
        _loaded_data = ()

        _user_input = input('Enter file name: ')

        try:

            with open(f'{_user_input}.pickle', 'rb') as load_file:
                _loaded_data = pickle.load(load_file)
               
            if _loaded_data[0] != my_game_constants.SAVE_GAME_HEADER:
                raise LoadDataError('Load data error! Terminating...')


        except FileNotFoundError:

            print('No such file exists! Terminating...')
            quit()

        except LoadDataError as load_error:

            print(load_error.message)
            quit()

        except EOFError:

            print('File is empty! Terminating...')
            quit()

        else:
            
            _, self.game_map, self.player = _loaded_data
            print('Data is loaded')

        return None


    @log_wrapper
    @debug_wrapper
    def __process_select_game_type(self):
        """
        Prompts user to select whether he wants to start a new game or load saved one if it exists
        """

        while True:

            _user_input = input('Enter "new" to start new game, "load" to load saved one(if it exists)": ')
            _user_input = _user_input.lower()

            if _user_input == 'new':

                self.is_new_game = True
                break

            elif _user_input == 'load':
                break

            print('Invalid input! Try again')

        return None


    @log_wrapper
    @debug_wrapper
    def __enter_player_name(self):
        """
        Prompts user to enter his name

        :return: str with player name
        :rtype: str
        """

        _user_input = ''

        while True:

            _user_input = input('Enter your name: ')

            if len(_user_input) > 0:
                break

            print('Invalid input! Try again')

        return _user_input


    @log_wrapper
    @debug_wrapper
    def __update_player_position(self, direction):
        """
        Calculates new player position according to given direction

        :param tuple direction: movement direction
        """

        _direction_row, _direction_column = direction
        _new_player_position_row, _new_player_position_column = self.player.position
        _map_side_lenght = len(self.game_map.generated_map)

        if _direction_row > 0:
            _new_player_position_row = (_new_player_position_row + 1) % _map_side_lenght

        elif _direction_row < 0:
            _new_player_position_row = (_map_side_lenght + _new_player_position_row - 1) % _map_side_lenght

        elif _direction_column > 0:
            _new_player_position_column = (_new_player_position_column + 1) % _map_side_lenght

        elif _direction_column < 0:
            _new_player_position_column = (_map_side_lenght + _new_player_position_column - 1) % _map_side_lenght

        self.player.position = (_new_player_position_row, _new_player_position_column)

        return None


    @log_wrapper
    @debug_wrapper
    def __process_move_player(self, user_input):
        """
        Updates given data according to new player position defined by user input

        :param str user_input: direction of player movement
        """
    
        _direction = my_game_constants.PLAYER_MOVE_DIRECTIONS_BY_NAMES[user_input]

        _current_player_position_row, _current_player_position_column = self.player.position

        self.game_map.generated_map[_current_player_position_row][_current_player_position_column] = \
           my_game_constants.EMPTY_CELL

        self.__update_player_position(_direction)

        _updated_player_position_row, _updated_player_position_column = self.player.position

        if self.game_map.generated_map[_updated_player_position_row][_updated_player_position_column] \
            == my_game_constants.TRAP:

            self.game_map.resolve_player_got_in_trap()
            self.player.resolve_trap_effect()
            print('You have gotten into a trap!')

        elif self.game_map.generated_map[_updated_player_position_row][_updated_player_position_column] \
             == my_game_constants.TREASURE:

              self.player.add_treasure()
              print('You have found a treasure!')

        self.game_map.generated_map[_updated_player_position_row][_updated_player_position_column] = \
           my_game_constants.PLAYER

        return None


    @log_wrapper
    @debug_wrapper
    def __process_user_input(self):
        """
        Prompts user to move character or save game
        """
        
        while True:

            _user_input = input('Enter "up", "down", "left", "right" to move, "save" to save current game: ')
            _user_input = _user_input.lower()

            if _user_input in my_game_constants.PLAYER_MOVE_DIRECTIONS_NAMES:

                self.__process_move_player(_user_input)
                break

            elif _user_input == 'save':

                self.__process_save_game()
                break

            print('Invalid input! Please, try again')

        return None


    def init_game(self):
        """
        Initialize flow variables according to user input
        """

        self.__process_select_game_type()

        if self.is_new_game:

            _player_name = self.__enter_player_name()
            _map_size = self.__map_size_input()

            self.game_map.initialize(_map_size)
            self.player.initialize(self.game_map.traps, _player_name, self.game_map.get_player_position())

        else:
            self.__process_load_game()

        return None


    @log_wrapper
    @debug_wrapper
    def run_game(self):
        """
        Runs game cycle
        """

        while True:
            
            if self.player.hp == 0:

                print(f'Bad luck, {self.player.name}! You have no health!')
                break

            elif self.player.bag == self.game_map.treasures:

                print(f'Congrats, {self.player.name}! You have collected all treasures!')
                break

            print(f'{self.player.name},')
            print(f'You have {self.player.hp} hp')
            print(f'You have collected {self.player.bag} treasures out of {self.game_map.treasures}')
            
            self.__scan_area_around_player()
            self.__process_user_input()

        self.game_map.print_map()

        return None


    @log_wrapper
    @debug_wrapper
    def __scan_area_around_player(self):
        """
        Checks cells around player for treasures and traps and prints corresponding notifications
        """
    
        _player_position_row, _player_position_column = self.player.position
        _map_side_lenght = len(self.game_map.generated_map)
    
        _cell_right = (_player_position_column + 1) % _map_side_lenght
        _cell_left = (_map_side_lenght + (_player_position_column - 1)) % _map_side_lenght

        _cell_top = (_map_side_lenght + (_player_position_row - 1)) % _map_side_lenght
        _cell_bottom = (_player_position_row + 1) % _map_side_lenght
    
        _cell_type = self.game_map.generated_map[_player_position_row][_cell_left]
        self.__scan_notification(_cell_type)

        _cell_type = self.game_map.generated_map[_player_position_row][_cell_right]
        self.__scan_notification(_cell_type)

        _cell_type = self.game_map.generated_map[_cell_top][_player_position_column]
        self.__scan_notification(_cell_type)

        _cell_type = self.game_map.generated_map[_cell_bottom][_player_position_column]
        self.__scan_notification(_cell_type)

        _cell_type = self.game_map.generated_map[_cell_top][_cell_left]
        self.__scan_notification(_cell_type)

        _cell_type = self.game_map.generated_map[_cell_top][_cell_right]
        self.__scan_notification(_cell_type)

        _cell_type = self.game_map.generated_map[_cell_bottom][_cell_right]
        self.__scan_notification(_cell_type)

        _cell_type = self.game_map.generated_map[_cell_bottom][_cell_left]
        self.__scan_notification(_cell_type)

        return None


    @log_wrapper
    @debug_wrapper
    def __scan_notification(self, cell_type):
        """
        Checks cell type and prints notification if check is passed

        :param str cell_type: type of item in cell
        """

        if cell_type != my_game_constants.EMPTY_CELL:
            print(my_game_constants.CELL_TYPES_INFO_MESSAGES[cell_type])

        return None
