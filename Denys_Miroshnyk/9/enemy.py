
class Enemy:
    def __init__(self):
        self.position = [-1, -1]
        self.moves = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        self.previous_cell = '🟋'


enemy = Enemy()
