from map_creator import game_entities
from map_creator import generated_map
from map_creator import generate_map
from map_creator import print_map
from input_module import read_input
from input_module import read_game_config
from input_module import main_menu_option
import files_module
import logger

map_size_x = int()
map_size_y = int()
moves = [(-1, 0), (1, 0), (0, 1), (0, -1)]
moving_commands = { 'up':moves[0], 'down':moves[1], 'right':moves[2], 'left':moves[3] }
managing_commands = ["save"]
warnings = ["This is impasse\n", "The trap is near you\n", "The treasure is near you\n"]


def move_player(player_pos_x,player_pos_y,command):
    """
    Changes player's position according to command
    :param player_pos_x: current player's position x  
    :param player_pos_y: current player's position y
    :param command: command to execute from moving_commands
    :return: new position
    :rtype: (int,int)
    """
    position_x = player_pos_x + moving_commands[command][0]
    position_y = player_pos_y + moving_commands[command][1]

    generated_map[player_pos_x][player_pos_y] = '+'

    if 0 <= position_x < map_size_y and 0 <= position_y < map_size_x:
        player_pos_x = position_x
        player_pos_y = position_y
    else:
        logger.logging_object.debug('End of map\n')
        logger.logging_object.warning(warnings[0])
    
    logger.logging_object.debug(f'Player position - {player_pos_x}{player_pos_y}')

    return player_pos_x,player_pos_y


def is_game_ended(current_position_status):
    """
    Checks if game is ended
    :param: player's position information - game entity character
    :paramtype: str
    :return: if the end game condition is reached
    :rtype: bool
    """
    is_ended = True

    if current_position_status == game_entities['treasure']:
        logger.logging_object.info('You won!')
    elif current_position_status == game_entities['trap']:
        logger.logging_object.info('You lost')
    else:
        is_ended = False

    return is_ended


def update(player_pos_x,player_pos_y):
    """
    Checks the current game state(neighbour positions) and outputs information about it
    :param player_pos_x: player's position x
    :param player_pos_y: player's position y
    :paramtype player_pos_x,player_pos_y: int
    :return: nothing
    :rtype: None
    """   
    number_of_treasures_near = 0
    number_of_traps_near = 0
    
    for direction in moves:

        neighbour_cell_x = player_pos_x + direction[0]
        neighbour_cell_y = player_pos_y + direction[1]

        if not 0 <= neighbour_cell_x < map_size_y or not 0 <= neighbour_cell_y < map_size_x:
            continue

        if generated_map[neighbour_cell_x][neighbour_cell_y] == game_entities['treasure']:
            number_of_treasures_near += 1
        elif generated_map[neighbour_cell_x][neighbour_cell_y] == game_entities['trap']:
            number_of_traps_near += 1

        logger.logging_object.debug(f'Cell {neighbour_cell_x},{neighbour_cell_y} checked')

    if number_of_treasures_near > 0:
        logger.logging_object.warning(warnings[2])
        
    if number_of_traps_near > 0:
        logger.logging_object.warning(warnings[1])


def game_loop(start_pos_x, start_pos_y):
    """
    Runs the main game logic
    :param start_pos_x: player's starting position x
    :param start_pos_y: player's startin position y
    :paramtype start_pos_x,start_pos_y: int
    :return: nothing
    :rtype: None
    """  
    is_end = False
    player_x,player_y = start_pos_x, start_pos_y
    while not is_end:

        update(player_x,player_y)
        command = read_input(moving_commands,managing_commands)

        logger.logging_object.info(f'Input command {command}')
        logger.logging_object.debug('input processing')

        if command == managing_commands[0]:
            
            logger.logging_object.debug('Game loop function - saving executing')
            position = player_x, player_y
            map_size = map_size_x,map_size_y
            files_module.save_game_state(generated_map, position,map_size)
            logger.logging_object.info('Game is saved successfully') 
            continue
        
        player_x,player_y = move_player(player_x,player_y,command)

        current_pos_status = generated_map[player_x][player_y]
        
        is_end = is_game_ended(current_pos_status)

    generated_map[player_x][player_y] = game_entities['player']


if __name__ == '__main__':

    option = main_menu_option()
    
    if option == 'start':

        logger.logging_object.info("New game started\n")
        map_size_x,map_size_y = read_game_config()
        start_pos_x, start_pos_y = generate_map(map_size_x,map_size_y)
        
    elif files_module.check_loading():

        logger.logging_object.info("Loaded game started\n")
        loaded_map,position,map_size = files_module.load_game()
        start_pos_x, start_pos_y = int(position[0]),int(position[1])
        map_size_x,map_size_y = int(map_size[0]),int(map_size[1])
        generated_map.extend(loaded_map)

    else:
        
        logger.logging_object.error("No saved file ")
        logger.logging_object.info("Can't load game\n")
        map_size_x,map_size_y = read_game_config()
        start_pos_x, start_pos_y = generate_map(map_size_x,map_size_y)
        
    game_loop(start_pos_x, start_pos_y)
    print_map()
        
