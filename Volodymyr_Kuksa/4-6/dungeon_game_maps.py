from random import randint
from random import shuffle
import dungeon_game_decorators

GAME_CHARACTERS = {'Empty': ' ', 'Trap': 'X', 'Treasure': 'O', 'Spawn': '@', 'Visited': '.'}


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
    traps_quantity = size_total // 10
    empty_quantity = size_total - (treasure_quantity + traps_quantity)

    characters = []

    characters.extend([GAME_CHARACTERS['Empty']] * empty_quantity)
    characters.extend([GAME_CHARACTERS['Trap']] * traps_quantity)
    characters.extend([GAME_CHARACTERS['Treasure']] * treasure_quantity)

    shuffle(characters)

    return characters


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
def generate_map(size):
    """
    Return square game map of dimensions size x size filled with randomly placed objects.

    :param size: size of map side.
    :type size: int.

    :return: game map.
    :rtype: list.
    """
    characters = generate_flat_map(size * size)
    game_map = split_rows(size, characters)

    return game_map


@dungeon_game_decorators.log_decor
@dungeon_game_decorators.debug_decor
def game_map_to_string(game_map):
    """
    Return visual representation of game map with border and legend.

    :param game_map: map to print.
    :type game_map: 2d list of one-character strings.

    :return: visual representation of game map with border and legend.
    :rtype: str.
    """
    horizontal_border = ''.join(['+', '-' * len(game_map[0]), '+'])

    result = [horizontal_border]

    for row in game_map:
        result.append(''.join(['|', ''.join(row), '|']))

    result.append(horizontal_border)

    result.append(f"{GAME_CHARACTERS['Treasure']} - treasures.")
    result.append(f"{GAME_CHARACTERS['Trap']} - traps.")
    result.append(f"{GAME_CHARACTERS['Spawn']} - spawn point.")
    result.append(f"{GAME_CHARACTERS['Visited']} - visited tiles.")

    result = '\n'.join(result)

    return result


if __name__ == '__main__':

    new_map = generate_map(randint(5, 10))
    print(game_map_to_string(new_map))
