from MyLogger import logger
from random import shuffle

EMPTY_CELL = '#'
TREASURE = 'T'
TRAP = 'C'

def map_size_input():
    """
    Prompts user to enter map size until it meets set requirements

    :return: map size
    :rtype: int
    """

    logger.debug('Entered map_size_input() function')

    map_size = 0

    logger.debug('Entered input loop')
    while True:

        logger.debug('Waiting fro user input')
        user_input = input("Enter map size(min - 5, max - 50): ")

        logger.debug('Validating input')
        if not user_input.isdigit():
            logger.info('Invalid input, try again')
            continue

        logger.debug('Casting user unput to int')
        map_size = int(user_input)

        logger.debug('Validating map size')
        if map_size >= 5 and map_size <= 50:

            logger.debug('Size validation successful')
            break

        logger.info('Invalid map size, try again')

    logger.debug('Returning from map_size_input() function')
    return map_size


def generate_map(size):
    """
    Generates map of given size

    :param int size: size of map
    :return: list of lists as map 
    """

    logger.debug('Entered generate_map(size) function')

    logger.debug('Calculating map area')
    map_area = size * size

    logger.debug('Calculating treasures amount')
    treasures_amount = map_area // 20

    logger.debug('Calculating traps amount')
    traps_amount = map_area // 10

    logger.debug('Calculating empty cells')
    empty_cells_amount = map_area - treasures_amount - traps_amount
    
    logger.info('Generating map')
    generated_map = []

    logger.debug('Adding treasures')
    generated_map.extend([TREASURE for x in range(0, treasures_amount)])

    logger.debug('Adding traps')
    generated_map.extend([TRAP for x in range(0, traps_amount)])

    logger.debug('Adding empty cells')
    generated_map.extend([EMPTY_CELL for x in range(0, empty_cells_amount)])

    logger.debug('Shuffling items')
    shuffle(generated_map)

    logger.debug('Splitting on rows')
    generated_map = [generated_map[i : i + size] for i in range(0, len(generated_map), size)]

    logger.debug('Returning generated_map')
    return generated_map

input = map_size_input()

gen_map = generate_map(input)

for i in range(0, len(gen_map)):
    print(gen_map[i])
