from Game_logger import logger
from Game_logger import log_decorator
from Game_logger import debug_decorator
import game_map
import player
import math
import pickle
from functools import partial



@log_decorator
@debug_decorator
def dungeon_game():
    """
    Function launch the dungeon game
    Returns:
        None
    """
    size_of_map = int(input("Enter size of map"))
    game_map_ = game_map.GameMap([size_of_map] * 2, 0.1, 0.05)

    player_ = player.Player(game_map_)

    direction_map = {'up': [1, 0], 'down': [-1, 0], 'left': [0, -1], 'right': [0, 1]}

    game_over = False
    player_win = False

    while not game_over:

        player_.print_info()

        player_.generate_warning(game_map_, 1)
        player_.generate_warning(game_map_, 2)

        game_input = input("Enter direction\n")
        if game_input == "save":
            save(game_map_, player_)
            logger.info("Game is saved")
            continue
        elif game_input == "load":
            game_map_, player_ = load()
            logger.info("Game is loaded")
            continue
        else:
            direction = direction_map[game_input]

        player_.move(game_map_, direction)

        player_win = player_.is_won()
        game_over = player_win or player_.is_lost()

    if player_win:
        print("You won!!!")
    else:
        print("You lost.")
    print(game_map_)

	
@log_decorator
@debug_decorator
def save(game_map_, player_):
    """
    Function save the game
    Args:
        game_map_(GameMap): game map to save
        player_(Player): player to save
    Returns:
        None
    """
    with open('save.pickable', 'wb') as handle:
        pickle.dump([game_map_.map_, player_.position, player_.hp, player_.treasure], handle)

		
@log_decorator
@debug_decorator
def load():
    """
    Function load the game
    Returns:
        (GameMap, Player)
    """
    with open('save.pickable', 'rb') as handle:
        game_save = pickle.load(handle)

    list_with_map = game_save[0]
    game_map_ = GameMap([len(list_with_map), len(list_with_map[0])], 0.1, 0.05)
    game_map_.map_ = list_with_map
    player_ = Player(game_map_)
    player_.position = game_save[1]
    player_.hp = game_save[2]
    player_.treasure = game_save[3]
    return game_map_, player_


dungeon_game()

