class DungeonGameError(Exception):

    def __init__(self, message):
        self.__message = message

    def __str__(self):
        return f'{self.__class__.__name__}: {self.__message}'


class WrongInputDungeonGameError(DungeonGameError):

    def __init__(self, actual_input, required_input):
        super().__init__(f'`{actual_input}` is wrong input, it should be: {required_input}')


class CellOutOfBoundsDungeonGameError(DungeonGameError):

    def __init__(self, size, x, y):
        super().__init__(f'(x:{x}, y:{y}) is wrong cell coords, it should be: 0 < x < {size}, 0 < y < {size}')
