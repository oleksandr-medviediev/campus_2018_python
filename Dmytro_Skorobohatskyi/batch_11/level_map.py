from random import shuffle, randint
from decorators import DebugDecorator

class LevelMap:

    TRAP = '#'
    TREASURE = '$'
    LIMIT = '?'
    FREE = '.'
    PLAYER = 'P'
    ENEMY = 'E'

    def __init__(self, size_of_side):

        amount_cells = size_of_side ** 2

        amount_traps = amount_cells // 10
        amount_treasures = amount_cells // 20

        level_fill_cells = []
        for _ in range(amount_traps):
            level_fill_cells.append(self.TRAP)

        for _ in range(amount_treasures):
            level_fill_cells.append(self.TREASURE)

        amount_free_cell = amount_cells - amount_traps - amount_treasures

        for _ in range(amount_free_cell):
            level_fill_cells.append(self.FREE)

        shuffle(level_fill_cells)

        self.level_matrix = self.__chunk_list(level_fill_cells, size_of_side)
        

    def __str__(self):

        return "LevelMap"


    @staticmethod
    def __chunk_list(seq, num):

        """ Function divides the sequence into num pieces

            Args:
                seq(list): specified sequence
                num(int): amount of chunks

            Returns:
                (list): list of num lists
        """
        
        length = len(seq) 
        avg = 0
        
        try:
            avg = length / num
        except ZeroDivisionError:
            return seq

        out = []
        last = 0.0

        while last < length:
            out.append(seq[int(last):int(last + avg)])
            last += avg

        return out


    @DebugDecorator()
    def show(self):

        """ Function shows play map on terminal """
        
        for _, row in enumerate(self.level_matrix):
            for _, cell in enumerate(row):
                print(cell, end=' ')
            print('')


    @DebugDecorator()
    def clear_cell(self, x, y):

        """ Function mark cell with x, y coordinates as free.

            Args: 
                x(int): x coordinate of player
                y(int): y coordinate of player
            
            Return:
                (none)
        """
        
        self.level_matrix[x][y] = self.FREE
