"""main module for Dungeon Game
"""

import terrain
import game
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

message_handler = logging.StreamHandler()
message_handler.setLevel(logging.INFO)

logger.addHandler(message_handler)

logger.info("Welcome to the game!")
logger.info("Type up/down/left/right to move")

while True:

    scale = input("Enter map scale: ")

    start_row, start_col, squares_map = terrain.generate(int(scale))

    game.run(start_row, start_col, squares_map)

    for row in squares_map:
        logger.info(row)

    logger.info("\n* - stands for a treasure")
    logger.info("t - stands for a trap")
    logger.info(". - stands for an empty square")
    logger.info("s - stands for the start position\n")

    answer = input("Play again? (y/n): ")

    if answer != 'y':
        break
