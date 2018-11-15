import map_generator
import dungeon_input
import custom_log
import serializer


is_trap_near_player = False
is_treasure_near_player = False
game_map = []


def get_player_pos():
    """
    Returns player's position from game map.

    :returns: players position as (x,y).
    :rtype: list of two ints.
    """

    global game_map

    x_index = -1
    y_index = -1

    for i in range(len(game_map)):

        x_index = game_map[i].find(map_generator.PLAYER_SYMBOL)

        if x_index != -1:
            y_index = i
            break
    
    return (x_index, y_index)


def get_valid_directions():
    """
    Returns possible player's moves.

    :returns: list of possible moves.
    :rtype: list of strings.
    """

    global game_map

    x_size = len(game_map[0])
    y_size = len(game_map)

    player_pos = get_player_pos()

    valid_directions = []

    if player_pos[0] > 0:
        valid_directions.append(dungeon_input.COMMANDS_TYPES[0])

    if player_pos[0] < x_size - 1:
        valid_directions.append(dungeon_input.COMMANDS_TYPES[1])

    if player_pos[1] < y_size - 1:
        valid_directions.append(dungeon_input.COMMANDS_TYPES[2])

    if player_pos[1] > 0:
        valid_directions.append(dungeon_input.COMMANDS_TYPES[3])

    return valid_directions


def is_item_near_player(item):
    """
    Returns result of check is some item near player.

    :param item: item to check.
    :item type: char.
    :returns: result of check.
    :rtype: bool.
    """

    global game_map

    player_pos = get_player_pos()

    possible_directions = get_valid_directions()

    result = False

    for direction in possible_directions:

        if direction == dungeon_input.COMMANDS_TYPES[0]:

            if game_map[player_pos[1]][player_pos[0] - 1] == item:
                result = True
                break
            
        elif direction == dungeon_input.COMMANDS_TYPES[1]:

            if game_map[player_pos[1]][player_pos[0] + 1] == item:
                result = True
                break

        elif direction == dungeon_input.COMMANDS_TYPES[2]:

            if game_map[player_pos[1] + 1][player_pos[0]] == item:
                result = True
                break


        elif direction == dungeon_input.COMMANDS_TYPES[3]:

            if game_map[player_pos[1] - 1][player_pos[0]] == item:
                result = True
                break

    return result


def start():
    """
    Start Game.

    :returns: None.
    :rtype: None.
    """

    global game_map

    while True:

        debug_status = "Off" if custom_log.is_debug else "On"
        string = input(f"Start Game(1)/Load Game(2)/Exit Game(3)/Turn { debug_status } Debug(4):")

        if string == '1':

            game_map = map_generator.create_map(10)
            custom_log.info("Game Started!")
            play()

        elif string == '2':
            game_map = serializer.load_map()

            if game_map == "":
                custom_log.error("Failed to Load Game")
                continue

            custom_log.info("Game Started!")
            play()

        elif string == '3':
            break

        elif string == '4':
            custom_log.toggle_debug()


def print_map():
    """
    Formatted shortcut for printing game_map.

    :returns: None.
    :rtype: None.
    """

    global game_map

    for i in range(len(game_map)):
        custom_log.info((game_map[i]))


def check_status():
    """
    Checks is traps or treasures are near player
    and save result to global variables.

    :returns: None.
    :rtype: None.
    """

    global is_treasure_near_player
    global is_trap_near_player

    is_treasure_near_player = is_item_near_player(map_generator.TREASURE_SYMBOL)
    is_trap_near_player = is_item_near_player(map_generator.TRAP_SYMBOL)


def replace_str_index(text,index=0,replacement=''):
    """
    Replace character at string.

    :param text: string to replace in.
    :text type: str.
    :param index: index of character.
    :index type: int.
    :param replacement: character to replace.
    :replacement type: str.
    :returns: result of check.
    :rtype: bool.
    """

    return '%s%s%s'%(text[:index],replacement,text[index+1:])


def move_player(direction):
    """
    Move player on Game Map.

    :param direction: direction to move.
    :direction type: str.
    :returns: item player stepped on.
    :rtype: str.
    """

    global game_map

    item_stepped_on = map_generator.GROUND_SYMBOL

    player_pos = get_player_pos()

    if direction == dungeon_input.COMMANDS_TYPES[0]:

        item_stepped_on = game_map[player_pos[1]][player_pos[0] - 1]
        game_map[player_pos[1]] = replace_str_index(game_map[player_pos[1]],player_pos[0] - 1, map_generator.PLAYER_SYMBOL)
        
    elif direction == dungeon_input.COMMANDS_TYPES[1]:

        item_stepped_on = game_map[player_pos[1]][player_pos[0] + 1]
        game_map[player_pos[1]] = replace_str_index(game_map[player_pos[1]],player_pos[0] + 1, map_generator.PLAYER_SYMBOL)

    elif direction == dungeon_input.COMMANDS_TYPES[2]:

        item_stepped_on = game_map[player_pos[1] + 1][player_pos[0]]
        game_map[player_pos[1] + 1] = replace_str_index(game_map[player_pos[1] + 1],player_pos[0], map_generator.PLAYER_SYMBOL)

    elif direction == dungeon_input.COMMANDS_TYPES[3]:

        item_stepped_on = game_map[player_pos[1] - 1][player_pos[0]]
        game_map[player_pos[1] - 1] = replace_str_index(game_map[player_pos[1] - 1],player_pos[0], map_generator.PLAYER_SYMBOL)
        
    game_map[player_pos[1]] = replace_str_index(game_map[player_pos[1]], player_pos[0], map_generator.GROUND_SYMBOL)

    return item_stepped_on


def play():
    """
    Function where whole game is happening.

    :returns: None.
    :rtype: None.
    """
    global is_treasure_near_player
    global is_trap_near_player
    global game_map

    custom_log.info("---------------------------------------------------")

    while True:



        valid_direction = get_valid_directions()

        custom_log.info("Input 'save'/'load' to save/load the game.")
        custom_log.info(f"Valid directions - {valid_direction}")

        check_status()

        custom_log.info(f"Traps Near You - {is_trap_near_player}")
        custom_log.info(f"Treasure Near You - {is_treasure_near_player}")

        direction = dungeon_input.get_direction()

        if direction == "save":
            serializer.save_map(game_map)
            continue

        elif direction == "load":
            new_game_map = serializer.load_map()

            if new_game_map == "":
                custom_log.error("Failed to Load Game")
                continue

            game_map = new_game_map
            continue


        if direction not in valid_direction:
            custom_log.warning("Can't move there!")
            continue

        item_stepped_on = move_player(direction)

        custom_log.info("---------------------------------------------------")

        if item_stepped_on == map_generator.TRAP_SYMBOL:
            end_game()
            break
        elif item_stepped_on == map_generator.TREASURE_SYMBOL:
            win_game()
            break


def end_game():
    """
    Ends game prints map.

    :returns: None.
    :rtype: None.
    """
    custom_log.info("You Lost!")
    print_map()


def win_game():
    """
    Wins game prints map.

    :returns: None.
    :rtype: None.
    """
    custom_log.info("You Won!")
    print_map()


if __name__ == "__main__":
    start()
