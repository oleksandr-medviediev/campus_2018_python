import logging
from random import shuffle
from random import randrange


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

debug_formatter = logging.Formatter('%(asctime)s - %(name)s - %(message)s')
info_formatter = logging.Formatter('%(message)s')

file_handler = logging.FileHandler('DebugLog.txt')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(debug_formatter)

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)
stream_handler.setFormatter(info_formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)


EMPTY_CELL = '#'
TREASURE = 'T'
TRAP = 'C'
PLAYER = 'P'
TRAPPED_PLAYER = 'X'
CELL_TYPES_INFO_MESSAGES = {TREASURE: 'There is a treasure nearby', TRAP: 'Careful! A trap is near'}


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


def generate_player_position(generated_map):
    """
    Generates random position for player

    :param list generated_map: list with generated empty cells, traps and treasures
    :return: generated map with placed player
    :rtype: list
    """

    logger.debug('Entered generate_player_position(generated_map) function')

    generated_map_with_player = generated_map
    player_position = 0

    logger.debug('Generating player position')
    while True:
        
        player_position = randrange(len(generated_map_with_player))

        if generated_map_with_player[player_position] == EMPTY_CELL:

            logger.debug('Player position generated')
            generated_map_with_player[player_position] = PLAYER
            break

    logger.debug('Returning generated_map_with_player')
    return generated_map_with_player


def get_player_position(generated_map):
    """
    Returns player position

    :return: tuple with player position indeces (row, column)
    :rtype: tuple
    """

    logger.debug('Entered get_player_position(generated_map) function')
    player_position = (None, None)

    logger.debug('Finding player')
    for i, row in enumerate(generated_map):

        for j, column in enumerate(row):

            if column == PLAYER:

                logger.debug('Player is found')
                player_position = (i, j)
                break
        
        if player_position[0] != None:
            break

    logger.debug('Returning from get_player_position(generated_map)')
    return player_position


def generate_map():
    """
    Generates map of given size with player, traps and treasures

    :return: tuple with list of lists as map, treasures amount in int and player position tuple (row, column)
    :rtype: tuple 
    """

    logger.debug('Entered generate_map() function')

    map_size = map_size_input()

    logger.debug('Calculating map area')
    map_area = map_size * map_size

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

    logger.debug('Placing player')
    generated_map = generate_player_position(generated_map)

    logger.debug('Shuffling map')
    shuffle(generated_map)

    logger.debug('Splitting on rows')
    generated_map = [generated_map[i : i + map_size] for i in range(0, len(generated_map), map_size)]

    logger.debug('Getting player position')
    player_position = get_player_position(generated_map)

    logger.debug('Returning generated data from generate_map()')
    return (generated_map, treasures_amount, player_position)
