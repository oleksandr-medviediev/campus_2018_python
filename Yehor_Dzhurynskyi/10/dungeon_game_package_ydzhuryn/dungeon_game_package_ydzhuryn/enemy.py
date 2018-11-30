import random
from . import dungeon_game_logger
from . import dungeon_game_error
from .character import Character
from .level import Level


class Enemy(Character):

    def __init__(self, level):

        super().__init__()

        self.x, self.y = level.random_inner_point()
        self.__level = level

    def respawn(self):
        """
        reset enemy's position to random inner point
        """

        self.x, self.y = self.__level.random_inner_point()

    def move(self):
        """
        move in random direction
        """

        while True:

            try:
                desired_x, desired_y = random.choice([(1, 0), (-1, 0), (0, 1), (0, -1)])
                self.__level.cell_at(self.x + desired_x, self.y + desired_y)
                self.x += desired_x
                self.y += desired_y
                break

            except dungeon_game_error.CellOutOfBoundsDungeonGameError:
                continue
