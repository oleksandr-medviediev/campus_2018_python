"""main module for Dungeon Game
"""

from game_logger import log_debug
from game_logger import log_info

import terrain
import game


debug_mode = False

log_info("Welcome to the game!")

game_session = None

while True:

    log_info("Type \"new\" to start new game")
    log_info("Type \"load\" to load saved game")
    log_info("Type \"debug\" to enter debug mode")

    command = input()

    if command == "new":

        scale = input("Enter map scale: ")
        game_session = game.GameSession(3, 3, int(scale))
        log_debug("new game created")
        break

    elif command == "load":

        game_session = game.GameSession()
        if game_session.load():
            break

    elif command == "debug":

        if debug_mode:
            log_info("Already in debug mode")

        else:

            debug_mode = True
            log_info("Game is run in debug mode")

    else:
        log_info(F"Unknown command: {command}")

game_session.run()
