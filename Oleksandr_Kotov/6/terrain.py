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


@info_decorator
@debug_decorator
def generate(scale):
    """Generate a map and a starting position

    Arguments:
        scale int -- map scale (number of squares == scale * scale)

    Returns:
        int -- start row
        int -- start column
        squares_map -- a map represented by an array of strings
    """

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

    start_row = start_position // scale
    start_col = start_position - start_row * scale

    squares_map = []

    row = ""

    for square in range(size):

        if square in traps:
            row += 't'
        elif square in treasures:
            row += '*'
        elif square == start_position:
            row += 's'
        else:
            row += '.'

        if len(row) == scale:

            squares_map.append(row)
            row = ""

    return (start_row, start_col, squares_map)
