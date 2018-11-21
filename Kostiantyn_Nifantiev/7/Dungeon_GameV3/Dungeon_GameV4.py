from dungeon_game import Game
from dungeon_logger import my_logger


game_instance = Game()

while True:

    game_instance.setup_game()

    while(game_instance.run_farame()):

        pass

    decision = input('Do you want to play again? y/n:\n')

    if decision == 'y':

        my_logger.debug("Restarting game")
        continue

    else:

        my_logger.debug("Abandoning game")
        break
