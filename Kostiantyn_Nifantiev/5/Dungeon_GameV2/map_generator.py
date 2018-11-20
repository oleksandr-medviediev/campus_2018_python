from random import randint
from random import shuffle
from math import ceil
from dungeon_logger import my_logger


def dungeon_map_generator(width = 20, height = 10):
    """
    Generates random map with at least 10% cells occupied with traps and 5% with treasures.
    Rounding quantity of special cells performed to higher value (ceil)
    """

    my_logger.debug("Checking correctness of input...")

    if not (isinstance(width, int) and isinstance(height, int)):
        
        my_logger.info('Wrong cell size! Width and height should be positive integers\n')
        return None

    if width < 2:

        width = 2

    elif width > 119:

        width = 119

    if height < 2:

        height = 2

    elif height > 30:

        height = 30

    my_logger.debug("Input check done")

    
    my_logger.debug("Calculating amount of traps and treasures...")

    cells_count = width * height
    treasures_count = ceil((cells_count) / 20)
    trap_count = ceil((cells_count) / 10)

    my_logger.debug("Traps and treasures quantity has been calculated")

    my_logger.debug("Generating map...")

    dungeon_map = ['T' for x in range(0, treasures_count)]
    dungeon_map.extend(['X' for x in range(0, trap_count)])
    dungeon_map.extend(['-' for x in range(0, cells_count - treasures_count - trap_count)])

    shuffle(dungeon_map)

    dungeon_map = [dungeon_map[x * width : x * width + width] for x in range(0, height)]

    my_logger.debug("Map has been generated")

    return dungeon_map
