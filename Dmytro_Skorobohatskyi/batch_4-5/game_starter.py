from dungeon_game_logic import *

show_game_rules()
logger.debug('The game is started.')

game_map = []
x = y = 0
    
if check_start_new_game():
    side = get_side_of_field()
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
