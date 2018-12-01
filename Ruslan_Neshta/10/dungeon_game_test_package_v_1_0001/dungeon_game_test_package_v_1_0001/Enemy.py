from random import randint
from time import sleep

from DungeonLogger import debugger_output
from DataLoadError import DataLoadError

from Player import Player


class Enemy(Player):
    """
    Defines enemy
    """

    @debugger_output()
    def __init__(self, world):
        """
        Cunstructs enemy instance

        :param world: world map object
        """

        setted = False
        self.__world = world

        self.__x = 0
        self.__y = 0

        while not setted:
            self.__rand_my_pos(world.size())
            setted = world.is_valid_as_player_position(self.x, self.y)

        world.init_enemy_position(self)

    @debugger_output()
    def __rand_my_pos(self, max):
        """
        Randomizes player posision in given ranges

        :param max: tuple with x,y bounds
        :rtype: None
        """

        self.__x = randint(0, max - 1)
        self.__y = randint(0, max - 1)


    @debugger_output()
    def reset_position(self):
        """
        Resets position
        """

        setted = False

        while not setted:
            self.__rand_my_pos(self.__world.size())
            setted = self.__world.is_valid_as_player_position(self.x, self.y)
        
        self.__world.update_enemy_position(self.x, self.y)


    @debugger_output()
    def update(self, player):
        """
        Runs enemy logic

        :param player: player object
        """

        while True:

            setted = False
            offsets = [-1, 1]

            while not setted:

                x_offset = offsets[randint(0, 1)]
                y_offset = offsets[randint(0, 1)]

                self.__x += x_offset
                self.__y += y_offset

                setted = self.__world._is_valid_position(self.x, self.y)

            self.__world.update_enemy_position(self.x, self.y)
            self.__world.update_player_position(player, player.x, player.y)

            sleep(3)


    @debugger_output()
    def save(self, save):
        """
        Saves enemy state to save

        :param save: dict
        """
        
        save['enemy_x'] = self.__x
        save['enemy_y'] = self.__y


    @debugger_output()
    def load(self, save):
        """
        Loads enemy state from save

        :param save: dict with enemy state
        """

        is_valid = isinstance(save, dict)
        if not is_valid:
            raise DataLoadError

        self.__x = save['enemy_x']
        self.__y = save['enemy_y']
    

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
