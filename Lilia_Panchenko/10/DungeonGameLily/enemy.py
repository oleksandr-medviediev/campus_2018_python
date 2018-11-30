from .logger import my_logger
from random import choice


class Enemy:
    """
    Class to control enemy. Responsible for enemy movement, player attack and spawn
    """

    def __init__(self):
        """Constructor for Enemy class"""
        self.attacked = False


    @my_logger.debug_decorator
    @my_logger.info_decorator
    def move(self, map_size):
        """
        Function to move enemy
        : param : map_size - size of game map, to avoid leaving game map
        : ptype : int
        : return : new enemy position
        : rtype : list of 2 elements
        """
        DIRECTION_TO_MOVE = [ [-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1] ]

        neighbour_cells = [[self.position[0] + direction[0], self.position[1] + direction[1]] \
        for direction in list(DIRECTION_TO_MOVE)]
        
        neighbour_cells = list(filter(lambda cell: cell[0] >= 0 and cell[1] >= 0 
            and cell[0] < map_size and cell[1] < map_size, neighbour_cells))

        self.position = choice(neighbour_cells)

        return self.position


    @my_logger.debug_decorator
    @my_logger.info_decorator
    def is_attacked_player(self, player):
        """
        Function to move enemy
        : param : player to check if one was attacked by enemy
        : ptype : Player
        : return : if player was attacked - True, otherwise - False
        : rtype : bool
        """
        self.attacked = False

        if player.position == self.position:
            self.attacked = True

        return self.attacked


    @my_logger.debug_decorator
    @my_logger.info_decorator
    def spawn(self, game_map):
        """
        Function to spawn enemy on map
        : param : game_map - represents game map
        : ptype : GameMap
        : return : None
        """
        self.position = choice(range(game_map.mapsize * game_map.mapsize))

        row, col = self.position // game_map.mapsize, self.position % game_map.mapsize

        while game_map.game_map[row][col] == -1 or game_map.game_map[row][col] == 1:

            self.position = choice(range(game_map.mapsize * game_map.mapsize))
            row, col = self.position // game_map.mapsize, self.position % game_map.mapsize

        self.position = []
        self.position.append(row)
        self.position.append(col)  

        self.attacked = False   
