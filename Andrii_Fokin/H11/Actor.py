
class Actor:
    
    MoveError = IndexError
    move_types = {
        'Up': [0, 1],
        'Dawn': [0, -1],
        'Right': [1, 0],
        'Left': [-1, 0]
    }


    def __init__(self):
        self.__previous_position = [0, 0]
        self.position = [0, 0]


    def move(self, move_type):
        
        if move_type not in self.move_types:
            raise self.MoveError()

        direction = self.move_types[move_type]
        self.__previous_position = self.position.copy()
        
        self.position[0] += direction[0]
        self.position[1] += direction[1]
        return self.position


    def undo_move(self):
        self.position = self.__previous_position
