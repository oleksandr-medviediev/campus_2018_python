import logging
import MyMapGenerator


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


PLAYER_MOVE_DIRECTIONS_NAMES = ['up', 'down', 'left', 'right']
PLAYER_MOVE_DIRECTIONS_BY_NAMES = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}


def scan_notification(cell_type):
    """
    Checks cell type and prints notification if check is passed

    :param str cell_type: type of item in cell
    """

    if cell_type != MyMapGenerator.EMPTY_CELL:
        logger.info(MyMapGenerator.CELL_TYPES_INFO_MESSAGES[cell_type])


def scan_area_around_player(player_position, game_map):
    """
    Checks cells around player for treasures and traps and prints corresponding notifications

    :param tuple current_data: tuple with current game data (map, 
        left treasures amount, player position and trapped state)
    """

    logger.debug('Entered scan_area_around_player(current_data) function')
    
    player_position_row, player_position_column = player_position
    map_side_lenght = len(game_map)
    
    cell_right = (player_position_column + 1) % map_side_lenght
    cell_left = (map_side_lenght + (player_position_column - 1)) % map_side_lenght

    cell_top = (map_side_lenght + (player_position_row - 1)) % map_side_lenght
    cell_bottom = (player_position_row + 1) % map_side_lenght
    
    logger.debug('Scanning cell from left')
    cell_type = game_map[player_position_row][cell_left]
    scan_notification(cell_type)

    logger.debug('Scanning cell from right')
    cell_type = game_map[player_position_row][cell_right]
    scan_notification(cell_type)

    logger.debug('Scanning cell from above')
    cell_type = game_map[cell_top][player_position_column]
    scan_notification(cell_type)

    logger.debug('Scanning cell from below')
    cell_type = game_map[cell_bottom][player_position_column]
    scan_notification(cell_type)

    logger.debug('Scanning top left cell')
    cell_type = game_map[cell_top][cell_left]
    scan_notification(cell_type)

    logger.debug('Scanning top right cell')
    cell_type = game_map[cell_top][cell_right]
    scan_notification(cell_type)

    logger.debug('Scanning bottom right cell')
    cell_type = game_map[cell_bottom][cell_right]
    scan_notification(cell_type)

    logger.debug('Scanning bottom left cell')
    cell_type = game_map[cell_bottom][cell_left]
    scan_notification(cell_type)

    logger.debug('Exiting scan_area_around_player(current_data) function')


def calculate_player_new_position(direction, player_position, game_map):
    """
    Calculates new player position according to given direction

    :param tuple direction: movement direction
    :param tuple player_position: current player position
    :param list game_map: current game map
    :return: tuple with new player position
    :rtype: tuple
    """

    logger.debug('Entering calculate_player_new_position(direction, player_position, game_map) function')

    direction_row, direction_column = direction
    new_player_position_row, new_player_position_column = player_position
    map_side_lenght = len(game_map)

    logger.debug('Calculation player new position')

    if direction_row > 0:

        logger.debug('User goes up')
        new_player_position_row = (new_player_position_row + 1) % map_side_lenght

    elif direction_row < 0:

        logger.debug('User goes down')
        new_player_position_row = (map_side_lenght + new_player_position_row - 1) % map_side_lenght

    elif direction_column > 0:

        logger.debug('User goes right')
        new_player_position_column = (new_player_position_column + 1) % map_side_lenght

    elif direction_column < 0:

        logger.debug('User goes left')
        new_player_position_column = (map_side_lenght + new_player_position_column - 1) % map_side_lenght

    logger.debug('Returning from calculate_player_new_position(direction, player_position, game_map)')
    return (new_player_position_row, new_player_position_column)


def process_move_player(user_input, current_data):
    """
    Updates given data according to new player position defined by user input

    :param str user_input: direction of player movement
    :param tuple current_data: tuple with current game data (map,
        left treasures amount, player position and trapped state)
    :return: updated game data
    :rtype: tuple
    """

    logger.debug('Entering process_move_player(user_input, current_data) function')
    
    direction = PLAYER_MOVE_DIRECTIONS_BY_NAMES[user_input]

    updated_game_map, treasures_left, player_position, is_trapped = current_data

    current_player_position_row, current_player_position_column = player_position
    new_player_position_row, new_player_position_column = calculate_player_new_position(direction, player_position,
                                                                                        updated_game_map)

    logger.debug('Updating previous player position')
    updated_game_map[current_player_position_row][current_player_position_column] = MyMapGenerator.EMPTY_CELL
    
    logger.debug('Checking for trap in new position')
    if updated_game_map[new_player_position_row][new_player_position_column] == MyMapGenerator.TRAP:

        logger.debug('Got trapped in new position')
        is_trapped = True

        logger.debug('Updated trapped position')
        updated_game_map[new_player_position_row][new_player_position_column] = MyMapGenerator.TRAPPED_PLAYER

    else:

        logger.debug('Checking for treasure in new position')
        if updated_game_map[new_player_position_row][new_player_position_column] == MyMapGenerator.TREASURE:

            logger.debug('Got treasure in new position')
            treasures_left -= 1

        logger.debug('Updated new player position')
        updated_game_map[new_player_position_row][new_player_position_column] = MyMapGenerator.PLAYER

    logger.debug('Returning updated game data from process_move_player(user_input, current_data)')
    return (updated_game_map, treasures_left, (new_player_position_row, new_player_position_column), is_trapped)


def update_player(current_data):
    """
    Updates current data according to user input

    :param tuple current_data: current data
    :return: tuple with updated data
    :rtype: tuple
    """

    logger.debug('Entering update_player(current_data) function')
    
    updated_data = current_data

    while True:

        logger.debug('Waiting for user input')
        user_input = input('Where do you want to go(up, down, left, right): ')
        user_input = user_input.lower()

        logger.debug('Validating user input')
        if user_input in PLAYER_MOVE_DIRECTIONS_NAMES:

            logger.debug('User input is validated')
            updated_data = process_move_player(user_input, current_data)
            break

        logger.info('Invalid input! Please, try again')

    logger.debug('Returning updated data from update_player(current_data)')
    return updated_data


def print_map(game_map):
    """
    Prints current map
    """

    logger.debug('Printing game map')
    for i in range(len(game_map)):
        print(game_map[i])



def run_game_cycle():
    """
    Runs game cycle
    """

    is_trapped = False
    game_map, treasures_left, player_position = MyMapGenerator.generate_map()

    current_data = (game_map, treasures_left, player_position, is_trapped)
    while True:

        if treasures_left == 0:

            logger.debug('All treasures are collected')
            logger.info('Congrats! You have collected all treasures!')
            break

        elif is_trapped:

            logger.debug('Player is trapped')
            logger.info('Bad luck! You have fallen into a trap!')
            break
        
        logger.debug('Scanning area')
        scan_area_around_player(player_position, game_map)

        logger.debug('Updating player')
        game_map, treasures_left, player_position, is_trapped = update_player(current_data)
        current_data = (game_map, treasures_left, player_position, is_trapped)

    print_map(game_map)
