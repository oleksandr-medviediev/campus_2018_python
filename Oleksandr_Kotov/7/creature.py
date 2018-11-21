
import decorators


class Creature:
    """defines basic live game creature
    """

    @decorators.debug_decorator
    def __init__(self,  row=0, col=0, health=0):
        """init object with position

        Keyword Arguments:
            row {int} -- row on game map (default: {0})
            col {int} -- column on game map (default: {0})
            health {int} -- creature health (default: {0})

        """
        self.__health = health
        self.__curr_row = row
        self.__curr_col = col

    @property
    def position(self):
        return self.__curr_row, self.__curr_col

    def set_position(self, row, col):
        """set object position

        Arguments:
            row {int} -- row on game map
            col {int} -- column on game map
        """

        self.__curr_row = row
        self.__curr_col = col

    @decorators.debug_decorator
    def damage(self, damage):
        """deal damage to creature

        Arguments:
            damage {int} -- number of points to decrement from health
        """

        self.__health -= damage

    @property
    @decorators.debug_decorator
    def health(self):
        return self.__health
        