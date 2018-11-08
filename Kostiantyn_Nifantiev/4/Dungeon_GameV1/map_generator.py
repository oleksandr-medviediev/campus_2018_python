from random import randint
from random import shuffle
from math import ceil


def dungeon_map_generator(width = 20, height = 10):
    """
    Generates random map with at least 10% cells occupied with traps and 5% with treasures.
    Rounding quantity of special cells performed to higher value (ceil)
    """
    if not (isinstance(width, int) and isinstance(height, int)):
        
        print('Wrong cell size! Width and height should be positive integers\n')
        return None

    if width < 2:

        width = 2

    elif width > 119:

        width = 119

    if height < 2:

        height = 2

    elif height > 30:

        height = 30

    cells_count = width * height
    treasures_count = ceil((cells_count) / 20)
    trap_count = ceil((cells_count) / 10)

    dungeon_map = ['T' for x in range(0, treasures_count)]
    dungeon_map.extend(['X' for x in range(0, trap_count)])
    dungeon_map.extend(['-' for x in range(0, cells_count - treasures_count - trap_count)])

    shuffle(dungeon_map)

    dungeon_map = [dungeon_map[x * width : x * width + width] for x in range(0, height)]

    return dungeon_map
