import constants
from decorators import DebugDecorator

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
