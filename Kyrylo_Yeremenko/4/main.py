"""
This module is starting point for task 4.1 from Coding Campus 2018 Python course
(Dungeon Game)
"""

import logging
from dungeon_map import DungeonMap
from player import Player
import utils
import log
from decorators import log_decorator, debug_log_decorator
import config

SAVE_PATH = "save.dat"
logger = logging.getLogger(log.LOGGER_NAME)

active_map = None
active_player = None


def predicate_map_size(string):
    """
    Predicate for map size input
    :param string: String to check
    :return: Tuple of bool and string, where bool signifies result, and string - error message
    """
    bool_result = False
    str_result = ""

    if string.isdigit():

        size = int(string)
        if 5 <= size <= 100:
            bool_result = True
        else:
            str_result = "Unacceptable map size! Try again"
    else:
        str_result = "Input is not integer! Try again"

    return bool_result, str_result


def predicate_movement_string(string):
    """
    Predicate for player move direction input
    :param string: String to check
    :return: Tuple of bool and string, where bool signifies result, and string - error message
    """
    bool_result = False
    str_result = ""

    if string.lower() == "u":
        bool_result = True
    elif string.lower() == "l":
        bool_result = True
    elif string.lower() == "r":
        bool_result = True
    elif string.lower() == "d":
        bool_result = True
    else:
        str_result = "Incorrect movement direction!\nPlayer can move up [U], left [L], right [R] or down [D]\n"

    return bool_result, str_result


def predicate_response(string):
    """
    Predicate for yes/no response input
    :param string: String to check
    :return: Tuple of bool and string, where bool signifies result, and string - error message
    """
    bool_result = False
    str_result = ""

    if string.lower() == "n" or string.lower() == "y":
        bool_result = True
    else:
        str_result = "Incorrect answer!"

    return bool_result, str_result


def predicate_command(string):
    """
    Predicate for command input
    :param string: String to check
    :return: Tuple of bool and string, where bool signifies result, and string - error message
    """
    bool_result = False
    str_result = ""

    if string.lower() == "move" or string.lower() == "save":
        bool_result = True
    else:
        str_result = "Incorrect command!"

    return bool_result, str_result


@log_decorator
@debug_log_decorator
def play_game():
    """
    Plays single game of Dungeon Game
    :return: None
    """

    while True:

        is_trap_nearby, is_treasure_nearby = active_map.check_nearby_tiles(active_player.position)

        print("\n\n")

        if is_trap_nearby:
            print("Your senses detect a trap in nearby tile. Watch your step!")
        if is_treasure_nearby:
            print("Radiant glow gives away treasure's location in nearby tile. Target is close!")

        logger.info(f"Player position {active_player.position}")
        print(f"Your position is ({active_player.position[1]}, {active_player.position[0]})")
        print(f"Your health is {active_player.hitpoints} HP")
        print(f"Your bag has space for {config.PLAYER_BAG_SIZE - active_player.bag } more chests.\n")

        command = utils.get_input(predicate_command, "Input command [Save] or [Move]: ")
        if command.lower() == "save":

            if utils.save_game(SAVE_PATH, active_map, active_player):
                print("Game saved!")
            else:
                print("Save failed!")

            continue

        while True:

            move_direction = utils.get_input(predicate_movement_string, "Input direction to move in: ")
            if active_player.move(move_direction.lower(), active_map):

                logger.info(f"Player moves {active_player.position[1]}, {active_player.position[0]}")
                break
            else:
                print("You can't move there! Try again\n")

        is_trap, is_treasure = active_map.check_current_tile(active_player.position)

        if is_trap:

            logger.info(f"Player is damaged by 1 hitpoint. Hitpoints left: {active_player.hitpoints - 1}")
            print("You spring the trap and it firmly clenches around your leg.")
            active_player.hitpoints -= 1

            if active_player.is_dead():

                logger.info("Player is killed")
                print("You loose too much blood trying to remove it and give in to darkness.")
                print("Dungeon consumes you!")
                break

            else:

                print("You manage to remove the trap suffering minor wounds.")
                active_map.game_map[active_player.position[0]][active_player.position[1]] = DungeonMap.SYMBOL_PLAYER

        if is_treasure:

            logger.info(f"Player found the treasure. Current bag size: {active_player.bag + 1}")
            print("Shimmering glow and warmth leads you to open chest filled with gold. You fill your bag with contents of the chest.")
            active_player.bag += 1

            if active_player.is_bag_full():

                logger.info("Player filled the bag")
                print("Feeling you can't carry anymore, you backtrack to dungeon exit with the bag full of gold.")
                print("You escaped the dungeon!")
                break

            else:

                print("Your bag feels a little heavier, but there is still space for more. You continue your journey.")
                active_map.game_map[active_player.position[0]][active_player.position[1]] = DungeonMap.SYMBOL_PLAYER

    active_player.mark_last_pos(active_map)
    logger.info("Game over")


@log_decorator
@debug_log_decorator
def init_game():
    """
    Initializes game map and player position
    :return: None
    """

    global active_map
    global active_player

    map_size = utils.get_input(predicate_map_size, "Input map size [5 - 100]: ")
    active_map = DungeonMap(int(map_size))
    active_player = Player(active_map)


@log_decorator
@debug_log_decorator
def start_game():
    """
    Start game dialog
    :return: None
    """

    global active_map
    global active_player

    active_map = DungeonMap(int(0))
    active_player = Player(active_map)

    response = utils.get_input(predicate_response, "Do you wish to load last saved game? [Y\\N]: ")

    if response.lower() == 'y':

        if not utils.load_game(SAVE_PATH, active_map, active_player):

            print("Failed to load saved game! Starting new game")
            init_game()

    else:

        logger.info("Starting new game.")
        init_game()


if __name__ == "__main__":

    print("Welcome to Dungeon Game!")
    log.init_logger()

    while True:

        start_game()
        play_game()

        print("\nGAME OVER\n")
        active_map.print_map()

        response = utils.get_input(predicate_response, "Try again? [Y\\N]: ")

        if response.lower() == 'n':
            break
        else:
            logger.info("User is restarting the game")

    logger.info("User quit the game")
    print("\nQuitting game...")
