import random


GROUND_SYMBOL = 'O'
TRAP_SYMBOL = 'X'
PLAYER_SYMBOL = 'T'
TREASURE_SYMBOL = '='

TRAP_MODIFIER = 10
TREASURE_MODIFIER = 20


def create_map(map_size):
    """
    Create Map for Dungeon Game.

    :param map_size: size of map.
    :map_size type: int.
    :returns: created map with traps and treasures.
    :rtype: list of strings.
    """
    
    trap_count = (map_size * map_size) // TRAP_MODIFIER
    treasure_count = (map_size * map_size) // TREASURE_MODIFIER
    ground_count = (map_size * map_size) - trap_count - treasure_count - 1

    str_map = GROUND_SYMBOL * ground_count
    str_map += TRAP_SYMBOL * trap_count
    str_map += TREASURE_SYMBOL * treasure_count
    str_map += PLAYER_SYMBOL

    str_map = list(str_map)
    random.shuffle(str_map)
    str_map = "".join(str_map)

    final_map = [str_map[i:i+map_size] for i in range(0, map_size*map_size, map_size)]

    return final_map


if __name__ == "__main__":
    my_map = create_map(10)
    for i in range(len(my_map)):
        print((my_map[i]))
