import pickle
import time
import asyncio
import threading
import my_game_constants
from my_errors import LoadDataError, MapSizeError
from my_decorator import log_wrapper, debug_wrapper
from my_player import Player
from my_enemy import Enemy
from my_map import MyMap


class MyGameFlow:

    @log_wrapper
    @debug_wrapper
    def __init__(self):
        """
        MyGameFlow class constructor
        """

        self.is_game_over = False
        self.is_new_game = False
        self.is_enemy_moved = True
        self.move_input = ''

        self.player = Player()
        self.game_map = MyMap()
        self.enemy = Enemy()


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
        Saves game into file, name is generated with current date and time
        """

        _data_to_save = (my_game_constants.SAVE_GAME_HEADER, self.game_map, self.player, self.enemy)

        _file_name = time.ctime()
        _file_name = _file_name.replace(" ", "")
        _file_name = _file_name.replace(':', "")

        with open(f'{_file_name}.pickle', 'wb') as save_file:
            pickle.dump(_data_to_save, save_file)

        print(f'Game saved in {_file_name}.pickle')  


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
            
            _, self.game_map, self.player, self.enemy = _loaded_data
            print('Data is loaded')


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


    @log_wrapper
    @debug_wrapper
    def __process_move_player(self):
        """
        Updates given data according to new player position defined by user input
        """
    
        _direction = my_game_constants.PLAYER_MOVE_DIRECTIONS_BY_NAMES[self.move_input]

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


    @log_wrapper
    @debug_wrapper
    def init_game(self):
        """
        Initialize flow variables according to user input
        """

        self.__process_select_game_type()

        if self.is_new_game:

            _player_name = self.__enter_player_name()
            _map_size = self.__map_size_input()

            self.game_map.initialize(_map_size)

            _player_position = self.game_map.get_object_position(my_game_constants.PLAYER)
            _enemy_position = self.game_map.get_object_position(my_game_constants.ENEMY)
            
            self.player.initialize(self.game_map.traps, _player_name, _player_position)
            self.enemy.initialize(_enemy_position)

        else:
            self.__process_load_game()


    @log_wrapper
    @debug_wrapper
    def run_game(self):
        """
        Runs game cycle
        """

        _thread = threading.Thread(target = self.__process_user_input)
        _thread.start()

        _event_loop = asyncio.get_event_loop()
        _tasks = [_event_loop.create_task(self.__check_game_conditions()),
                _event_loop.create_task(self.__resolve_enemy_actions()),
                _event_loop.create_task(self.__check_player_input())]

        _wait_tasks = asyncio.wait(_tasks)
        _event_loop.run_until_complete(_wait_tasks)
        _event_loop.close()

        self.game_map.print_map()
        _thread.join()


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


    @log_wrapper
    @debug_wrapper
    def __scan_notification(self, cell_type):
        """
        Checks cell type and prints notification if check is passed

        :param str cell_type: type of item in cell
        """

        if cell_type != my_game_constants.EMPTY_CELL \
            and my_game_constants.CELL_TYPES_INFO_MESSAGES.get(cell_type) != None:

            print(my_game_constants.CELL_TYPES_INFO_MESSAGES[cell_type])


    @log_wrapper
    @debug_wrapper
    async def __resolve_enemy_actions(self):
        """
        Processes enemy movement and interaction with player
        """

        _time_since_last_enemy_move = time.time()
        _time_now = time.time()

        while not self.is_game_over:

            _time_now = time.time()
            
            if self.enemy.position == self.player.position:

                print('Enemy hit you')

                self.player.resolve_enemy_hit()
                _player_position_row, _player_position_column = self.player.position

                if self.player.hp == 0:

                    self.is_game_over = True

                    self.game_map.generated_map[_player_position_row][_player_position_column] = \
                        my_game_constants.ENEMY

                    print(f'Bad luck, {self.player.name}! You have no health!')

                else:

                    self.game_map.generated_map[_player_position_row][_player_position_column] = \
                        my_game_constants.PLAYER

                    self.enemy.position = self.game_map.generate_new_position(my_game_constants.ENEMY)

                    _time_since_last_enemy_move = time.time()

            elif (_time_now - _time_since_last_enemy_move) > my_game_constants.ENEMY_MOVE_INTERVAL:

                print('Enemy moved')

                _time_since_last_enemy_move = time.time()
                self.is_enemy_moved = True

                _enemy_position_row, _enemy_position_column = self.enemy.position

                self.game_map.generated_map[_enemy_position_row][_enemy_position_column] = \
                        my_game_constants.EMPTY_CELL

                self.enemy.move_enemy(len(self.game_map.generated_map))

                self.__resolve_enemy_movement()

            await asyncio.sleep(0)


    @log_wrapper
    @debug_wrapper
    async def __check_game_conditions(self):
        """
        Checks game conditions
        """

        self.__display_current_info()
        
        while not self.is_game_over:         

            if self.player.hp == 0:

                self.is_game_over = True

                _player_position_row, _player_position_column = self.player.position
                    
                self.game_map.generated_map[_player_position_row][_player_position_column] = \
                    my_game_constants.DEAD_PLAYER

                print(f'Bad luck, {self.player.name}! You have no health!')

            elif self.player.bag == self.game_map.treasures:

                self.is_game_over = True

                print(f'Congrats, {self.player.name}! You have collected all treasures!')
                    
            elif self.game_map.treasures == 0 and self.player.bag == 0:

                self.is_game_over = True
                print(f'Enemy destroyed all treasures! You lost')

            await asyncio.sleep(0)


    @log_wrapper
    @debug_wrapper
    def __process_user_input(self):
        """
        Processes user input in separate thread
        """

        while not self.is_game_over:
            self.move_input = input()


    @log_wrapper
    @debug_wrapper
    async def __check_player_input(self):
        """
        Processes player input
        """

        while not self.is_game_over:

            if self.is_enemy_moved:

                print('Enter "u", "d", "l", "r" to move, "s" to save current game: ')
                self.is_enemy_moved = False

            if self.move_input in my_game_constants.PLAYER_MOVE_DIRECTIONS_NAMES:

                self.__process_move_player()
                self.__display_current_info()

            elif self.move_input == 's':

                self.__process_save_game()
                self.__display_current_info()

            elif len(self.move_input) > 0:

                print('Invalid input! Please, try again')
                print('Enter "u", "d", "l", "r" to move, "s" to save current game: ')
                self.is_enemy_moved = False

            self.move_input = ''
            await asyncio.sleep(0)


    @log_wrapper
    @debug_wrapper
    def __display_current_info(self):
        """
        Displays current game info
        """

        print(f'{self.player.name},')
        print(f'You have {self.player.hp} hp')
        print(f'You have collected {self.player.bag} treasures out of {self.game_map.treasures}')

        self.__scan_area_around_player()


    @log_wrapper
    @debug_wrapper
    def __resolve_enemy_movement(self):
        """
        Checks effect of enemy movement
        """

        _enemy_position_row, _enemy_position_column = self.enemy.position

        if self.game_map.generated_map[_enemy_position_row][_enemy_position_column] \
            == my_game_constants.TRAP:

            print('Enemy got into a trap!')

            self.game_map.generated_map[_enemy_position_row][_enemy_position_column] =\
                my_game_constants.EMPTY_CELL

            self.game_map.generate_new_position(my_game_constants.TRAP)
            self.enemy.position = self.game_map.generate_new_position(my_game_constants.ENEMY)

        elif self.game_map.generated_map[_enemy_position_row][_enemy_position_column] \
            == my_game_constants.TREASURE:

            print('Enemy destroyed treasure!')

            self.game_map.generated_map[_enemy_position_row][_enemy_position_column] =\
                my_game_constants.EMPTY_CELL

            self.game_map.generate_new_position(my_game_constants.TREASURE)
            self.enemy.position = self.game_map.generate_new_position(my_game_constants.ENEMY)

        else:

            self.game_map.generated_map[_enemy_position_row][_enemy_position_column] =\
                my_game_constants.ENEMY
