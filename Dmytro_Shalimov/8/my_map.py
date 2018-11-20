from my_decorator import log_wrapper, debug_wrapper
from random import shuffle
from random import randrange
from my_errors import PlayerNotFoundError
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

        return None


    def __generate_player_position(self):
        """
        Generates random position for player
        """

        player_position = 0
        
        while True:
        
            player_position = randrange(len(self.generated_map))

            if self.generated_map[player_position] == my_game_constants.EMPTY_CELL:

                self.generated_map[player_position] = my_game_constants.PLAYER
                break

        return None


    def __generate_map(self):
        """
        Generates map of given size with player, traps and treasures
        """

        _map_area = self.size * self.size

        self.treasures = _map_area // 20
        self.traps = _map_area // 10

        _empty_cells_amount = _map_area - self.treasures - self.traps
    
        print('Generating map')

        self.generated_map.extend([my_game_constants.TREASURE for x in range(0,  self.treasures)])
        self.generated_map.extend([my_game_constants.TRAP for x in range(0, self.traps)])
        self.generated_map.extend([my_game_constants.EMPTY_CELL for x in range(0, _empty_cells_amount)])

        self.__generate_player_position()

        shuffle(self.generated_map)

        self.generated_map = [self.generated_map[i : i + self.size]
                             for i in range(0, len(self.generated_map), self.size)]

        return None


    def get_player_position(self):
        """
        Returns player position

        :return: tuple with player position indeces (row, column)
        :rtype: tuple
        """

        _player_position = (None, None)

        try:

            for i, row in enumerate(self.generated_map):
                for j, column in enumerate(row):

                    if column == my_game_constants.PLAYER:

                        _player_position = (i, j)
                        break
        
                if _player_position[0] != None:
                    break

            if _player_position == (None, None):
                raise PlayerNotFoundError()
        
        except PlayerNotFoundError:

            print('Player is not found on the map! Terminating...')
            quit()

        return _player_position


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
