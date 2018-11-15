import dungeon_logger


CAGE_STATE = ['bomb', 'treasue', 'empty']
GAME_STATE = ['lost', 'won', 'ingame']
COMMANDS = ['r', 'l', 'u', 'd']
WARNINGS = {'bomb':'Bomb is near you!',
            'treasue':'Tresure is near you'}


def check_pos(dun_map, position):
    """
    :param dun_map: dungeon map
    :type dun_map: list[list[]]
    
    :param position: position on the dun_map
    :type position: list[x,y]

    :return: element of CAGE_STATE
    :rtype: str
    """

    dungeon_logger.logger.debug(f'position: {position}, pos type: {type(position)}')
    ret_val = ""
    pos_value = dun_map[position[0]][position[1]]
    if pos_value == '!':
        ret_val = 'bomb'

    elif pos_value == '#':
        ret_val = 'treasue'

    else:
        ret_val = 'empty'

    return ret_val


def check_closest_pos(dun_map, position, size):
    """
    :param dun_map: dungeon map
    :type dun_map: list[list[]]
    :param position: position on the dun_map
    :type position: list[x,y]
    :param size: size of the dun_map
    :type size: int

    :return: up to 2 elements of CAGE_STATE
    :rtype: {str}
    """

    ret_val = set()
    x_coord = position[0]
    y_coord = position[1]
    if x_coord > 0:
        
        value = check_pos(dun_map, [x_coord - 1, y_coord])
        if value != 'empty':
            ret_val.add(value)

    if x_coord < size - 2:
        
        value = check_pos(dun_map, [x_coord + 1, y_coord])
        if value != 'empty':
            ret_val.add(value)
        
    if y_coord > 0:
        
        value = check_pos(dun_map, [x_coord, y_coord - 1])
        if value != 'empty':
            ret_val.add(value)

    if y_coord < size - 2:
        
        value = check_pos(dun_map, [x_coord, y_coord + 1])
        if value != 'empty':
            ret_val.add(value)

    dungeon_logger.logger.debug("Nearest positions")

    return ret_val


def make_move_if_possible(position, size, command):
    """
    :param position: position on the dun_map
    :type position: list[x,y]
    
    :param size: size of the dun_map
    :type size: int
    
    :param command: command to move right or left, higher or lower
    :type command: str

    :return: True if possible , False otherwise
    :rtype: bool
    """

    ret_val = True
    if command == 'r':
        
        if position[1] > size - 2:
            ret_val = False
        else:
            position[1] += 1

    if command == 'l':

        if position[1] < 1:
            ret_val = False
        else:
            position[1] -= 1

    if command == 'u':

        if position[0] < 1:
            ret_val = False
        else:
            position[0] -= 1

    if command == 'd':

        if position[0] > size - 2:
            ret_val = False
        else:
            position[0] += 1

    dungeon_logger.logger.debug("Move is possible")

    return  ret_val
    

def make_move(dun_map, position, size, command):
    """
    :param dun_map: dungeon map
    :type dun_map: list[list[]]
    
    :param position: position on the dun_map
    :type position: list[x,y]
    
    :param size: size of the dun_map
    :type size: int
    
    :param command: command to move right or left, higher or lower
    :type command: str

    :return: game state
    :rtype: element of GAME_STATE
    """

    dungeon_logger.logger.debug(f"Move with command: {command}")
    
    dun_map[position[0]][position[1]] = '0'
    move_ret_val = make_move_if_possible(position, size, command)
    if move_ret_val == False:

        dungeon_logger.logger.info('Move is not possible')
        return 'ingame'

    cage_state = check_pos(dun_map, position)
    game_state = 'ingame'

    if cage_state == 'empty':
        
        cages = check_closest_pos(dun_map, position, size)
        for cage in cages:
            dungeon_logger.logger.info(WARNINGS[cage])

    elif cage_state == 'bomb':
        
        dungeon_logger.logger.info("You LOST!!!")
        game_state = 'lost'
        
    else:
        
        dungeon_logger.logger.info("You WON!!!")
        game_state = 'won'

    return game_state
