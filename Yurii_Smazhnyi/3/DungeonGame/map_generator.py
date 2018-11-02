import random
from math import sqrt


GROUND_SYMBOL = 'O'
TRAP_SYMBOL = 'X'
PLAYER_SYMBOL = 'T'
TREASURE_SYMBOL = '='

TRAP_COUNT = 5
TREASURE_COUNT = 2


def create_map(map_size):
    """
    Create Map for Dungeon Game.

    :param map_size: size of map.
    :map_size type: int.
    :returns: created map with traps and treasures.
    :rtype: list of strings.
    """

    ground_count = (map_size * map_size) - TRAP_COUNT - TREASURE_COUNT

    str_map = GROUND_SYMBOL * ground_count
    str_map += TRAP_SYMBOL * TRAP_COUNT
    str_map += TREASURE_SYMBOL * TREASURE_COUNT

    str_map = list(str_map)
    random.shuffle(str_map)
    str_map = "".join(str_map)

    final_map = [str_map[i:i+map_size] for i in range(0, map_size*map_size, map_size)]

    return final_map


if __name__ == "__main__":
    my_map = create_map(5)
    for i in range(len(my_map)):
        print("".join(my_map[i]))