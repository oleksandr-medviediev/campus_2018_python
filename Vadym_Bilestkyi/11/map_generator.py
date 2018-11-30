from dungeon_logging import logger, with_logging
import random


@with_logging
def generate(map_size):
    new_map = [[None] * map_size for _ in range(map_size)]
    logger.debug('Empty map generated')

    for i in range(map_size**2 // 10):
        x = random.choice(range(map_size))
        y = random.choice(range(map_size))
        new_map[x][y] = 'Trap'
    logger.debug('Traps was placed')

    for i in range(map_size**2 // 20):
        x = random.choice(range(map_size))
        y = random.choice(range(map_size))
        new_map[x][y] = 'Treasure'
    logger.debug('Treasures was placed')

    return new_map
