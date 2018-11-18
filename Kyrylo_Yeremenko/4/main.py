"""
This module is starting point for task 4.1 from Coding Campus 2018 Python course
(Dungeon Game)
"""

import logging
import dungeon_map
import player
import utils
import log
from decorators import log_decorator

SAVE_PATH = "save.dat"
logger = logging.getLogger(log.LOGGER_NAME)


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
def play_game():
    """
    Plays single game of Dungeon Game
    :return: None
    """

    while True:

        is_trap_nearby, is_treasure_nearby = dungeon_map.check_nearby_tiles(player.position)

        print("\n\n")

        if is_trap_nearby:
            print("Your senses detect a trap in nearby tile. Watch your step!")
        if is_treasure_nearby:
            print("Radiant glow gives away treasure's location in nearby tile. Target is close!")

        logger.info(f"Player position {player.position}")
        print(f"Your position is ({player.position[1]}, {player.position[0]})\n")

        command = utils.get_input(predicate_command, "Input command [Save] or [Move]: ")
        if command.lower() == "save":

            if utils.save_game(SAVE_PATH):
                print("Game saved!")
            else:
                print("Save failed!")

            continue

        while True:

            move_direction = utils.get_input(predicate_movement_string, "Input direction to move in: ")
            if player.move(move_direction.lower()):

                logger.info(f"Player moves {player.position[1]}, {player.position[0]}")
                break
            else:
                print("You can't move there! Try again\n")

        is_trap, is_treasure = dungeon_map.check_current_tile(player.position)

        if is_trap:

            logger.info("Player is killed")
            print("You spring the trap and, unable to react, suffer mortal wounds.")
            print("Darkness of Dungeon consumes you!")
            break

        if is_treasure:

            logger.info("Player found the treasure")
            print("Shimmering glow and warmth leads you to open chest filled with gold. You close the chest, lift it and get out of there.")
            print("You escaped the Dungeon!")
            break

    player.mark_last_pos()
    logger.info("Game over")


@log_decorator
def init_game():
    """
    Initializes game map and player position
    :return: None
    """

    map_size = utils.get_input(predicate_map_size, "Input map size [5 - 100]: ")
    dungeon_map.generate(int(map_size))
    player.init_position()


@log_decorator
def start_game():
    """
    Start game dialog
    :return: None
    """

    response = utils.get_input(predicate_response, "Do you wish to load last saved game? [Y\\N]: ")

    if response.lower() == 'y':

        if not utils.load_game(SAVE_PATH):

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
        dungeon_map.print_map()

        response = utils.get_input(predicate_response, "Try again? [Y\\N]: ")

        if response.lower() == 'n':
            break
        else:
            logger.info("User is restarting the game")

    logger.info("User quit the game")
    print("\nQuitting game...")
