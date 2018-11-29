from custom_logger import logger as log
from logger_decorator import debug_log_decorator
from game_terrain import game_terrain
from random import choice
from character import character


class Enemy:
    def __init__(self):
        self.position = [-1, -1]
        self.moves = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        self.previous_cell = '🟋'

    def move(self):
        move = choice(self.moves)
        game_terrain.terrain[self.position[0],
                             self.position[1]] = self.previous_cell
        self.position[0] += move[0]
        self.position[1] += move[1]
        self.previous_cell = game_terrain.terrain[self.position[0],
                                                  self.position[1]]

        if self.position[0] == character.position[0] and self.position[1] == character.position[1]:
            character.current_hp -= 1
            log.info(
                        f"You've found a trap {'👾'} \n{character.current_hp} / 3 hp")
            self.respawn()
        else:
            game_terrain.terrain[self.position[0], self.position[1]] = '👾'

    def respawn(self):
        self.position = game_terrain.init_free_cell('👾')
        self.previous_cell = '🟋'


enemy = Enemy()
