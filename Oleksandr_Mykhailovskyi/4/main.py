import string

import map_generator
import game_utilities
import savegame_utility
from game_utilities import game_step


def main():
    print("Wilkommen im Dungeon Game!\n")

    while True:
        game_map = game_utilities.game_setup()
        input_action = input("Load game?Y/N\n")
        input_action = input_action.casefold()

        if(input_action == "Y".casefold()):
            game_map, game_utilities.position = savegame_utility.load()
            game_utilities.logger.info("game loaded")
            print("game loaded")

        result = True
        while result:
            result = game_step(game_map)

        input_action = input("Continue?Y/N\n")
        input_action = input_action.casefold()

        if input_action == "N".casefold():
            return


if __name__ == '__main__':
    main()
