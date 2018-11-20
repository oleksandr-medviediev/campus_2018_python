from character import Character

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

    def move(self, move_name):
        """
        Execute move and return new position.

        :param move_name: name of the move to be executed.
        :type move_name: single character str.

        :return: (position_x, position_y).
        :rtype: (int, int).
        """
        new_x = self.__position_x + PLAYER_MOVES[move_name][0]
        new_y = self.__position_y + PLAYER_MOVES[move_name][1]

        return new_x, new_y

    def set_position(self, position_x, position_y):
        """
        Set new player position.

        :param position_x: x coordinate of new position.
        :type position_x: int.

        :param position_y: y coordinate of new position.
        :type position_y: int.
        """
        self.__position_x, self.__position_y = position_x, position_y
