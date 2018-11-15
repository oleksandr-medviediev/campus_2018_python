import logging
from my_decorator import log_wrapper, debug_wrapper
from random import shuffle
from random import randrange


EMPTY_CELL = '#'
TREASURE = 'T'
TRAP = 'C'
PLAYER = 'P'
TRAPPED_PLAYER = 'X'
CELL_TYPES_INFO_MESSAGES = {TREASURE: 'There is a treasure nearby', TRAP: 'Careful! A trap is near'}


@log_wrapper
@debug_wrapper
def map_size_input():
    """
    Prompts user to enter map size until it meets set requirements

    :return: map size
    :rtype: int
    """

    map_size = 0

    while True:

        user_input = input("Enter map size(min - 5, max - 50): ")

        if not user_input.isdigit():

            print('Invalid input, try again')
            continue

        map_size = int(user_input)

        if map_size >= 5 and map_size <= 50:
            break

        print('Invalid map size, try again')

    return map_size


@log_wrapper
@debug_wrapper
def generate_player_position(generated_map):
    """
    Generates random position for player

    :param list generated_map: list with generated empty cells, traps and treasures
    :return: generated map with placed player
    :rtype: list
    """

    generated_map_with_player = generated_map
    player_position = 0

    while True:
        
        player_position = randrange(len(generated_map_with_player))

        if generated_map_with_player[player_position] == EMPTY_CELL:

            generated_map_with_player[player_position] = PLAYER
            break

    return generated_map_with_player


@log_wrapper
@debug_wrapper
def get_player_position(generated_map):
    """
    Returns player position

    :return: tuple with player position indeces (row, column)
    :rtype: tuple
    """

    player_position = (None, None)

    for i, row in enumerate(generated_map):
        for j, column in enumerate(row):

            if column == PLAYER:

                player_position = (i, j)
                break
        
        if player_position[0] != None:
            break

    return player_position


@log_wrapper
@debug_wrapper
def generate_map():
    """
    Generates map of given size with player, traps and treasures

    :return: tuple with list of lists as map, treasures amount in int and player position tuple (row, column)
    :rtype: tuple 
    """

    map_size = map_size_input()

    map_area = map_size * map_size

    treasures_amount = map_area // 20

    traps_amount = map_area // 10

    empty_cells_amount = map_area - treasures_amount - traps_amount
    
    print('Generating map')
    generated_map = []

    generated_map.extend([TREASURE for x in range(0, treasures_amount)])
    generated_map.extend([TRAP for x in range(0, traps_amount)])
    generated_map.extend([EMPTY_CELL for x in range(0, empty_cells_amount)])

    generated_map = generate_player_position(generated_map)

    shuffle(generated_map)

    generated_map = [generated_map[i : i + map_size] for i in range(0, len(generated_map), map_size)]

    player_position = get_player_position(generated_map)

    return (generated_map, treasures_amount, player_position)
