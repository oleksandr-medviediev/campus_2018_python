import string

import savegame_utility

import logging_utility
from logging_utility import logger

from game_world import GameWorld


def main():
    """
    Main function - starter for dungeon game.
    Package - pip install dungeon-game-mykhailovskyi.
    URL: https://pypi.org/project/dungeon-game-mykhailovskyi/
    """
    print("Wilkommen im Dungeon Game!\n")
    print("To save/load game just enter save/load during your turn")

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
    try:
        main()
    except KeyboardInterrupt as identifier:
        print("Understandable, for you to know - \
         you could just write \'exit\'")
