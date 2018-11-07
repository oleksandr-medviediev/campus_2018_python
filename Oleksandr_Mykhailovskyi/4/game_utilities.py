import random
from logging_utility import logger

import map_generator
from map_generator import player_repr
from map_generator import fog_repr
from map_generator import unknown_repr
from map_generator import map_cells_repr
from map_generator import map_elements
import savegame_utility

# Game info
position = [-1, -1]
view_depth = [1, 1]

actions_list = ["up", "left", "down", "right", "save"]

action_dict = {
    actions_list[0]: "w",
    actions_list[1]: "a",
    actions_list[2]: "s",
    actions_list[3]: "d",
    actions_list[4]: "save"
}


def format_cell(mstr, cell_index):
    """
    Gets str reprs regarding player pos.

    Args:
        mstr (str): str repr of cell.
        cell_index ([int, int]): cell index
    Returns:
        str - repr of cell regarding player pos.
    """
    mrepr = ""
    if cell_index[0] == position[0] and cell_index[1] == position[1]:
        mrepr = player_repr
    elif cell_index[0] > position[0] + view_depth[0] or cell_index[1] > position[1] + view_depth[1]:
        mrepr = fog_repr
    elif cell_index[0] < position[0] - view_depth[0] or cell_index[1] < position[1] - view_depth[1]:
        mrepr = fog_repr
    elif mstr == map_elements[1][1] or mstr == map_elements[2][1]:
        mrepr = unknown_repr
    else:
        mrepr = mstr
    return mrepr


def format_output(game_map):
    """
    Shows map.

    Args:
        game_map ([[str...]...]): game map.
    """

    print(position)

    printed = str()
    for index_i, i in enumerate(game_map):
        for index_j, j in enumerate(i):
            printed += format_cell(j, [index_i, index_j])
        printed += "\n"
    print(printed)


def get_map_cell(position, game_map):
    """
    Little hack ot check cell's around player
    when he's on the border.

    Args:
        position ((int,int)): position to check.
        game_map ([[str...]...]): game map generated by game_generator module.

    Returns:
        cell content if position is valid.
        map_cells_repr[0] - for non-valid position.
    """
    size = len(game_map)
    if position[0] >= size or position[0] < 0 or \
            position[1] >= size or position[0] < 0:

        return map_cells_repr[0]

    return game_map[position[0]][position[1]]


def get_action():
    """
    Returns:
        str - Action mapped on input.
        If no action / no such action - None
    """

    input_action = input("Your turn\n")
    for key in action_dict.keys():
        if input_action == action_dict[key]:
            return key
    return None


def check_position(position, game_map):
    """
    Checks whether position is acceptable.

    Args:
        position ((int,int)): position to check.
        game_map ([[str...]...]): game map generated by game_generator module.
    Returns:
        True if acceptable.
        False otherwise.
    """
    size = len(game_map)
    returnFlag = True
    if position[0] >= size or position[1] >= size:
        returnFlag = False
    elif position[0] < 0 or position[1] < 0:
        returnFlag = False
    return returnFlag


def move_player(action, position, game_map):
    """
    Moves player on the map.

    Args:
        action (str): action from action dict.
        position ((int,int)): position to check.
        game_map ([[str...]...]): game map generated by game_generator module.
    Returns:
        [int, int] - list, new position.
    """
    oldPosition = list(position)
    if action == actions_list[0]:
        # Move up
        position[1] += 1
    elif action == actions_list[1]:
        # Move left
        position[0] -= 1
    elif action == actions_list[2]:
        # Move down
        position[1] -= 1
    elif action == actions_list[3]:
        # Move right
        position[0] += 1

    if not check_position(position, game_map):
        return oldPosition
    return position


def on_action(action, game_map):
    """
    Args:
        action (str): actions from the actions list
        position ([int, int]): playuer's position
        game_map ([[str...]...]): game map
    """

    global position
    if action == actions_list[4]:
        savegame_utility.save(game_map, position)
        logger.info("game saved")
    else:
        position = move_player(action, position, game_map)


def generate_random_position(game_map):
    """
    Args:
        game_map ([[str...]...]): game map generated by game_generator module.
    Returns:
        [int, int] - list, new position.
    """
    size = len(game_map)
    pos = [random.randint(0, size - 1), random.randint(0, size - 1)]
    return pos


def game_setup():
    """
    Gets all things ready to start the game.

    Returns:
        game_map ([[str...]...]): game map generated by game_generator module.
    """
    logger.debug("setting-up started...")
    game_map = map_generator.generate_random_map(True)
    logger.debug("map generated")
    global position
    position = generate_random_position(game_map)
    logger.debug("start position generated")
    logger.debug("setting-up ended.")
    return game_map


def get_warning(position, game_map):
    """
    Get str warning - if anything in range 1 of it
    can lead to defeat/win.

    Args:
        position ((int,int)): position to check.
        game_map ([[str...]...]): game map generated by game_generator module.
    Returns:
        str - warning if something is present in player's view.
        str - empty otherwise.
    """
    print(position)
    mwarning = ""

    positions = []

    positions.append([position[0], position[1] + view_depth[1]])
    positions.append([position[0], position[1] - view_depth[1]])
    positions.append([position[0] + view_depth[0], position[1]])
    positions.append([position[0] - view_depth[0], position[1]])

    for pos in positions:
        cell = get_map_cell(pos, game_map)
        if cell == map_cells_repr[1]:
            mwarning = "Achtung, you just might win!\n"
        elif cell == map_cells_repr[2]:
            mwarning += "Achtung, you can loose!\n"

    return mwarning


def game_update_position(position, game_map):
    """
    Update game state depending on cell.

    Args:
        position ((int,int)): position to check.
        game_map ([[str...]...]): game map generated by game_generator module.
    Returns:
        1 - win.
        0 - nothing.
        -1 - loss.
    """

    cell = game_map[position[0]][position[1]]
    if cell == map_cells_repr[1]:
        return 1
    elif cell == map_cells_repr[2]:
        print(map_cells_repr[2])
        return -1
    return 0


def game_step(game_map):
    """
    Main game step.

    Args:
        game_map ([[str...]...]): game map generated by game_generator module.
    Returns:
        False when game is over.
        True otherwise.
    """
    logger.debug("step started...")
    global position

    format_output(game_map)
    print(get_warning(position, game_map))
    logger.debug("output completed")

    action = get_action()
    if action is None:
        return True
    logger.debug("action received & checked")

    on_action(action, game_map)
    logger.debug("on action script performed")

    step_result = game_update_position(position, game_map)
    logger.debug("new position checked and used, step performed")

    res = True
    if step_result == 1:
        print("Congratulations, winner!")
        logger.info("game won.")
        res = False
    elif step_result == -1:
        print("You lost")
        logger.info("game lost.")
        res = False

    logger.debug("step ended.")
    return res
