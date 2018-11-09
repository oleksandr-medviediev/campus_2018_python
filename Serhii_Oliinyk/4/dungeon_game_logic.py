import dungeon_game_load_and_save as io
import dungeon_game_logger as log

def run_game(my_map, player_position):
    """
    Check if player find treasure and win or find trap and lose.

    :param my_map: the list of game map.
    :type my_map: list.

    :param player_position: the list of player position.
    :type player_position: list.

    :return: True if player win and False if player lose.
    :rtype: bool

    """
    direction_map = {
        "a": "left",
        "d": "right",
        "w": "up",
        "s": "down",
        "save": ""
    }

    result = False
    
    while True:
        directions = check_player_position(my_map, player_position)

        value = input("Choose direction a-left, d-right, w-up, s-down")
        if (value in direction_map) == False:
            log.logger.warning("Incorect input direction!")
            continue

        if value == "save":
            io.save_game(my_map)
            result = None
            break
        
        if (direction_map[value] in directions) == False:
            log.logger.info("You cannot move in this direction!")
        
        new_x = player_position[0]
        new_y = player_position[1]
        if value == "a":
            new_y -= 1
        elif value == "d":
            new_y += 1
        elif value == "w":
            new_x -= 1
        elif value == "s":
            new_x += 1

        if my_map[new_x][new_y] == "$":
            result = True
            break
        elif my_map[new_x][new_y] == "x":
            result = False
            break
        else:
            my_map[player_position[0]][player_position[1]] = "_"
            player_position[0] = new_x
            player_position[1] = new_y
            my_map[player_position[0]][player_position[1]] = "p"

    return result
        

def check_player_position(my_map, player_position):
    """
    Check if trap or treasure located near the player and calculate possible direction of movement.

    :param my_map: the list of game map.
    :type my_map: list.

    :param player_position: the list of player position.
    :type player_position: list.

    :return: list of possible directions.
    :rtype: list

    """

    size = len(my_map)
    x = player_position[0]
    y = player_position[1]

    surround_points = []
    move_direction = []

    surround_points.append([x, y + 1])
    surround_points.append([x + 1, y])
    surround_points.append([x, y - 1])
    surround_points.append([x - 1, y])

    move_direction.append("right")
    move_direction.append("down")
    move_direction.append("left")
    move_direction.append("up")

    point_value = [-1, -1]
    str_value = ""

    for i in range(len(surround_points)):
        if ((surround_points[i][0] < 0) or
            (surround_points[i][0] > (size - 1)) or
            (surround_points[i][1] < 0) or
            (surround_points[i][1] > (size - 1))):
            surround_points[i] = point_value
            move_direction[i] = str_value

    while point_value in surround_points:
        surround_points.remove(point_value)

    while str_value in move_direction:
        move_direction.remove(str_value)

    for i in surround_points:
        row = i[0]
        col = i[1]
        
        if my_map[row][col] == "$":
            log.logger.info("Treasure is nearby!")
        elif my_map[row][col] == "x":
            log.logger.info("Trap is nearby!")
    
    log.logger.info("You can move: ")
    for i in move_direction:
        log.logger.info(i)
    
    return move_direction
