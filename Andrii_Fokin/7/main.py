

import Game_
import dg_decorators

dg_decorators.DEBUG_MODE = True


@dg_decorators.decorator_start_end_logging
def main():

    while input("Start the Game? y/n : ") == 'y':
        player_answer = input('(1) new game or (2) saved game : ')
        game = Game_.Game()

        if player_answer == '2':
            game.load()

        print(game)
        game.loop()



main()
