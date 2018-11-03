import string

import map_generator
import game_utilities
from game_utilities import game_step


def main():
    print("Wilkommen im Dungeon Game!\n")

    while True:
        game_map = game_utilities.game_setup()

        result = True
        while result:
            result = game_step(game_map)

        input_action = input("Continue?Y/N\n")
        input_action = input_action.casefold()

        if input_action.count("N".casefold()) == 1:
            return


if __name__ == '__main__':
    main()
