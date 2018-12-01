from random import randint

from DungeonLogger import debugger_output
from DataLoadError import DataLoadError


class Player:
    """
    Defines in game player
    """

    @debugger_output()
    def __init__(self, world):
        """
        Cunstructs player instance

        :param world: world map object
        """

        setted = False
        self.__world = world

        self.__health = 3
        self.__treasures = 0

        self.__x = 0
        self.__y = 0

        while not setted:
            self.rand_my_pos(world.size())
            setted = world.is_valid_as_player_position(self.x, self.y)

        world.init_player_position(self.x, self.y)


    @debugger_output()
    def rand_my_pos(self, max):
        """
        Randomizes player posision in given ranges

        :param max: tuple with x,y bounds
        :rtype: None
        """

        self.__x = randint(0, max - 1)
        self.__y = randint(0, max - 1)


    @property
    @debugger_output()
    def health(self):
        """
        Returns health

        :rtype: int
        """

        return self.__health


    @health.setter
    @debugger_output()
    def health(self, hp):
        """
        Sets health

        :param hp: amount of health
        :rtype: None
        """

        self.__health = hp


    @property
    @debugger_output()
    def treasures(self):
        """
        Returns treasures

        :rtype: int
        """

        return self.__treasures


    @debugger_output()
    def save(self, save):
        """
        Saves player state to save

        :param save: dict
        """

        save['player_health'] = self.__health
        save['player_treasures'] = self.__treasures

        save['player_x'] = self.__x
        save['player_y'] = self.__y


    @debugger_output()
    def load(self, save):
        """
        Loads player state from save

        :param save: dict with players state
        """

        is_valid = isinstance(save, dict)
        if not is_valid:
            raise DataLoadError

        self.__health = save['player_health']
        self.__treasures = save['player_treasures']

        self.__x = save['player_x']
        self.__y = save['player_y']


    @treasures.setter
    @debugger_output()
    def treasures(self, treasures):
        """
        Sets treasures

        :param treasures: amount of treasures
        :rtype: None
        """

        self.__treasures = treasures


    @property
    @debugger_output()
    def x(self):
        """
        Returns x value

        :rtype: int
        """

        return self.__x


    @property
    @debugger_output()
    def y(self):
        """
        Returns y value

        :rtype: int
        """

        return self.__y


    @debugger_output()
    def up(self):
        """
        Moves player up
        """

        self.__world.update_player_position(self, self.x, self.y - 1)
        self.__y -= 1


    @debugger_output()
    def down(self):
        """
        Moves player down
        """

        self.__world.update_player_position(self, self.x, self.y + 1)
        self.__y += 1


    @debugger_output()
    def left(self):
        """
        Moves player left
        """

        self.__world.update_player_position(self, self.x - 1, self.y)
        self.__x -= 1


    @debugger_output()
    def right(self):
        """
        Moves player right
        """

        self.__world.update_player_position(self, self.x + 1, self.y)
        self.__x += 1


    @debugger_output()
    def is_alive(self):
        """
        Returns True if player is alive

        :rtype: bool
        """

        alive = self.health > 0
        return alive
