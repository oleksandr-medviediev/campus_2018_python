from random import randint
from custom_logger import logger as log
from logger_decorator import debug_log_decorator
from character import character
from enemy import enemy


EMPTY_CELL = '🟋'
TRAP = '◉'
TREASURE = '⭐'
PLAYER = '웃'
WALL = '⏹'
ENEMY = '👾'


class GameTerrain:
    def __init__(self, size):
        self.terrain = list()
        self.size = size

    @debug_log_decorator
    def init_free_cell(self, cell_type):
        while True:
            i = randint(1, self.size)
            j = randint(1, self.size)

            if self.terrain[i][j] == EMPTY_CELL:
                self.terrain[i][j] = cell_type
                return [i, j]

    @debug_log_decorator
    def generate_new_map(self):
        self.terrain = [[EMPTY_CELL for j in range(self.size + 2)]
                   for i in range(self.size + 2)]

        # generating walls
        for i in range(self.size + 2):
            self.terrain[i][0] = WALL
            self.terrain[0][i] = WALL

            self.terrain[i][self.size + 1] = WALL
            self.terrain[self.size + 1][i] = WALL

        # generating treasures
        for i in range((self.size**2) // 20):
            self.init_free_cell(TREASURE)

        # generating traps
        for i in range((self.size**2) // 10):
            self.init_free_cell(TRAP)

        character.position = self.init_free_cell(PLAYER)
        self.respawn_enemy()


    @debug_log_decorator
    def find_player_position(self):
        for i in range(1, self.size + 2):
            for j in range(1, self.size + 2):
                if self.terrain[i][j] == PLAYER:
                    log.debug(
                        f'find_player_position: player position is x = {j}, y = {i}')
                    return [i, j]


    @debug_log_decorator
    def find_player_enemy(self):
        for i in range(1, self.size + 2):
            for j in range(1, self.size + 2):
                if self.terrain[i][j] == ENEMY:
                    log.debug(
                        f'find_player_position: player position is x = {j}, y = {i}')
                    return [i, j]

    
    @debug_log_decorator
    def respawn_enemy(self):
        enemy.position = game_terrain.init_free_cell('👾')
        enemy.previous_cell = '🟋'


game_terrain = GameTerrain(10)
