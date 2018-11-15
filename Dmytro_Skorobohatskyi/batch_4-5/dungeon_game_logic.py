import level_builder
from random import randint
from logging_system import logger
import game_saver

# Data section
all_shifts = [
    { 'x': -1, 'y': 0 },
    { 'x': 0, 'y': 1 },
    { 'x': 1, 'y': 0 },
    { 'x': 0, 'y': -1 }
]

SAVE_COMMAND_INDEX = -1

UP_INDEX = 0 
RIGHT_INDEX = 1
DOWN_INDEX = 2
LEFT_INDEX = 3 

directions = {
    'l': LEFT_INDEX,
    'u': UP_INDEX,
    'r': RIGHT_INDEX,
    'd': DOWN_INDEX
}

game_objects = [level_builder.TRAP, level_builder.TREASURE]


def show_game_rules():

    """ Funtion shows game rules in its beginning. """
    
    print('''Rules:
            Player can move up, down, left and right
            (if it's not an edge of the map).
            If you get trapped - you lost.
            If you find a treasure - you won.''')


def get_side_of_field():

    """ Function recognize player's input to specify side of field.

        Args:
            (none)

        Returns:
            int: specified side

    """
    
    number_string = input('Enter the side of field(more than 5): ')

    while not number_string.isdigit() or int(number_string) < 5:
        number_string = input('Wrong input. Side: ')

    side = int(number_string)

    return side

    
def get_random_start_point(level_map):

    """ Function return random start point for player.
        This point must be not a trap and not a treasure.

        Args:
            level_map(list[list]): matrix presenting play map

        Returns:
            (int, int): coordinates of start point

    """
        
    line = randint(0, len(level_map) - 1)
    column = randint(0, len(level_map[line]) - 1)

    while level_map[line][column] in game_objects:
        line = randint(0, len(level_map) - 1)
        column = randint(0, len(level_map[line]) - 1)

    return line, column


def warn_situation_in_cell(level_map, x, y):

    """ Function warns the player if there's a trap or a treasure
        within one square from him.

        Args:
            level_map(list[list]): matrix presenting play map
            x(int): coordinate by columns of player position
            y(int): coordinate by rows of player position

        Returns:
            (none)

    """
    
    for i, index in enumerate(directions.values()):
        
        if is_direction_blocked(level_map, index, x, y):
            continue

        temp_x, temp_y = get_new_coordinates(index, x, y)
        
        if level_map[temp_x][temp_y] == level_builder.TRAP:
            logger.info('Near a trap. Be careful.')
        elif level_map[temp_x][temp_y] == level_builder.TREASURE:
            logger.info('Near a treasure. Good luck.')


def recognize_input():

    """ Function recognize player's input with possible save variant.

        Args:
            (none)

        Returns:
            int: index of direction or save command
    """
    
    player_choice = input('Enter the direction(r, l, u, d) or save: ')
    while player_choice == '':
        player_choice = input()

    while player_choice not in ['r', 'l', 'u', 'd', 'save']:
        player_choice = input('Wrong input. Direction: ')
    
    if player_choice == 'save':
        return SAVE_COMMAND_INDEX

    direction = directions.get(player_choice, None)

    return direction


def get_shift_by_direction(direction_index):

    """ Function return shift depending on direction.

        Args:
            direction_index(int): index specified direction

        Returns:
            (int, int): shift by columns and rows
    """
    
    shift_x = all_shifts[direction_index]['x']
    shift_y = all_shifts[direction_index]['y']

    return shift_x, shift_y

    
def is_direction_blocked(level_map, direction_index, x, y):

    """ Function checks possibility to move in specified direction
        from current position

        Args:
            level_map(list[list]): matrix presenting play map
            direction_index(int): index presenting direction
            x(int): coordinate by columns of current player position
            y(int): coordinate by rows of current player position

        Returns:
            (bool): return True if player can NOT in specified direction

    """
    
    shift_x, shift_y = get_shift_by_direction(direction_index)
    new_x, new_y = get_new_coordinates(direction_index, x, y)
    
    is_cell_blocked = new_x < 0 or new_y < 0 or \
                      new_x == len(level_map[0]) or \
                      new_y == len(level_map)

    return is_cell_blocked


def get_new_coordinates(direction_index, x, y):

    """ Function returns new coordinates of player shifted in specified direction

        Args:
            direction_index(int): index presenting direction
            x(int): coordinate by columns of current player position
            y(int): coordinate by rows of current player position

        Returns:
            (int, int): new player's coordinates

    """
    
    shift_x, shift_y = get_shift_by_direction(direction_index)
    new_x, new_y = shift_x + x, shift_y + y

    return new_x, new_y


def is_game_over(level_map, x, y):

    """ Function checks game over as winning or losing

        Args:
            level_map(list[list]): matrix presenting play map
            x(int): coordinate by columns of player position
            y(int): coordinate by rows of player position

        Returns:
            (bool): return True if player stand on a trap or treasure

    """

    is_cell_contain_object = level_map[x][y] in game_objects

    return is_cell_contain_object


def check_game_win(symbol):

    """ Function recognize result of game

        Args:
            symbol(str): trap or treasure symbol

        Returns:
            bool: return True if symbol is treasure

    """
    
    is_winning = symbol == level_builder.TREASURE
    
    return is_winning


def show_game_result(is_winning):

    """ Function shows result of game

        Args:
            is_winning(bool): true if winning, otherwise - if losing

        Returns:
            (none)

    """
    
    result_string = 'You lose!'
    
    if is_winning:
        result_string = 'You won!'
        
    logger.info(result_string)


def save_game(level_map, x, y):

    """ Function saves play map and player position to file 

        Args:
            level_map(list[list]): matrix presenting play map
            x(int): coordinate by columns of player position
            y(int): coordinate by rows of player position

        Returns:
            (none)

    """
    
    save_object = {
        'map': level_map,
        'x': x,
        'y': y
    }

    game_saver.save_to_file(save_object)


def load_game():

    """ Function loads play map and player position from file 

        Args:
            (none)

        Returns:
            (list[list], int, int): matrix presenting play map
                                    and player position

    """
    
    saved_object = game_saver.load_from_file()
    
    level_map = saved_object['map'].copy()
    x = saved_object['x']
    y = saved_object['y']

    return level_map, x, y


def check_start_new_game():

    """ Function checks start new game or load existing saving.
        If file does not exist, start new game

        Args:
            (none)

        Returns:
            (bool): return true if chosen start new game option,
                    otherwise - return False

    """
    
    logger.info('\nPress "load" for loading game.\nAnything to start new game.\n')

    choice = input('Enter your choice: ')

    is_start_new_game = choice != 'load'

    if not is_start_new_game and not game_saver.check_loading_file():
        is_start_new_game = True
        logger.info('Loading does not exist. Starting new game...')

    return is_start_new_game
