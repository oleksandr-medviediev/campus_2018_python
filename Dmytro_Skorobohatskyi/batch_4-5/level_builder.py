from random import shuffle, randint
import logging_system


TRAP = '#'
TREASURE = '$'
LIMIT = '?'
FREE = '.'

def chunk_list(seq, num):

    """ Function divides the sequence into num pieces

        Args:
            seq(list): specified sequence
            num(int): amount of chunks

        Returns:
            (list): list of num lists
    """
    
    length = len(seq) 
    avg = length / num
    out = []
    last = 0.0

    while last < length:
        out.append(seq[int(last):int(last + avg)])
        last += avg

    return out

    
def generate_map(size_of_side):

    """ Function generates the square play field with size_of_side side

        Args:
            size_of_side(int): side of square play map

        Returns:
            list[list]: matrix presenting the play map

    """

    amount_cells = size_of_side ** 2

    amount_traps = amount_cells // 10
    amount_treasures = amount_cells // 20

    level_fill_cells = []
    for i in range(amount_traps):
        level_fill_cells.append(TRAP)

    for i in range(amount_treasures):
        level_fill_cells.append(TREASURE)

    amount_free_cell = amount_cells - amount_traps - amount_treasures

    for i in range(amount_free_cell):
        level_fill_cells.append(FREE)

    shuffle(level_fill_cells)

    level_map = chunk_list(level_fill_cells, size_of_side)

    return level_map


def show_level_map(level_map):

    """ Function shows play map on terminal

        Args:
            level_map(list[list]): matrix presenting the play map

        Returns:
            (none)
    """
    
    for i, row in enumerate(level_map):
        for j, cell in enumerate(row):
            print(cell, end=' ')
        print('')
