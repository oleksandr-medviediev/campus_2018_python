import logging
from random import shuffle
import dungeon_game_decorators

GAME_CHARACTERS = {'Empty': ' ', 'Trap': 'X', 'Treasure': 'O', 'Spawn': '@', 'Visited': '.'}
VECTORS_TO_ADJACENT_TILES = ((0, -1), (0, 1), (1, 0), (-1, 0))


class GameMap:

    def __init__(self, map_size=0):
        """
        GameMap constructor.

        :param map_size: size of the map to be constructed.
        :type map_size: int.
        """
        self.__map_size = map_size

        if map_size > 0:
            self.__game_map = GameMap.generate_game_map(map_size)
        else:
            self.__game_map = []

    @staticmethod
    @dungeon_game_decorators.log_decor
    @dungeon_game_decorators.debug_decor
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
    @dungeon_game_decorators.log_decor
    @dungeon_game_decorators.debug_decor
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
    @dungeon_game_decorators.log_decor
    @dungeon_game_decorators.debug_decor
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

    @dungeon_game_decorators.log_decor
    @dungeon_game_decorators.debug_decor
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

    @dungeon_game_decorators.log_decor
    @dungeon_game_decorators.debug_decor
    def get_tile_character(self, position_x, position_y):
        """
        Return game map character on position with coordinates position_x and position_y.

        :param position_x: x coordinate of the position.
        :type position_x: int.

        :param position_y: y coordinate of the position.
        :type position_y: int.

        :return: Game map character on position.
        :rtype: single-character str.
        """
        return self.__game_map[position_y][position_x]

    @dungeon_game_decorators.log_decor
    @dungeon_game_decorators.debug_decor
    def mark_tile_as_visited(self, position_x, position_y):
        """
        Mark game tile on position with coordinates position_x and position_y as visited.

        :param position_x: x coordinate of the position.
        :type position_x: int.

        :param position_y: y coordinate of the position.
        :type position_y: int.
        """
        self.__game_map[position_y][position_x] = GAME_CHARACTERS['Visited']

    @dungeon_game_decorators.log_decor
    @dungeon_game_decorators.debug_decor
    def print_state_on_position(self, position_x, position_y):
        """

        :param position_x:
        :param position_y:
        :return:
        """
        treasures = 0
        traps = 0

        for offset in VECTORS_TO_ADJACENT_TILES:

            adjacent_x = position_x + offset[0]
            adjacent_y = position_y + offset[1]

            if not 0 <= adjacent_x < self.__map_size or not 0 <= adjacent_y < self.__map_size:
                continue

            adjacent_tile = self.__game_map[adjacent_y][adjacent_x]

            if adjacent_tile == GAME_CHARACTERS['Treasure']:
                treasures += 1
            elif adjacent_tile == GAME_CHARACTERS['Trap']:
                traps += 1

        GameMap.output_map_state(treasures, traps)

    @staticmethod
    @dungeon_game_decorators.log_decor
    @dungeon_game_decorators.debug_decor
    def output_map_state(treasures, traps):
        """
        Output information about nearby treasures and traps.

        :param treasures: number of treasures in tiles, adjacent to the player.
        :type treasures: int.

        :param traps: number of traps in tiles, adjacent to the player.
        :type traps: int.

        :return: None.
        """
        if treasures == 1:
            logging.info('There is a treasure nearby!')
        elif treasures:
            logging.info('There are multiple treasures nearby!')

        if traps == 1:
            logging.info('There is a trap nearby!')
        elif traps:
            logging.info('There are multiple traps nearby!')

        if not treasures and not traps:
            logging.info('There is nothing nearby.')

    @property
    def game_map(self):
        """
        game_map getter.

        :return: game map.
        :rtype: 2d list of single-character strings.
        """
        return self.__game_map

    @game_map.setter
    def game_map(self, new_map):
        """
        game_map setter.

        :param new_map: new game map.
        :type new_map: 2d list of single-character str.
        """
        self.__game_map = new_map
        self.__map_size = len(new_map[0])

    def __str__(self):
        """
        Return visual representation of game map with border and legend.

        :return: visual representation of game map with border and legend.
        :rtype: str.
        """
        horizontal_border = ''.join(['+', '-' * self.__map_size, '+'])

        result = [horizontal_border]

        for row in self.__game_map:
            result.append(''.join(['|', ''.join(row), '|']))

        result.append(horizontal_border)

        result.append(f"{GAME_CHARACTERS['Treasure']} - treasures.")
        result.append(f"{GAME_CHARACTERS['Trap']} - traps.")
        result.append(f"{GAME_CHARACTERS['Spawn']} - spawn point.")
        result.append(f"{GAME_CHARACTERS['Visited']} - visited tiles.")

        result = '\n'.join(result)

        return result
