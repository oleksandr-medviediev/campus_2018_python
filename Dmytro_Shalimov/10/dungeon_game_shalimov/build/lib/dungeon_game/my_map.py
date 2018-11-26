from random import shuffle
from random import randrange
from my_decorator import log_wrapper, debug_wrapper
from my_errors import CharacterNotFoundError
import my_game_constants


class MyMap:

    @log_wrapper
    @debug_wrapper
    def __init__(self):
        """
        MyMap class constructor
        """

        self.size = 0
        self.traps = 0
        self.treasures = 0
        self.generated_map = []


    @log_wrapper
    @debug_wrapper
    def initialize(self, size):
        """
        Initializes map's attributes

        :param int size:
        """

        self.size = size
        self.__generate_map()


    @log_wrapper
    @debug_wrapper
    def __generate_init_object_position(self, character):
        """
        Generates random position for given object

        :param str character:
        """

        _player_position = 0

        while True:

            _player_position = randrange(len(self.generated_map))

            if self.generated_map[_player_position] == my_game_constants.EMPTY_CELL:

                self.generated_map[_player_position] = character
                break


    @log_wrapper
    @debug_wrapper
    def __generate_map(self):
        """
        Generates map of given size with player, traps and treasures
        """

        _map_area = self.size * self.size

        self.treasures = _map_area // 20
        self.traps = _map_area // 10

        _empty_cells_amount = _map_area - self.treasures - self.traps

        print('Generating map')

        self.generated_map.extend([my_game_constants.TREASURE for x in range(0, self.treasures)])
        self.generated_map.extend([my_game_constants.TRAP for x in range(0, self.traps)])
        self.generated_map.extend([my_game_constants.EMPTY_CELL
                                   for x in range(0, _empty_cells_amount)])

        self.__generate_init_object_position(my_game_constants.PLAYER)
        self.__generate_init_object_position(my_game_constants.ENEMY)

        shuffle(self.generated_map)

        self.generated_map = [self.generated_map[i : i + self.size]
                              for i in range(0, len(self.generated_map), self.size)]


    @log_wrapper
    @debug_wrapper
    def get_object_position(self, character):
        """
        Returns given object position

        :param str character:
        :return: tuple with player position indeces (row, column)
        :rtype: tuple
        """

        _object_position = (None, None)

        try:

            for i, row in enumerate(self.generated_map):
                for j, column in enumerate(row):

                    if column == character:

                        _object_position = (i, j)
                        break

                if _object_position[0] is not None:
                    break

            if _object_position == (None, None):
                raise CharacterNotFoundError('Given character is not found on the map!\
                                             Terminating...')

        except CharacterNotFoundError as no_char_error:

            print(no_char_error.message)
            quit()

        return _object_position


    @log_wrapper
    @debug_wrapper
    def generate_new_position(self, character):
        """
        Generates new position for given object and places it on map

        :param str character:
        :return: tuple with player position indeces (row, column)
        :rtype: tuple
        """

        _object_position = (None, None)
        _map_side_size = len(self.generated_map)

        _rand_row = 0
        _rand_column = 0

        while True:

            _rand_row = randrange(_map_side_size)
            _rand_column = randrange(_map_side_size)

            if self.generated_map[_rand_row][_rand_column] == my_game_constants.EMPTY_CELL:

                self.generated_map[_rand_row][_rand_column] = character
                _object_position = (_rand_row, _rand_column)
                break

        return _object_position


    @log_wrapper
    @debug_wrapper
    def print_map(self):
        """
        Prints current map
        """

        for i in range(len(self.generated_map)):
            print(self.generated_map[i])


    @log_wrapper
    @debug_wrapper
    def resolve_player_got_in_trap(self):
        """
        Removes trap from map
        """

        self.traps -= 1
