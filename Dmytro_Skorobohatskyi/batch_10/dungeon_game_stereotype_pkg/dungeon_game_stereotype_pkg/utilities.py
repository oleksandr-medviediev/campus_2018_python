from . import constants

from .decorators import DebugDecorator

class Utilities:

    @staticmethod
    @DebugDecorator()
    def get_shift_by_direction(direction_index):

        """ Function return shift depending on direction.

            Args:
                direction_index(int): index specified direction

            Returns:
                (int, int): shift by columns and rows
        """
        
        shift_x = constants.all_shifts[direction_index]['x']
        shift_y = constants.all_shifts[direction_index]['y']

        return shift_x, shift_y


    @staticmethod
    @DebugDecorator()
    def get_new_coordinates(direction_index, x, y):

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