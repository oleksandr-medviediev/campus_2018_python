from random import randint
from itertools import product

from DungeonLogger import main_logger
from DungeonLogger import debugger_output

from WorldInitError import WorldInitError
from DataLoadError import DataLoadError
from PlayerMoveError import PlayerMoveError


class World:
    """
    Defines in game world
    """
    
    empty = '~'
    player = '*'

    treasure = '$'
    explored = '.'

    trap = 'x'
    enemy = '@'

    @debugger_output()
    def __init__(self, size):
        """
        Constructs world

        :param size: defines map bounds
        """

        if size <= 0:
            raise WorldInitError

        self.__world = [[World.empty for _ in range(size)] for _ in range(size)]
        self.__player_position = [0, 0]
        self.__enemy_position = [0, 0]
        self.__old_item = World.empty
        self.__enemy = None


    @debugger_output()
    def init_player_position(self, x, y):
        """
        Sets initial players position value

        :param x: x axis coordinate
        :param y: y axis coordinate
        """

        self.__player_position = [x, y]
        self.world[y][x] = World.player


    @debugger_output()
    def init_enemy_position(self, enemy):
        """
        Sets initial enemy position value

        :param enemy: enemy object
        """

        self.__enemy_position = [enemy.x, enemy.y]
        self.__enemy = enemy
        self.world[enemy.y][enemy.x] = World.enemy


    @debugger_output()
    def fill_the_map(self, amount_of_items, item):
        """
        Fills map with given amount of items

        :param world: map to fill
        :param amount_of_items: amount of items to spawn
        :param item: item to spawn
        :return: nothing
        :rtype: None
        """

        size = len(self.__world)
        i = 0

        while i < amount_of_items:
            x = randint(0, size - 1)
            y = randint(0, size - 1)

            if self.__world[y][x] == item:
                continue

            else:
                self.__world[y][x] = item
                i += 1


    @debugger_output()
    def save(self, save):
        """
        Saves map state to save

        :param save: dict
        """

        save['map'] = self.__world
        save['map_player'] = self.__player_position



    @debugger_output()
    def load(self, save):
        """
        Loads map state from save

        :param save: dict with map state
        """
        
        is_valid = isinstance(save, dict)
        if not is_valid:
            raise DataLoadError

        self.__world = save['map']
        self.__player_position = save['map_player']


    @debugger_output()
    def size(self):
        """
        Returns map size

        :rtype: int
        """

        size = len(self.__world)
        return size


    @property
    def world(self):
        """
        Returns world
        """

        return self.__world


    @world.setter
    @debugger_output()
    def world(self, world):
        """
        Sets world

        :rtype: None
        """

        self.__world = world


    @debugger_output()
    def update_player_position(self, player, x, y):
        """
        Updates player according to it's position

        :param player: player object
        :param x: x axis coordinate
        :param y: y axis coordinate
        :rtype: None
        """

        if not self._is_valid_position(x, y):
            raise PlayerMoveError

        item = self.__world[y][x]

        if item == World.treasure:
            player.treasures += 1
            main_logger.info("You've found a treasure!\n")
        
        elif item == World.trap:
            player.health -= 1
            main_logger.info("You've got in trap! You've lost one health =/\n")

        elif item == World.enemy:
            player.health -= 1
            main_logger.info("You've been attacked by enemy! You've lost one health =/\n")
            self.__enemy.reset_position()

        old = self.__player_position
        self.world[old[1]][old[0]] = World.explored

        self.__player_position = [x, y]
        self.world[y][x] = World.player


    @debugger_output()
    def update_enemy_position(self, x, y):
        """
        Updates enemy according to it's position

        :param x: x axis coordinate
        :param y: y axis coordinate
        :rtype: None
        """

        old = self.__enemy_position
        self.world[old[1]][old[0]] = self.__old_item

        self.__old_item = self.__world[y][x]
        self.__enemy_position = [x, y]

        self.world[y][x] = World.enemy


    @debugger_output()
    def is_valid_as_player_position(self, x, y):
        """
        Returns True if position is valid for player initialization
        
        :param x: x axis coordinate
        :param y: y axis coordinate
        :return: is valid
        :rtype: bool
        """

        is_valid = self.world[y][x] == World.empty
        return is_valid


    @debugger_output()
    def _is_valid_position(self, x, y):
        """
        Returns True if position is valid, False otherwise

        :param x: x axis coordinate
        :param y: y axis coordinate
        :return: is valid
        :rtype: bool
        """

        size = len(self.__world)
        valid = 0 <= x < size and 0 <= y < size

        return valid


    @debugger_output()
    def print_except(self, what_to_hide):
        """
        Prints map to string
        Elements that in what_to_hide will be replaced with World.empty

        :param what_to_hide: iterable of items
        :return: printed map
        :rtype: str
        """

        elements = []
        for i in self.__world:

            lines = ['|']
            for j in i:

                if j in what_to_hide:
                    lines.append(World.empty)
                else:
                    lines.append(j)

            lines.append('|\n')
            elements.append(''.join(lines))
        
        string = ''.join(elements)
        return string


    @debugger_output()
    def print(self):
        """
        Prints world to string

        :return: printed world
        :rtype: str
        """

        string = self.print_except([])
        return string


    @debugger_output()
    def is_around_of(self, x, y, what):
        """
        Returns true if there is 'what' around of give coordinates

        :param x: x axis coordinate
        :param y: y axis coordinare
        :param what: searching item
        :return: true if there is wanted item
        :rtype: bool
        """

        comb = product((-1, 0, 1), (-1, 0, 1))
        size = len(self.__world)

        squares = [(x + p[0], y + p[1]) for p in comb if 0 <= x + p[0] < size if 0 <= y + p[1] < size]
        result = set(map(lambda p: self.__world[p[1]][p[0]] == what, squares))

        found = True in result
        return found


    @debugger_output()
    def is_trap_near_player(self):
        """
        Returns True if there is a trap near player

        :rtype: bool
        """

        is_near = self.is_around_of(self.__player_position[0], self.__player_position[1], World.trap)
        return is_near


    @debugger_output()
    def is_treasure_near_player(self):
        """
        Returns True if there is a treasure near player

        :rtype: bool
        """

        is_near = self.is_around_of(self.__player_position[0], self.__player_position[1], World.treasure)
        return is_near
