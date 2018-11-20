import logging
from random import shuffle

GAME_CHARACTERS = {'Empty': ' ', 'Trap': 'X', 'Treasure': 'O', 'Spawn': '@', 'Visited': '.'}


class GameMap:

    def __init__(self, map_size):

        self.__map_size = map_size
        self.__game_map = GameMap.generate_game_map(map_size)

    @staticmethod
    def generate_game_map(map_size):
        """
        Return square game map of dimensions size x size filled with randomly placed objects.

        :param map_size: size of map side.
        :type map_size: int.

        :return: game map.
        :rtype: list.
        """
        characters = GameMap.generate_flat_map(map_size * map_size)
        game_map = GameMap.split_rows(map_size, characters)

        return game_map

    @staticmethod
    def generate_flat_map(size_total):
        """
        Return an array of randomly generated characters that represent a sequence of all rows in game map.

        :param size_total: the total size of game map.
        :type size_total: int.

        :return: an array of randomly generated characters that represent a sequence of all rows in game map.
        :rtype: list.
        """
        treasure_quantity = size_total // 20

        if treasure_quantity < 3:
            treasure_quantity = 3

        traps_quantity = size_total // 10

        if traps_quantity < 3:
            traps_quantity = 3

        empty_quantity = size_total - (treasure_quantity + traps_quantity)

        characters = []

        characters.extend([GAME_CHARACTERS['Empty']] * empty_quantity)
        characters.extend([GAME_CHARACTERS['Trap']] * traps_quantity)
        characters.extend([GAME_CHARACTERS['Treasure']] * treasure_quantity)

        shuffle(characters)

        return characters

    @staticmethod
    def split_rows(size, characters):
        """
        Return an array of batches of characters of size length each.

        :param size: length of one batch.
        :type size: int.

        :param characters: characters that are split into batches.
        :type characters: iterable.

        :return: array of batches of characters of size length each.
        :rtype: list.
        """
        game_map = []

        for i in range(size):

            row = characters[i * size: i * size + size]
            game_map.append(row)

        return game_map

    def is_valid_position(self, position_x, position_y):
        """
        Return True if position with coordinates position_x and position_y is valid, False otherwise.

        :param position_x: x coordinate of the position.
        :type position_x: int.

        :param position_y: y coordinate of the position.
        :type position_y: int.

        :return: True if position is valid, False otherwise.
        """
        if 0 <= position_x < self.__map_size and 0 <= position_y < self.__map_size:

            is_valid = True

        else:

            logging.info('That path is blocked!')
            is_valid = False

        return is_valid
