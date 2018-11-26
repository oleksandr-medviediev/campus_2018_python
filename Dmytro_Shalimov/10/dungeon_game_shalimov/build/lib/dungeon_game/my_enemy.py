from random import randrange
from my_decorator import log_wrapper, debug_wrapper

class Enemy:

    @log_wrapper
    @debug_wrapper
    def __init__(self):
        """
        Enemy class constructor
        """

        self.position = (None, None)

    @log_wrapper
    @debug_wrapper
    def initialize(self, position):
        """
        Initializes character's attributes

        :param tuple position:
        """

        self.position = position


    @log_wrapper
    @debug_wrapper
    def move_enemy(self, map_side_length):
        """
        Moves enemy to random cell around it

        :param: int map_side_length:
        """

        self.position = self.__generate_next_position(map_side_length)


    @log_wrapper
    @debug_wrapper
    def __generate_next_position(self, map_side_length):
        """
        Generates new enemy position

        :param: int map_side_length:
        """

        _possible_new_positions = []
        _new_position = (None, None)

        _enemy_position_row, _enemy_position_column = self.position

        _cell_right = (_enemy_position_column + 1) % map_side_length
        _cell_left = (map_side_length + (_enemy_position_column - 1)) % map_side_length

        _cell_top = (map_side_length + (_enemy_position_row - 1)) % map_side_length
        _cell_bottom = (_enemy_position_row + 1) % map_side_length

        _new_position = _cell_top, _enemy_position_column
        _possible_new_positions.append(_new_position)

        _new_position = _cell_bottom, _enemy_position_column
        _possible_new_positions.append(_new_position)

        _new_position = _enemy_position_row, _cell_left
        _possible_new_positions.append(_new_position)

        _new_position = _enemy_position_row, _cell_right
        _possible_new_positions.append(_new_position)

        _new_position = _cell_top, _cell_left
        _possible_new_positions.append(_new_position)

        _new_position = _cell_top, _cell_right
        _possible_new_positions.append(_new_position)

        _new_position = _cell_bottom, _cell_left
        _possible_new_positions.append(_new_position)

        _new_position = _cell_bottom, _cell_right
        _possible_new_positions.append(_new_position)

        return _possible_new_positions[randrange(len(_possible_new_positions))]
