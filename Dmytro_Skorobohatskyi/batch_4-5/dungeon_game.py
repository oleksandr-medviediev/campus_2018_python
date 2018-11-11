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
    
    player_choice = input('Enter the direction(r, l, u, d): ')
    while player_choice == '':
        player_choice = input()
    
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

        Args:
            (none)

        Returns:
            (bool): return true if chosen start new game option,
                    otherwise - return False

    """
    
    logger.info('\n1. Start new game.\n2. Load game.')

    choice = input('Enter your choice: ')

    is_start_new_game = choice == '1'

    return is_start_new_game

    
def run_game():

    """ Function implements main logic of game.   """
    show_game_rules()
    logger.debug('The game is started.')

    game_map = []
    x = y = 0
    
    if check_start_new_game():
        side = int(input('Enter the side of field: '))
        logger.debug('The field side is {}.'.format(side))
        game_map = level_builder.generate_map(side)
        logger.debug('The map was generated.')
        
        x, y = get_random_start_point(game_map)
        logger.debug('The start point is ({0}, {1})'.format(x, y))
    else:
        game_map, x, y = load_game()
        logger.debug('The game was loaded successfully.')
        logger.debug('The start point is ({0}, {1})'.format(x, y))

    is_game_continuos = True

    while is_game_continuos:

        logger.debug('The turn was started.')

        warn_situation_in_cell(game_map, x, y)
        logger.debug('The situation was warned successfully.')
        
        choice = recognize_input()
        if choice == SAVE_COMMAND_INDEX:
            save_game(game_map, x, y)
            while choice == SAVE_COMMAND_INDEX:
               choice = recognize_input()
            
        logger.debug('The direction index is {}.'.format(choice))

        if not is_direction_blocked(game_map, choice, x, y):   
            x, y = get_new_coordinates(choice, x, y)
            logger.debug('The player moved to ({0}, {1})'.format(x, y))

            if is_game_over(game_map, x, y):
                is_winning = check_game_win(game_map[x][y])
                show_game_result(is_winning)
                is_game_continuos = False
                logger.debug('The game over')
                
        else:
            logger.warning("You can't move there")
               
        logger.debug('The turn was finished successfully.')
    
    level_builder.show_level_map(game_map)

    logger.debug('The game is finished successfully.')
