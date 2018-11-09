"""main module for Dungeon Game
"""

import pickle
import os.path

import terrain
import game
from game_logger import logger


start_row = 0
start_col = 0
squares_map = []

logger.info("Welcome to the game!")

while True:

    logger.info("Type \"new\" to start new game")
    logger.info("Type \"load\" to load saved game")
    command = input()

    if command == "new":

        scale = input("Enter map scale: ")
        start_row, start_col, squares_map = terrain.generate(int(scale))
        logger.debug("new game created")
        break

    elif command == "load":

        if os.path.exists("sav.txt"):

            with open("sav.txt", "rb") as savefile:

                start_row, start_col, squares_map = pickle.load(savefile)
                logger.debug("game loaded")
                break

        else:

            logger.info("No save file found :(")
            continue

    logger.info(F"Unknown command: {command}")


start_position_message = F"start position: ({start_row}, {start_col})"
logger.debug(start_position_message)
logger.debug("map:")
for row in squares_map:
    logger.debug(row)


game.run(start_row, start_col, squares_map)

for row in squares_map:
    logger.info(row)

logger.info("* - stands for a treasure")
logger.info("t - stands for a trap")
logger.info(". - stands for an empty square")
logger.info("s - stands for the start position\n")
