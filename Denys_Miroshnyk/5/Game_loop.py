import Map_generator
import Save_load
from Custom_logger import logger as log

player_position = (-1, -1)

player_actions = {1: 'up', 2: 'down',
                  3: 'right', 4: 'left', 5: 'load', 6: 'save'}
player_actions_callbacks = {
    1: lambda point: [point[0], point[1] + 1],
    2: lambda point: [point[0], point[1] - 1],
    3: lambda point: [point[0] + 1, point[1]],
    4: lambda point: [point[0] - 1, point[1]]}


def player_input(game_map):
    log.debug("player_input function called")
    global player_position

    log.info(
        f"Your action :{[f'{key} - {val},' for key, val in player_actions.items()]}")
    action = int(input())

    result = True
    log.debug(f"player_input: the action is {player_actions[action]}")

    if action in range(1, 5):
        player_position_new = player_actions_callbacks[action](player_position)
        cell_type = game_map[player_position_new[1]][player_position_new[0]]

        if cell_type == Map_generator.treasure or cell_type == Map_generator.trap:
            player_position = player_position_new
            result = False
            log.debug(f"player_input: player found a {cell_type}")
        elif cell_type == Map_generator.wall:
            log.info("you found the wall. Can't move further")
        else:
            game_map[player_position[1]][player_position[0]
                                         ] = Map_generator.empty_cell
            player_position = player_position_new
            game_map[player_position[1]][player_position[0]
                                         ] = Map_generator.player
            log.debug(
                f"_player_input: player new pos({player_position[0]}, {player_position[1]})")
    elif action == 5:
        game_map = Save_load.load_game()
    elif action == 6:
        Save_load.save_game(game_map)
    else:
        print("invalid input \n")

    return result


def print_state(game_map):
    log.debug("print_state function called")
    global player_position

    for val in player_actions_callbacks.values():
        player_neighbored_point = val(player_position)
        if game_map[player_neighbored_point[1]][player_neighbored_point[0]] == Map_generator.trap:
            log.info("trap is somewhere near")
        elif game_map[player_neighbored_point[1]][player_neighbored_point[0]] == Map_generator.treasure:
            log.info("Treasure is somewhere near")


def loop(game_map):
    log.debug("loop function called")
    global player_position
    print_state(game_map)

    while player_input(game_map):
        log.debug("loop next iteration:")
        print_state(game_map)

    cell_type = game_map[player_position[1]][player_position[0]]
    if cell_type == Map_generator.treasure:
        log.info("you found the treasure! Victory")
    else:
        log.info("Trap *traps*\n You *lost* xD")
