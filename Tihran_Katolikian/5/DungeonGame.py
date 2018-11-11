from DungeonGameMapGenerator import generate_map, DungeonCell
from enum import Enum
from sys import stdout
import DungeonGameSaveLoad


class PlayerCommand(Enum):
    UP = 0
    LEFT = 1
    DOWN = 2
    RIGHT = 3
    SAVE = 4


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


def output_map(dungeon_map, dungeon_cell_to_output_symbol):
    '''
    Function is used to output a map for Dungeon Game.
    :param dungeon_map: a map to output;
    :param dungeon_cell_to_output_symbol: a map that will be used to output the cells
    :type dungeon_map: a list of lists of DungeonCells; 
    :type dungeon_cell_to_output_symbol: a dict with key type: DungeonCell, value type: str.
    '''

    # i guess there must be more efficient way to format such string
    lock_string = ''.join('-' * len(dungeon_map))

    print(lock_string)

    for row in dungeon_map:
        for element in row:
            stdout.write(dungeon_cell_to_output_symbol[element])
        stdout.write('\n')

    print(lock_string)


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
    while True:
        input_command = input('Please, input the direction of your move. Use w, a, s, d, save commands: ')
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
                    print('Unfortunately you can\'t go there. Try again.')
                    continue

            return command
        else:
            print('Wrong input. Try again.')


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


def run_game(map_size):
    '''
    Function runs the Dungeon Game;
    :param map_size: a size of map that will be used for game. Size should be >= 5;
    :type map_size: int
    '''
    player_position, dungeon_map = generate_map(map_size)

    should_run = True
    while should_run:
        output_map(dungeon_map, hide_everything_except_player_map)

        cells_near_player = get_cells_near(player_position, dungeon_map)

        traps_nearby = [cell for cell in cells_near_player if cell is DungeonCell.TRAP]
        if traps_nearby:
            print(f'Warning! There is {len(traps_nearby)} traps nearby!')
        
        treasures_nearby = [cell for cell in cells_near_player if cell is DungeonCell.TREASURE]
        if treasures_nearby:
            print(f'Wow! There is {len(treasures_nearby)} treasures just near you! Good luck!')

        player_command = get_player_command(player_position, map_size)
        if player_command in move_commands:
            old_x, old_y = player_position
            player_position = sum_vectors(player_position, direction_to_vector[player_command])
            new_x, new_y = player_position
            
            if dungeon_map[new_x][new_y] is DungeonCell.TREASURE:
                print('You won! Gratz! :)')
                should_run = False
            elif dungeon_map[new_x][new_y] is DungeonCell.TRAP:
                print('You lost:( GL next time!')
                should_run = False
            else:
                print('You found nothing. Keep exploring the map!:)')
                dungeon_map[old_x][old_y] = DungeonCell.EMPTY
                dungeon_map[new_x][new_y] = DungeonCell.PLAYER
        else:
            DungeonGameSaveLoad.save_game(player_position, dungeon_map)
            print('Game is saved.')

    output_map(dungeon_map, output_everything_map)
