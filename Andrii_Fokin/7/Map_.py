from random import randint as rint
import dg_decorators


class Map_:

    cell_free = '-'
    cell_trap = '#'
    cell_treasure = '@'
    cell_player = 'P'
    cell_border = '%'

    @dg_decorators.decorator_start_end_logging
    def __init__(self, size):
        self.size = int(size + 2)
        self.field = [[self.cell_free for _ in range(self.size)] for _ in range(self.size)]

        for i in range(self.size):
            self.field[i][0] = self.cell_border
            self.field[0][i] = self.cell_border

            self.field[i][self.size - 1] = self.cell_border
            self.field[self.size - 1][i] = self.cell_border

        for i in range(((self.size - 2)**2) // 20):
            self._fill_free_cell(self.cell_trap)
            self._fill_free_cell(self.cell_trap)
            self._fill_free_cell(self.cell_treasure)


    @dg_decorators.decorator_start_end_logging
    def get_cell_type(self, cell_coordinates):

        x = cell_coordinates[0]
        y = cell_coordinates[1]

        result = self.field[y][x]
        return result


    @dg_decorators.decorator_start_end_logging
    def set_cell_type(self, cell_coordinates, cell_type):
        x = cell_coordinates[0]
        y = cell_coordinates[1]

        self.field[y][x] = cell_type


    @dg_decorators.decorator_start_end_logging
    def get_free_cell(self):
        while (True):
            i = rint(1, self.size - 1)
            j = rint(1, self.size - 1)

            if self.field[i][j] == self.cell_free:
                return [j, i]


    @dg_decorators.decorator_start_end_logging
    def _fill_free_cell(self, cell_type):
        while (True):
            i = rint(1, self.size - 1)
            j = rint(1, self.size - 1)

            if self.field[i][j] == self.cell_free:
                self.field[i][j] = cell_type
                return [j, i]


    @dg_decorators.decorator_start_end_logging
    def __str__(self):
        result = f'Treasure {self.cell_treasure}\
        \nTrap {self.cell_trap}\
        \nBorder {self.cell_border}'
        
        for line in self.field[::-1]:
            result += f'\n {line}'

        return result