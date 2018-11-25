import logger_decorator
import logging
import logger
from dungeon_game_error import MapSizeValueError
from dungeon_game_error import CommandError

def read_game_config():
    """
    Reads and validates input about map size
    :return: map size
    :rtype: (int,int)
    """
    map_size_x = input(f'The width of the map: ')
    map_size_y = input(f'The lenght of the map: ')
    
    while not map_size_x.isnumeric() or not map_size_y.isnumeric():
        map_size_x = input(f'The width of the map: ')
        map_size_y = input(f'The lenght of the map: ')

    try:
        
        map_size_x = int(map_size_x)
        map_size_y = int(map_size_y)

        if (map_size_x < 8 or map_size_y < 8) or (map_size_x > 20 or map_size_y > 20):
            raise MapSizeValueError((map_size_x,map_size_y))


    except (TypeError, MapSizeValueError) as error:
         logger.logging_object.error(error)
         logger.logging_object.info('Map size must be integer in range [8;20]. Map size is set to default value 9x9\n ')
         map_size_x = 9
         map_size_y = 9

    return map_size_x,map_size_y


def read_input(moving_commands,managing_commands):
    """
    Reads and validates input command
    :param moving_commands: commands to move character
    :param managing_commands: game flow commands
    :paramtype moving_commands: dict(std:int,int))
    :paramype managing_commands: list(str)
    :return: command
    :rtype: str
    """
    command_names = list(moving_commands.keys())
    command_names.extend(managing_commands)
    command = input(f'Choose your next command.\n{command_names}: ').lower()


    try:
        
        if command not in command_names:
            raise CommandError()

    except CommandError as error:
        
        logger.logging_object.error(error)
        return read_input(moving_commands,managing_commands)
            
    return command


def main_menu_option():
    """
    Reads and validates input about game main menu 
    :return: command
    :rtype: str
    """
    debug_mode_on = input(f'To enable debug mode type y/Y\n').lower()

    if debug_mode_on == 'y':
        
        logger_decorator.is_debug_mode = True
        logger.stream_logger.setLevel(logging.DEBUG)
        
    options = ['Start new game', 'Load saved game']
    commands = ['start', 'load']

    command = input(f'Choose option{options}\nPrint onr of corresponding {commands}\n').lower()

    while command not in commands:
        command = input(f'Print right command')

    return command
    
