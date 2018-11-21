"""main module for Dungeon Game
"""

import pickle
import os.path

from game_logger import log_debug
from game_logger import log_info

import terrain
import game


debug_mode = False

start_row = 0
start_col = 0
squares_map = []

log_info("Welcome to the game!")

while True:

    log_info("Type \"new\" to start new game")
    log_info("Type \"load\" to load saved game")
    log_info("Type \"debug\" to enter debug mode")

    command = input()

    if command == "new":

        scale = input("Enter map scale: ")
        start_row, start_col, squares_map = terrain.generate(int(scale))
        log_debug("new game created")
        break

    elif command == "load":

        if os.path.exists("sav.txt"):

            with open("sav.txt", "rb") as savefile:

                start_row, start_col, squares_map = pickle.load(savefile)
                log_debug("game loaded")
                break

        else:

            log_info("No save file found :(")
            continue

    elif command == "debug":

        if debug_mode: 
            log_info("Already in debug mode")

        else:

            debug_mode = True
            log_info("Game is run in debug mode")

    else:
        log_info(F"Unknown command: {command}")


start_position_message = F"start position: ({start_row}, {start_col})"
log_debug(start_position_message)
log_debug("map:")

for row in squares_map:
    log_debug(row)


game.run(start_row, start_col, squares_map)

for row in squares_map:
    log_info(row)

log_info("* - stands for a treasure")
log_info("t - stands for a trap")
log_info(". - stands for an empty square")
log_info("s - stands for the start position\n")
