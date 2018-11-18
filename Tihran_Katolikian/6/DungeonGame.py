from DungeonGameMapGenerator import generate_map, DungeonCell
from enum import Enum
from sys import stdout
import DungeonGameSaveLoad
import logging
import logging.config


class PlayerCommand(Enum):
    UP = 0
    LEFT = 1
    DOWN = 2
    RIGHT = 3
    SAVE = 4


class StartMenu(Enum):
    NEW_GAME = 0
    LOAD_GAME = 1


text_to_menu = {
    'new game' : StartMenu.NEW_GAME,
    'load' : StartMenu.LOAD_GAME
}


text_to_command = {
    'w' : PlayerCommand.UP,
    'a' : PlayerCommand.LEFT,
    's' : PlayerCommand.DOWN,
    'd' : PlayerCommand.RIGHT,
    'save' : PlayerCommand.SAVE
}

move_commands = (
    PlayerCommand.UP,
    PlayerCommand.LEFT,
    PlayerCommand.DOWN,
    PlayerCommand.RIGHT
)

direction_to_vector = {
    PlayerCommand.UP : (-1, 0),
    PlayerCommand.LEFT : (0, -1),
    PlayerCommand.DOWN: (1, 0),
    PlayerCommand.RIGHT: (0, 1)
}


hide_everything_except_player_map = {
    DungeonCell.EMPTY : ' ',
    DungeonCell.PLAYER : '*',
    DungeonCell.TRAP: ' ',
    DungeonCell.TREASURE: ' '
}


output_everything_map = {
    DungeonCell.EMPTY : ' ',
    DungeonCell.PLAYER : '*',
    DungeonCell.TRAP: '#',
    DungeonCell.TREASURE: '$'
}


sum_vectors = lambda a, b: (a[0] + b[0], a[1] + b[1])


def process_game_start():
    '''
    Function is used to process game start. It is an equivalent of menu in normal games.
    :return: a function that player have chosen in menu;
    :rtype: StartMenu.
    '''
    logging.debug('Method called')
    while True:
        logging.info('Type \'new game\' to start a new game or \'load\' to old game from save: ')
        input_command = input()
        if input_command in text_to_menu.keys():
            return text_to_menu[input_command]


def output_map(dungeon_map, dungeon_cell_to_output_symbol):
    '''
    Function is used to output a map for Dungeon Game.
    :param dungeon_map: a map to output;
    :param dungeon_cell_to_output_symbol: a map that will be used to output the cells
    :type dungeon_map: a list of lists of DungeonCells; 
    :type dungeon_cell_to_output_symbol: a dict with key type: DungeonCell, value type: str.
    '''
    logging.debug('Method called')
    # i guess there must be more efficient way to format such string
    lock_string = ''.join('-' * len(dungeon_map))

    logging.info(lock_string)

    row_to_string = lambda row: ''.join(dungeon_cell_to_output_symbol[x] for x in row)
    map_string = '\n'.join(row_to_string(row) for row in dungeon_map)
    logging.info(map_string)

    logging.info(lock_string)


def get_player_command(position, map_size):
    '''
    Function is used get the user's input;
    :param position: a position on map;
    :param map_size: a size of map;
    :return: a user's command;
    :type map_size: int;
    :type position: a tuple of 2 ints;
    :rtype: str
    '''
    logging.debug('Method called')
    while True:
        logging.info('Please, input your command. Use "w", "a", "s", "d" and "save" commands: ')
        input_command = input()
        logging.debug(f'User command is:{input_command}')
        if input_command in text_to_command.keys():
            command = text_to_command[input_command]

            if command in move_commands:
                can_go_there = True
                x, y = position
                if command is PlayerCommand.UP and x is 0:
                    can_go_there = False
                elif command is PlayerCommand.DOWN and x is map_size - 1:
                    can_go_there = False
                elif command is PlayerCommand.LEFT and y is 0:
                    can_go_there = False
                elif command is PlayerCommand.RIGHT and y is map_size - 1:
                    can_go_there = False

                if not can_go_there:
                    logging.debug('User can\'t go in direction')
                    logging.info('Unfortunately you can\'t go there. Try again.')
                    continue

            return command
        else:
            logging.info('Wrong input. Try again.')


def get_cells_near(position, dungeon_map):
    '''
    Function used to get all cells that are near the position on map;
    :param position: a position on map;
    :param dungeon_map: a map used for dungeon game;
    :return: all cells near position;
    :type position: a tuple of 2 ints;
    :type dungeon_map: a list of lists of DungeonCells;
    :rtype: a list of DungeonCells.
    '''
    logging.debug('Method called')
    map_size = len(dungeon_map)
    x, y = position

    cells = []
    if x != 0:
        cells.append(dungeon_map[x - 1][y])
    
    if x != map_size - 1:
        cells.append(dungeon_map[x + 1][y])

    if y != 0:
        cells.append(dungeon_map[x][y - 1])

    if y != map_size - 1:
        cells.append(dungeon_map[x][y + 1])

    assert(len(cells) >= 2 and len(cells) <= 4)

    return cells


def run_game(game_start_mode, map_size):
    '''
    Function runs the Dungeon Game;
    :param game_start_mode: the way game should start;
    :param map_size: a size of map that will be used for game. Size should be >= 5. If game_start_mode is LOAD, the\
    value of map_size is idnored and will be overwritten after load;
    :type map_size: int if game_start_mode is NEW_GAME, any other type otherwise;
    :type game_start_mode: StartMenu.
    '''
    logging.debug('Method called')
    if game_start_mode is StartMenu.LOAD_GAME:
        logging.debug('Game starts with LOAD GAME mode. Loading from file...')
        player_position, dungeon_map = DungeonGameSaveLoad.load_game()
        map_size = len(dungeon_map)
    else:
        logging.debug('Game starts with NEW GAME mode. Generating map...')
        player_position, dungeon_map = generate_map(map_size)
    logging.debug(f'Map:{dungeon_map}\nPlayer position:{player_position}')

    should_run = True
    logging.debug('Game loop starts')
    game_loop_counter = 0
    while should_run:
        logging.debug(f'Game loop iteration {game_loop_counter}')
        output_map(dungeon_map, hide_everything_except_player_map)

        cells_near_player = get_cells_near(player_position, dungeon_map)

        traps_nearby = [cell for cell in cells_near_player if cell is DungeonCell.TRAP]
        if traps_nearby:
            logging.info(f'Warning! There is {len(traps_nearby)} traps nearby!')
        
        treasures_nearby = [cell for cell in cells_near_player if cell is DungeonCell.TREASURE]
        if treasures_nearby:
            logging.info(f'Wow! There is {len(treasures_nearby)} treasures just near you! Good luck!')

        player_command = get_player_command(player_position, map_size)
        if player_command in move_commands:
            old_x, old_y = player_position
            player_position = sum_vectors(player_position, direction_to_vector[player_command])
            new_x, new_y = player_position
            
            if dungeon_map[new_x][new_y] is DungeonCell.TREASURE:
                logging.info('You won! Gratz! :)')
                should_run = False
            elif dungeon_map[new_x][new_y] is DungeonCell.TRAP:
                logging.info('You lost:( GL next time!')
                should_run = False
            else:
                logging.info('You found nothing. Keep exploring the map!:)')
                dungeon_map[old_x][old_y] = DungeonCell.EMPTY
                dungeon_map[new_x][new_y] = DungeonCell.PLAYER
        else:
            DungeonGameSaveLoad.save_game(player_position, dungeon_map)
            logging.debug('Game if saved.')
            logging.info('Game is saved.')

    logging.debug('Game loop ended')
    output_map(dungeon_map, output_everything_map)
