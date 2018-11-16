from Game_logger import logger
from Game_logger import log_decorator
import Map_generator
import Warning_generator
import math
import pickle
from functools import partial



@log_decorator
def dungeon_game():
    """
    Function launch the dungeon game
    Returns:
        none
    """
    size_of_map = int(input("Enter size of map"))
    game_map = Map_generator.generate_map([size_of_map] * 2, 0.1, 0.05)

    player_position = Map_generator.generate_coordinates(game_map)
    direction_map = {'up': [1, 0], 'down': [-1, 0], 'left': [0, -1], 'right': [0, 1]}

    game_over = False
    player_win = False

    while not game_over:
        logger.info("Your position:" + str(player_position))
        Warning_generator.generate_warning(game_map, player_position, 1)
        Warning_generator.generate_warning(game_map, player_position, 2)

        game_input = input("Enter direction")
        if game_input == "save":
            save(game_map, player_position)
            logger.info("Game is saved")
            continue
        elif game_input == "load":
            game_map, player_position = load()
            logger.info("Game is loaded")
            continue
        else:
            direction = direction_map[game_input]

        player_position[0] += direction[0]
        player_position[1] += direction[1]

        player_position[0] = max(0, min(player_position[0], size_of_map - 1))
        player_position[1] = max(0, min(player_position[1], size_of_map - 1))

        if game_map[player_position[0]][player_position[1]] == 1:
            game_over = True

        elif game_map[player_position[0]][player_position[1]] == 2:

            game_over = True
            player_win = True

    if player_win:
        print("You won!!!")
    else:
        print("You lost.")
    print(game_map)

@log_decorator
def save(game_map, player_position):
    """
    saves level in file
        :param str lvl: string level representation
        :param int player_x: current x-position of player
        :param int player_y: current y-position of player
    """

    with open('save.pickable', 'wb') as handle:
        pickle.dump([game_map, player_position], handle)

@log_decorator
def load():
    """
    loads level from file
    :return: loaded level
    :rtype: tuple
    """

    with open('save.pickable', 'rb') as handle:
        game_save = pickle.load(handle)

    game_map = game_save[0]
    player_position = game_save[1]

    return game_map, player_position


dungeon_game()

