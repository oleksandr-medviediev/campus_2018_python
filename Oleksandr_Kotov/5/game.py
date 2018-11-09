"""main game logic
"""

import pickle
from contextlib import contextmanager

from game_logger import logger


def _structure_is_near(structure, curr_row, curr_col, squares_map):
    """find if given structure is within one square

    Arguments:
        structure str -- structure to find
        curr_row int -- current player row
        curr_col int -- current player column
        squares_map [str] -- game map

    Returns:
        bool -- true if given structure is within one square, false otherwise
    """

    is_near = False
    scale = len(squares_map)

    if curr_col < scale - 1:
        if squares_map[curr_row][curr_col + 1] == structure:
            is_near = True

    if curr_col > 1:
        if squares_map[curr_row][curr_col - 1] == structure:
            is_near = True

    if curr_row < scale - 1:
        if squares_map[curr_row + 1][curr_col] == structure:
            is_near = True

    if curr_row > 1:
        if squares_map[curr_row - 1][curr_col] == structure:
            is_near = True

    return is_near


def _write_move_fail_to_log(dir):
    """write fail while moving in specified directoin to log

    Arguments:
        dir str -- move direction
    """

    logger.debug(F"failed to move {dir}")


def run(start_row, start_col, squares_map):
    """run the game

        function is proceeded until player finds a treasure or enters a trap

    Arguments:
        start_row int -- start position row
        start_col int -- start position column
        squares_map [str] -- game map
    """

    logger.info("Type \"up/down/left/right\" to move")
    logger.info("Type \"save\" to save current game")

    border = len(squares_map) - 1

    curr_row = start_row
    curr_col = start_col

    while True:

        if squares_map[curr_row][curr_col] == 't':

            logger.debug("player has found a treasure")
            logger.debug("game ends")
            logger.info("You have entered a trap!")
            break

        if squares_map[curr_row][curr_col] == '*':

            logger.debug("player has entered a trap")
            logger.debug("game ends")
            logger.info("You have found a treasure!")
            break

        if _structure_is_near('t', curr_row, curr_col, squares_map):

            logger.debug("trap is within one square")
            logger.info('There is a trap within one square!')

        if _structure_is_near('*', curr_row, curr_col, squares_map):

            logger.debug("treasure is within one square")
            logger.info('There is a treasure within one square!')

        moved = False

        while not moved:

            command = input("What to do?: ")

            if command == 'up':

                if curr_row == 0:

                    logger.info("You are already on top of the map!")
                    _write_move_fail_to_log(command)

                else:

                    moved = True
                    curr_row -= 1
                    logger.info("Moving up")

            elif command == 'down':

                if curr_row == border:

                    logger.info("You are already on bottom of the map!")
                    _write_move_fail_to_log(command)

                else:

                    moved = True
                    curr_row += 1
                    logger.info("Moving down")

            elif command == 'right':

                if curr_col == border:

                    msg = "You are already on the right border of the map!"
                    logger.info(msg)
                    _write_move_fail_to_log(command)

                else:

                    moved = True
                    curr_col += 1
                    logger.info("Moving right")

            elif command == 'left':

                if curr_col == 0:

                    msg = "You are already on the left border of the map!"
                    logger.info(msg)
                    _write_move_fail_to_log(command)

                else:

                    moved = True
                    curr_col -= 1
                    logger.info("Moving left")

            elif command == "save":

                with open("sav.txt", "wb") as savefile:

                    data_to_save = [curr_row, curr_col, squares_map]
                    pickle.dump(data_to_save, savefile, protocol=0)
                    logger.info("Saved succesfully")

            else:
                logger.info(F"Unknown command: {command}")

            if moved:

                logger.debug(F"moved {command}")
                cur_pos_msg = F"current position: ({curr_row}, {curr_col})"
                logger.debug(cur_pos_msg)
