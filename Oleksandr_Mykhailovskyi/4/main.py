import string

import savegame_utility

import logging_utility
from logging_utility import logger

from game_world import GameWorld


def main():
    print("Wilkommen im Dungeon Game!\n")
    print("To save game just enter save during your turn")

    while True:
        logger.info("game started")
        logging_utility.debug_mode = False

        input_action = input("enable debug mode?Y/N\n")
        input_action = input_action.casefold()

        if input_action == "Y".casefold():
            logging_utility.debug_mode = True

        result = True
        while result:
            game_world = GameWorld()
            game_world.update_loop()

        input_action = input("Continue?Y/N\n")
        input_action = input_action.casefold()

        if input_action == "N".casefold():
            return


if __name__ == '__main__':
    main()
