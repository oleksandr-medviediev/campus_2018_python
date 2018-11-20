"""module for generating game map

        * - stands for a treasure
        t - stands for a trap
        . - stands for an empty square
        s - stands for the start position

        Top left square coordinates are (0, 0)
"""

from random import choices
from random import choice
from math import floor

from decorators import debug_decorator
from decorators import info_decorator


class Terrain:

    __start_row = 0
    __start_col = 0
    __map = []
    __scale = 0

    @info_decorator
    @debug_decorator
    def __init__(self, scale=0):
        """Generate a map and a starting position

        Arguments:
            scale int -- map scale (number of squares == scale * scale)
        """
        self.__scale = scale

        traps = []
        treasures = []

        size = scale * scale

        squares_id = range(size)

        traps = choices(squares_id, k=floor(size / 10))

        treasures = [square for square in squares_id if square not in traps]
        treasures = choices(treasures, k=floor(size / 20))

        empty_squares = []

        for square in squares_id:
            if square not in traps and square not in treasures:
                empty_squares.append(square)

        start_position = choice(empty_squares)

        self.__start_row = start_position // scale
        self.__start_col = start_position - self.__start_row * scale

        row = []

        for square in range(size):

            if square in traps:
                row.append('t')
            elif square in treasures:
                row.append('*')
            elif square == start_position:
                row.append('s')
            else:
                row.append('.')

            if len(row) == scale:

                self.__map.append(row)
                row = []

    @property
    def start_position(self):
        """get start position

        Returns:
            tuple -- tuple of 2 ints: start row and start column
        """

        return self.__start_row, self.__start_col

    def get_square(self, row, col):
        """get square type located at given row and column

        Arguments:
            row {int} -- given row
            col {int} -- given column

        Returns:
            str -- object type located at given row and column
        """

        return self.__map[row][col]

    @property
    def scale(self):
        return self.__scale

    @property
    def map(self):
        return self.__map

    def __str__(self):

        string = "\n"

        for row in self.__map:

            for col in row:
                string += col
            
            string += '\n'

        return string
