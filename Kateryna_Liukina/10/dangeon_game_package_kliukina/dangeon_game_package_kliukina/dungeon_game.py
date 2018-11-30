from .game_logger import logger, log_decorator, debug_decorator 
from .custom_exeption import InvalidDirectionError, InvalidMapSizeError, InvalidSaveDataError
from . import game_map
from . import player
import math
import pickle
from . import enemy
from threading import Thread

"""
https://test.pypi.org/project/dungeon-game-kliukina/
"""

@log_decorator
@debug_decorator
def dungeon_game():
    """
    Function launch the dungeon game
    Returns:
        None
    """
    while True:
        try:
            size_of_map = int(input("Enter size of map"))
            game_map_ = game_map.GameMap([size_of_map] * 2, 0.1, 0.05)
        except (InvalidMapSizeError, ValueError) as error:
            logger.warning(error)
        else:
            break
    
    player_ = player.Player(game_map_)

    game_over = False
    player_win = False

    run_enemy(game_map_, player_)
    
    while not game_over:

        player_.print_info()

        player_.generate_warning(game_map_, 1)
        player_.generate_warning(game_map_, 2)
        
        while True:
            try:
                game_input = input("Enter direction\n")
                if game_input == "save":
                    save(game_map_, player_)
                    logger.info("Game is saved")
                elif game_input == "load":
                    game_map_, player_ = load()
                    logger.info("Game is loaded")
                else:               
                    player_.move(game_map_, game_input)
            except (InvalidDirectionError, InvalidSaveDataError) as error:
                logger.warning(error)
            except FileNotFoundError:
                logger.warning("No saved game")
            except (pickle.UnpicklingError, MemoryError):                
                logger.warning("Invalid save file")
            else:
                break

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
    
    if not isinstance(game_save, list) or len(game_save) != 4:
             InvalidSaveDataError
    
    list_with_map = game_save[0]
    game_map_ = GameMap([len(list_with_map), len(list_with_map[0])], 0.1, 0.05)
    game_map_.map_ = list_with_map
    player_ = Player(game_map_)
    player_.position = game_save[1]
    player_.hp = game_save[2]
    player_.treasure = game_save[3]
    return game_map_, player_  

    
@log_decorator
@debug_decorator
def run_enemy(game_map_, player_):
    """
    Function create enemy and thread
    Args:
        game_map_(GameMap): game map to save
        player_(Player): player to save
    Returns:
        None
    """
    enemy_ = enemy.Enemy(game_map_)
    enemy_thread = Thread(target = enemy_.run_logic, args = (game_map_, player_))
    enemy_thread.setDaemon(True)
    enemy_thread.start()


dungeon_game()

