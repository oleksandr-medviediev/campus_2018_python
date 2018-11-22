
import decorators
import creature


class Player(creature.Creature):
    """defines game player
    """

    @decorators.debug_decorator
    def __init__(self, row, col, health):
        """initialzie player instance

        Arguments:
            row {int} -- row on game map
            col {int} -- column on game map
            health {int} -- player health
        """
        super().__init__(row, col, health)
        self.__bag = 0

    @decorators.debug_decorator
    def grant_treasure(self, treasure_value):
        """grant player a treasure and increase bag size

        Arguments:
            treasure_value {int} -- number of points to add to bag
        """
        self.__bag += treasure_value

    @property
    def bag(self):
        return self.__bag
