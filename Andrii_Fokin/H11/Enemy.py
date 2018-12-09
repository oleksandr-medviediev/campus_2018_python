from random import randint as rint
from tools.dg_decorators import decorator_start_end_logging
from Actor import Actor


class Enemy(Actor):
    
    @decorator_start_end_logging
    def move(self):
        move_type_index = rint(0, len(self.move_types) - 1)
        move_type = list(self.move_types.keys())[move_type_index]
        super().move(move_type)
