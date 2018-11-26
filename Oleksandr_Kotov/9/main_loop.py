"""main module for Dungeon Game
"""
import exceptions

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

    try:
        command = input()

        if command == "new":

            try:

                scale = int(input("Enter map scale: "))

                if (scale < 1):
                    raise exceptions.TerrainGenerationError(scale)

            except exceptions.TerrainGenerationError as instance:
                log_info(instance)
                continue
                
            except ValueError:
                log_info(F"Entered scale is not an integer: {scale}")
                continue

            game_session = game.GameSession(3, 3, int(scale))
            log_debug("new game created")
            break

        elif command == "load":

            game_session = game.GameSession(0, 0, 1)
            if game_session.load():
                break

        elif command == "debug":

            if debug_mode:
                log_info("Already in debug mode")

            else:

                debug_mode = True
                log_info("Game is run in debug mode")

        else:
            raise exceptions.MenuCommandError(command)

    except exceptions.MenuCommandError as instance:
            log_info(instance)

try:
    game_session.run()

except AttributeError:
    log_info("Game was not initialized. Ending")
