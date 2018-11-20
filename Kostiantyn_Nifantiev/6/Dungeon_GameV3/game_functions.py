from map_generator import dungeon_map_generator
from random import randint
import pickle
from dungeon_logger import my_logger
from dungeon_logger import log_decorator


@log_decorator
def spawn_player(width, height, dungeon_map):
    """
    Parameters corresponds to map size
    """
    my_logger.debug("Trying to find empty place for palyer...")

    while True:

        player_x = randint(0, width - 1)
        player_y = randint(0, height - 1)

        if dungeon_map[player_y][player_x] != '-':

            continue

        else:

            break

    my_logger.debug("Empty place for palyer has been found")

    return [player_x, player_y]


@log_decorator
def make_move(move_direction, player_position, map_size):
    """
    Changes player position according to user input
    """

    if not move_direction in set(['w', 'd', 's', 'a']):

        my_logger.info('Wrong direction! Try again!')

    old_position = player_position[:]


    if move_direction == 'w':

        if player_position[1] > 0:

            player_position[1] -=1
            my_logger.info('You have moved up')

    elif move_direction == 'd':

        if player_position[0] < map_size[0] - 1:

            player_position[0] +=1
            my_logger.info('You have moved right')

    elif move_direction == 's':

        if player_position[1] < map_size[1] - 1:

            player_position[1] +=1
            my_logger.info('You have moved down')

    elif move_direction == 'a':

        if player_position[0] > 0:

            player_position[0] -=1
            my_logger.info('You have moved left')

    if old_position == player_position:

        my_logger.info("There is a wall!")


@log_decorator
def check_around(player_x, player_y, map_size, dungeon_map, player_map):
    """
    This function performs check for treasures/traps in surrounding cells
    """
    
    is_treasure = False
    is_trap = False

    my_logger.debug("Checking for wall near player...")

    min_row_index = player_y - 1 if player_y - 1 > 0 else 0
    max_row_index = player_y + 2 if player_y + 1 < map_size[1] else map_size[1]
    row_range = range(min_row_index, max_row_index)

    min_column_index = player_x - 1 if player_x - 1 > 0 else 0
    max_column_index = player_x + 2 if player_x + 1 < map_size[0] else map_size[0]
    column_range = range(min_column_index, max_column_index)

    my_logger.debug("Wall check done")

    my_logger.debug("Checking for treasures and traps around")

    for y in row_range:

        for x in column_range:

            if dungeon_map[y][x] == 'T':

                is_treasure = True

            elif dungeon_map[y][x] == 'X':

                is_trap = True

    if is_treasure and is_trap:

        fill_cells = '!'

    elif is_treasure:

        fill_cells = 't'

    elif is_trap:

        fill_cells = 'x'

    else:

        fill_cells = '-'

    my_logger.debug("Treasures and traps check done")

    my_logger.debug("Making output for player")

    for y in row_range:

        for x in column_range:

            if not player_map[y][x] == '-':

                player_map[y][x] = fill_cells

    player_map[player_y][player_x] = '@'

    for row in player_map:

        my_logger.info("".join(row))

    if is_treasure:

        my_logger.info('There is a treasure!')

    elif is_trap:

        my_logger.info('There is a trap!')

    my_logger.debug("Player output finished")

    return (is_treasure, is_trap)


@log_decorator
def game_loop():
    """
    Main game function contains game loop and some surrounding stuff
    """
    my_logger.debug("Game start choice")
    start_game_choice = input('Enter "y" if you want to play a new game or\n"load" if you want to load existing game:\n')
    my_logger.debug("Game start choice handling")

    if start_game_choice == "load":
        
            my_logger.info("Loading game...")
            in_file = open('dungeon.sav', 'rb')

            data = pickle.load(in_file)

            game_map = data[0]
            player_map = data[1]
            player_position = data[2]
            map_size = data[3]
            my_logger.info("Game has been loaded!")

    else:

        map_request = input('Enter preferable map size in format "width:height", or just press enter to play with default map:\n')
        my_logger.info("Generating map...")

        if not len(map_request):

            map_size = [20, 10]

        else:

            map_size = [int(token) for token in map_request.split(':')]

        game_map = dungeon_map_generator(*map_size)

        player_map = [['?' for x in range(0, map_size[0])] for y in range(0, map_size[1])]

        player_position = spawn_player(*map_size, game_map)

        my_logger.info("Map has been generated successfully!")

    my_logger.debug("Checking around...")
    check_around(*player_position, map_size, game_map, player_map)
    my_logger.debug("Check around has been done")

    my_logger.debug("Entering main game loop...")

    while True:

        move = input('\nEnter your move, please (w - up, d - right, s - down, a - left), or "save" for save game:\n')

        if move == "save":

            data = [game_map, player_map, player_position, map_size]

            out_file = open('dungeon.sav', 'wb')

            pickle.dump(data, out_file)
            break

        player_map[player_position[1]][player_position[0]] = '-'

        make_move(move, player_position, map_size)

        check_around(*player_position, map_size, game_map, player_map)

        if game_map[player_position[1]][player_position[0]] == 'T':

            my_logger.info("\n>>>This is a treasure! You are victorious!<<<\n")
            break

        elif game_map[player_position[1]][player_position[0]] == 'X':

            my_logger.info("\n}}}This is a trap! You loose!{{{\n")
            break

        else:

            continue

    my_logger.debug("Main game loop has stopped")
     
    my_logger.debug("Printing game map...")

    for row in game_map:

        my_logger.info("".join(row))

    my_logger.debug("Game map has been printed")
