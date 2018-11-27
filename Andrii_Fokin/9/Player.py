from tools.dg_exсeptios import PlayerMoveError
from tools.dg_decorators import decorator_start_end_logging

from Actor import Actor


class Player(Actor):

    @decorator_start_end_logging
    def __init__(self):
        super().__init__()
        self.HP = 3
        self.score = 0


    @decorator_start_end_logging
    def move(self, move_type):
        super().move(move_type)

    @decorator_start_end_logging
    def undo_move(self):
        super().undo_move()

    @decorator_start_end_logging
    def __str__(self):
        return f'Position : {self.position}\nHP : {self.HP}\nScore : {self.score}'
