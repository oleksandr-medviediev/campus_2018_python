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

    map_size_x = int(map_size_x)
    map_size_y = int(map_size_y)

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

    while command not in command_names:
        command = input(f'Such command doesn''t exist.\nYour command: ').lower()

    return command


def main_menu_option():
    """
    Reads and validates input about game main menu 
    :return: command
    :rtype: str
    """

    options = ['Start new game', 'Load saved game']
    commands = ['start', 'load']

    command = input(f'Choose option{options}\nPrint onr of corresponding {commands}\n').lower()

    while command not in commands:
        command = input(f'Print right command')

    return command
    
