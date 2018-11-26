from logger import debug_decorator
from logger import info_decorator
from random import choice

class Enemy:

    def __init__(self):
        self.attacked = False


    @debug_decorator
    @info_decorator
    def move(self, map_size):

        DIRECTION_TO_MOVE = [ [-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1] ]

        neighbour_cells = [[self.position[0] + direction[0], self.position[1] + direction[1]] \
        for direction in list(DIRECTION_TO_MOVE)]
        
        neighbour_cells = list(filter(lambda cell: cell[0] >= 0 and cell[1] >= 0 
            and cell[0] < map_size and cell[1] < map_size, neighbour_cells))

        self.position = choice(neighbour_cells)

        return self.position


    @debug_decorator
    @info_decorator
    def is_attacked_player(self, player):

        self.attacked = False

        if player.position == self.position:
            self.attacked = True

        return self.attacked


    @debug_decorator
    @info_decorator
    def respawn(self, position):
        self.spawn(position)


    @debug_decorator
    @info_decorator
    def spawn(self, game_map):

        self.position = choice(range(game_map.mapsize * game_map.mapsize))

        row, col = self.position // game_map.mapsize, self.position % game_map.mapsize

        while game_map.game_map[row][col] == -1 or game_map.game_map[row][col] == 1:

            self.position = choice(range(game_map.mapsize * game_map.mapsize))
            row, col = self.position // game_map.mapsize, self.position % game_map.mapsize

        self.position = []
        self.position.append(row)
        self.position.append(col)  

        self.attacked = False   

