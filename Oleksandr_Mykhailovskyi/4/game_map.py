from map_generator import generate_random_map

from logging_utility import logger
from logging_utility import logging_debug_decorator
from logging_utility import logging_info_decorator

from game_exceptions import LogicalError


class Position:
    """
    Wrapper for 2D coordinates.
    """
    def __init__(self, x, y):
        """
        Initializes public x, y coordinates.

        Args:
            x (int): x-coordinate.
            y (int): y-coordinate.
        """
        self.x = x
        self.y = y

    def __repr__(self):
        return f'{self.x} {self.y}'

    def __str__(self):
        return f'{self.x} {self.y}'

    def clamp(self, min, max):
        """
        Clamps to [min, max)
        Args:
            min (Position): min value.
            max (Position): max value.
        """
        self.x = self.x if self.x >= min.x else min.x
        self.y = self.y if self.y >= min.y else min.y

        self.x = self.x if self.x < max.x else max.x - 1
        self.y = self.y if self.y < max.y else max.y - 1


class Map:
    """
    Map class
    """
    @logging_debug_decorator
    @logging_info_decorator
    def __init__(self, size, treasures, traps):
        """
        Initializes Map instance. If any of
        given argument < 0 -> initialized with 0.
        Additionally initializes:
            default cell representations(self.reprs),
            default cell probabilities(self.probabilities),
            default randomized map(self.map(i,j)),
            default view(self.view).

        Args:
            size (Position): non-negative by any argument size.
            treasures (int): amount of treasures.
            traps (int): amount of traps.
        """
        if size.x < 0:
            size.x = -size.x
        if size.y < 0:
            size.y = -size.y

        if size.x != size.y:
            size.x = size.y

        if treasures < 0 or treasures > size.x:
            treasures = 0
        if traps < 0 or traps > size.x:
            traps = 0

        self.__size = size

        # cell representations
        self.reprs = {
            "nothing": ".",
            "treasure": "!",
            "trap": "x",
            "fog": "-",
            "unknown": "?",
            "player": "P",
            "enemy": "E"
            }

        # cell probabilities
        self.probabilities = {
            "nothing": 17/20,
            "treasure": 1/20,
            "trap": 1/10
            }

        self.cell_quantities = {
            "nothing": size.x * size.x - treasures - traps,
            "treasure": treasures,
            "trap": traps
        }

        # map
        self.__game_map = \
            generate_random_map(self.cell_quantities, self.reprs, size=self.size.x, probabilistic=False)

        # view
        self.view = Position(1, 1)

    @property
    def size(self):
        return self.__size

    def treasures(self):
        return self.cell_quantities["treasures"]

    def traps(self):
        return self.cell_quantities["traps"]

    @property
    def game_map(self):
        return self.__game_map

    @game_map.setter
    def game_map(self, game_map):
        self.__game_map = game_map
        self.size.x = len(game_map)
        self.size.y = len(game_map)

    def map_wrapper(self, position):
        return self.__game_map[position.y][position.x]

    def get_cell_repr(self, player_pos, pos):
        """
        Returns str representation of pos(i, j).

        Args:
            player_pos (Position): player position.
            pos (Position): map cell coordinates.
        Returns:
            str - str represantion of cell regarding visibility.
        """
        if pos.x >= self.size.x or \
           pos.y >= self.size.y or \
           pos.x < 0 or pos.y < 0:
            raise ValueError("incorrect map indices.")

        mrepr = ""
        if pos.x == player_pos.x and pos.y == player_pos.y:
            mrepr = self.reprs["player"]
        elif pos.x > player_pos.x + self.view.x or \
                pos.x < player_pos.x - self.view.x or \
                pos.y > player_pos.y + self.view.y or \
                pos.y < player_pos.y - self.view.y:
            mrepr = self.reprs["fog"]
        elif self.__game_map[pos.y][pos.x] == self.reprs["treasure"] or \
                self.__game_map[pos.y][pos.x] == self.reprs["trap"]:
            mrepr = self.reprs["unknown"]
        else:
            mrepr = self.__game_map[pos.y][pos.x]
        return mrepr

    @logging_debug_decorator
    @logging_info_decorator
    def show(self, player_pos, enemies_pos):
        """
        Prints map.

        Args:
            player_pos (Position): player position.
        """

        mlist = []
        for i in range(self.size.x):
            for j in range(self.size.y):
                pass
                mlist.append(self.get_cell_repr(player_pos, Position(j, i)))
            mlist.append("\n")

        # show enemies
        for enemy_pos in enemies_pos:
            mlist[enemy_pos.y*(self.size.y+1)+enemy_pos.x] = self.reprs["enemy"]
        print(''.join(mlist))

    @logging_debug_decorator
    @logging_info_decorator
    def check(self):
        if self.size.x != self.size.y:
            raise LogicalError("Map size.x must be = size.y.")
        if self.size.x != len(self.__game_map):
            raise LogicalError("Map size argument is not de-facto size.")

        for line in self.__game_map:
            if self.size.x != len(line):
                raise LogicalError("Incorrect line size in map.")

            for element in line:
                if element not in self.reprs.values():
                    raise ValueError

        size_sq = self.size.x ** 2

        if size_sq < self.cell_quantities["nothing"] or \
           size_sq < self.cell_quantities["treasures"] or \
           size_sq < self.cell_quantities["traps"]:
            raise LogicalError(f'{size_sq} is less than of of cell quantities.')

        for probability in self.probabilities.values():
            if probability > 1:
                raise LogicalError(f'Probability {probability} is more than 1.')
