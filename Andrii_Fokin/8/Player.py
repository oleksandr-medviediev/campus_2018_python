import dg_decorators
from dg_exсeptios import PlayerMoveError

move_types = {
    'Up': [0, 1],
    'Dawn': [0, -1],
    'Right': [1, 0],
    'Left': [-1, 0]
}


class Player:

    @dg_decorators.decorator_start_end_logging
    def __init__(self):
        self.__previous_position = [0, 0]
        self.position = [0, 0]
        self.HP = 3
        self.score = 0


    @dg_decorators.decorator_start_end_logging
    def move(self, move_type):
        
        global move_types
        if move_type not in move_types:
            raise PlayerMoveError()

        direction = move_types[move_type]
        self.__previous_position = self.position.copy()
        
        self.position[0] += direction[0]
        self.position[1] += direction[1]
        return self.position


    @dg_decorators.decorator_start_end_logging
    def undo_move(self):
        self.position, self.__previous_position = self.__previous_position, self.position


    @dg_decorators.decorator_start_end_logging
    def __str__(self):
        return f'Position : {self.position}\nHP : {self.HP}\nScore : {self.score}'
