from random import randint
from character import Character
import dungeon_game_decorators

PLAYER_MOVES = {'u': (0, -1), 'd': (0, 1), 'l': (-1, 0), 'r': (1, 0)}


class Player(Character):

    def __init__(self, name):
        """
        Player constructor.

        :param name: name of the player.
        :type name: str.
        """
        super().__init__(name)

        self.__position_x = 0
        self.__position_y = 0

    @dungeon_game_decorators.log_decor
    @dungeon_game_decorators.debug_decor
    def calculate_new_position(self, move_name):
        """
        Return new player position.

        :param move_name: name of the move to be executed.
        :type move_name: single character str.

        :return: (position_x, position_y).
        :rtype: (int, int).
        """
        new_x = self.__position_x + PLAYER_MOVES[move_name][0]
        new_y = self.__position_y + PLAYER_MOVES[move_name][1]

        return new_x, new_y

    @dungeon_game_decorators.log_decor
    @dungeon_game_decorators.debug_decor
    def set_position(self, position_x, position_y):
        """
        Set new player position.

        :param position_x: x coordinate of new position.
        :type position_x: int.

        :param position_y: y coordinate of new position.
        :type position_y: int.
        """
        self.__position_x, self.__position_y = position_x, position_y

    @dungeon_game_decorators.log_decor
    @dungeon_game_decorators.debug_decor
    def get_position(self):
        """
        Return player position as a cortege: (position_x, position_y).

        :return: (position_x, position_y).
        :rtype: (int, int).
        """
        return self.__position_x, self.__position_y

    @dungeon_game_decorators.log_decor
    @dungeon_game_decorators.debug_decor
    def randomize_position(self, map_size):
        """
        Set player to random position.

        :param map_size: size of game map.
        :type map_size: int.
        """
        self.__position_x = randint(0, map_size - 1)
        self.__position_y = randint(0, map_size - 1)

    def __str__(self):
        """
        Return str with player stats.

        :return: str with player stats.
        :rtype: str.
        """
        return f'{self.character_name}: HP: {self.hp}, BAG: {self.bag}'
