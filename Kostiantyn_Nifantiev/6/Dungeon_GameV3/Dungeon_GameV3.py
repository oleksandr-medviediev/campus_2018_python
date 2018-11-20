from game_functions import game_loop
from dungeon_logger import my_logger
from dungeon_logger import log_decorator

while True:

    my_logger.debug("Entering main game function")

    game_loop()

    my_logger.debug("Main game function has finished")

    decision = input('Do you want to play again? y/n:\n')

    if decision == 'y':

        my_logger.debug("Restarting game")
        continue

    else:

        my_logger.debug("Abandoning game")
        break


