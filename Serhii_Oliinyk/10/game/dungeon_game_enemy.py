from random import choice


class Enemy:
    def __init__(self):
        self.__position = [0, 0]


    def update_direction(self, directions):
        """
        Choose random direction fro enemy.

        :param directions: list of possible directions.
        :type my_map: list.

        :return: None.

        """
        new_direction = choice(directions)

        if new_direction == "left":
            self.__position[1] -= 1
        elif new_direction == "right":
            self.__position[1] += 1
        elif new_direction == "up":
            self.__position[0] -= 1
        elif new_direction == "down":
            self.__position[0] += 1


    @property
    def position(self):
        return self.__position


    @position.setter
    def position(self, position):
        self.__position = position
