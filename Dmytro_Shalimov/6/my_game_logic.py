import logging
from my_decorator import my_wrapper
import my_map_generator
import my_save_load_handler


PLAYER_MOVE_DIRECTIONS_NAMES = ['up', 'down', 'left', 'right']
PLAYER_MOVE_DIRECTIONS_BY_NAMES = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}


@my_wrapper
def scan_notification(cell_type):
    """
    Checks cell type and prints notification if check is passed

    :param str cell_type: type of item in cell
    """

    if cell_type != my_map_generator.EMPTY_CELL:
        print(my_map_generator.CELL_TYPES_INFO_MESSAGES[cell_type])


@my_wrapper
def scan_area_around_player(player_position, game_map):
    """
    Checks cells around player for treasures and traps and prints corresponding notifications

    :param tuple current_data: tuple with current game data (map, 
        left treasures amount, player position and trapped state)
    """
    
    player_position_row, player_position_column = player_position
    map_side_lenght = len(game_map)
    
    cell_right = (player_position_column + 1) % map_side_lenght
    cell_left = (map_side_lenght + (player_position_column - 1)) % map_side_lenght

    cell_top = (map_side_lenght + (player_position_row - 1)) % map_side_lenght
    cell_bottom = (player_position_row + 1) % map_side_lenght
    
    cell_type = game_map[player_position_row][cell_left]
    scan_notification(cell_type)

    cell_type = game_map[player_position_row][cell_right]
    scan_notification(cell_type)

    cell_type = game_map[cell_top][player_position_column]
    scan_notification(cell_type)

    cell_type = game_map[cell_bottom][player_position_column]
    scan_notification(cell_type)

    cell_type = game_map[cell_top][cell_left]
    scan_notification(cell_type)

    cell_type = game_map[cell_top][cell_right]
    scan_notification(cell_type)

    cell_type = game_map[cell_bottom][cell_right]
    scan_notification(cell_type)

    cell_type = game_map[cell_bottom][cell_left]
    scan_notification(cell_type)


@my_wrapper
def calculate_player_new_position(direction, player_position, game_map):
    """
    Calculates new player position according to given direction

    :param tuple direction: movement direction
    :param tuple player_position: current player position
    :param list game_map: current game map
    :return: tuple with new player position
    :rtype: tuple
    """

    direction_row, direction_column = direction
    new_player_position_row, new_player_position_column = player_position
    map_side_lenght = len(game_map)

    if direction_row > 0:
        new_player_position_row = (new_player_position_row + 1) % map_side_lenght

    elif direction_row < 0:
        new_player_position_row = (map_side_lenght + new_player_position_row - 1) % map_side_lenght

    elif direction_column > 0:
        new_player_position_column = (new_player_position_column + 1) % map_side_lenght

    elif direction_column < 0:
        new_player_position_column = (map_side_lenght + new_player_position_column - 1) % map_side_lenght

    return (new_player_position_row, new_player_position_column)


@my_wrapper
def process_move_player(user_input, current_data):
    """
    Updates given data according to new player position defined by user input

    :param str user_input: direction of player movement
    :param tuple current_data: tuple with current game data (map,
        left treasures amount, player position and trapped state)
    :return: updated game data
    :rtype: tuple
    """
    
    direction = PLAYER_MOVE_DIRECTIONS_BY_NAMES[user_input]

    updated_game_map, treasures_left, player_position, is_trapped = current_data

    current_player_position_row, current_player_position_column = player_position
    new_player_position_row, new_player_position_column = calculate_player_new_position(direction, player_position,
                                                                                        updated_game_map)

    updated_game_map[current_player_position_row][current_player_position_column] = my_map_generator.EMPTY_CELL
    
    if updated_game_map[new_player_position_row][new_player_position_column] == my_map_generator.TRAP:

        is_trapped = True
        updated_game_map[new_player_position_row][new_player_position_column] = my_map_generator.TRAPPED_PLAYER

    else:

        if updated_game_map[new_player_position_row][new_player_position_column] == my_map_generator.TREASURE:
            treasures_left -= 1

        updated_game_map[new_player_position_row][new_player_position_column] = my_map_generator.PLAYER

    return (updated_game_map, treasures_left, (new_player_position_row, new_player_position_column), is_trapped)


@my_wrapper
def update_player(current_data):
    """
    Updates current data according to user input

    :param tuple current_data: current data
    :return: tuple with updated data
    :rtype: tuple
    """
    
    updated_data = current_data

    while True:

        user_input = input('Enter "up", "down", "left", "right" to move, "save" to save current game): ')
        user_input = user_input.lower()

        if user_input in PLAYER_MOVE_DIRECTIONS_NAMES:

            updated_data = process_move_player(user_input, current_data)
            break

        elif user_input == 'save':

            my_save_load_handler.process_save_game(current_data)
            break

        print('Invalid input! Please, try again')

    return updated_data


@my_wrapper
def print_map(game_map):
    """
    Prints current map
    """

    for i in range(len(game_map)):
        print(game_map[i])


@my_wrapper
def process_select_game():
    """
    Prompts user to select whether he wants to start a new game or load saved one if it exists

    :return: True if New game, false otherwise
    :rtype: bool
    """

    is_new_game = True

    while True:

        user_input = input('Enter "new" to start new game, "load" to load saved one(if it exists)": ')
        user_input = user_input.lower()

        if user_input == 'load':

            is_new_game = False
            break

        elif user_input == 'new':
            break

        print('Invalid input! Try again')

    return is_new_game


@my_wrapper
def init_game_data():
    """
    Initializes game data according to game type selected by user(new or load)

    :return: tuple with game data (map,
        left treasures amount, player position and trapped state)
    :rtype: tuple
    """

    current_data = ()
    is_trapped = False

    while not current_data:

        if process_select_game():

            game_map, treasures_left, player_position = my_map_generator.generate_map()
            current_data = (game_map, treasures_left, player_position, is_trapped)

        else:

            current_data = my_save_load_handler.process_load_game()
            if not current_data:
                print('Something wrong with file or data in it. Please try again')

            else:
                print('Data is loaded')

    return current_data 


@my_wrapper
def run_game_cycle():
    """
    Runs game cycle
    """

    current_data = init_game_data()
    game_map, treasures_left, player_position, is_trapped = current_data
    
    while True:

        if treasures_left == 0:

            print('Congrats! You have collected all treasures!')
            break

        elif is_trapped:

            print('Bad luck! You have fallen into a trap!')
            break
        
        scan_area_around_player(player_position, game_map)

        game_map, treasures_left, player_position, is_trapped = update_player(current_data)
        current_data = (game_map, treasures_left, player_position, is_trapped)

    print_map(game_map)
