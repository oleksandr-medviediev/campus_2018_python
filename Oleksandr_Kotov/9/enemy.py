
import random

import creature


class Enemy(creature.Creature):
    """defines game enemy
    """

    def __init__(self,  scale):
        """init enemy with map scale

        Keyword Arguments:
            row {int} -- row on game map (default: {0})
            col {int} -- column on game map (default: {0})
            health {int} -- creature health (default: {0})

        """
        super().__init__(row=random.randint(0, scale - 1),
                         col=random.randint(0, scale - 1),
                         health=1)

        self.__scale = scale

    def move(self):

        neighbour_positions = []

        curr_row, curr_col = self.position

        if curr_row < self.__scale - 1:
            neighbour_positions.append((curr_row + 1, curr_col))

        if curr_row > 0:
            neighbour_positions.append((curr_row - 1, curr_col))

        if curr_col < self.__scale - 1:
            neighbour_positions.append((curr_row, curr_col + 1))

        if curr_col > 0:
            neighbour_positions.append((curr_row, curr_col - 1))

        new_position = random.choice(neighbour_positions)

        self.set_position(*new_position)
