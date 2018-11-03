import dungeon_game_load_and_save as io

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
            print("Incorect input direction!")
            continue

        if value == "save":
            io.save_game(my_map)
            result = None
            break
        
        if (direction_map[value] in directions) == False:
            print("You cannot move in this direction!")
        
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

    if (x == 0) and (y == 0):
        surround_points.append([x, y + 1])
        surround_points.append([x + 1, y])

        move_direction.append("right")
        move_direction.append("down")
    elif (x == 0) and (y == (size - 1)):
        surround_points.append([x, y - 1])
        surround_points.append([x + 1, y])

        move_direction.append("left")
        move_direction.append("down")
    elif (x == (size - 1)) and (y == 0):
        surround_points.append([x - 1, y])
        surround_points.append([x, y + 1])

        move_direction.append("right")
        move_direction.append("up")
    elif (x == (size - 1)) and (y == (size - 1)):
        surround_points.append([x, y - 1])
        surround_points.append([x - 1, y])

        move_direction.append("left")
        move_direction.append("up")
    elif (x == 0) and (y > 0) and (y < (size - 1)):
        surround_points.append([x, y - 1])
        surround_points.append([x, y + 1])
        surround_points.append([x + 1 , y])

        move_direction.append("right")
        move_direction.append("left")
        move_direction.append("down")
    elif (x == (size - 1)) and (y > 0) and (y < (size - 1)):
        surround_points.append([x, y - 1])
        surround_points.append([x, y + 1])
        surround_points.append([x - 1, y])

        move_direction.append("right")
        move_direction.append("left")
        move_direction.append("up")
    elif (y == 0) and (x > 0) and (x < (size - 1)):
        surround_points.append([x - 1, y])
        surround_points.append([x + 1, y])
        surround_points.append([x, y + 1])

        move_direction.append("right")
        move_direction.append("up")
        move_direction.append("down")
    elif (y == (size - 1)) and (x > 0) and (x < (size - 1)):
        surround_points.append([x - 1, y])
        surround_points.append([x + 1, y])
        surround_points.append([x, y - 1])

        move_direction.append("up")
        move_direction.append("left")
        move_direction.append("down")
    else:
        surround_points.append([x - 1, y])
        surround_points.append([x + 1, y])
        surround_points.append([x, y - 1])
        surround_points.append([x, y + 1])

        move_direction.append("up")
        move_direction.append("left")
        move_direction.append("down")
        move_direction.append("right")
    
    for i in surround_points:
        row = i[0]
        col = i[1]
        
        if my_map[row][col] == "$":
            print("Treasure is nearby")
        elif my_map[row][col] == "x":
            print("Trap is nearby")
    
    print("You can move: ")
    for i in move_direction:
        print(i)
    
    return move_direction
