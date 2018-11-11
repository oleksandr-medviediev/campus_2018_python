import pickle
import logging
import dungeon_map
import player
import log


logger = logging.getLogger(log.LOGGER_NAME)


def get_input(predicate, input_message):
    """
    Gets input from user satisfying given predicate
    :param predicate: Predicate, accepts string, returns tuple of Bool and string (error message)
    :param input_message: Message to display user
    :return: Accepted string
    """

    return_string = ""
    while True:

        string = input(input_message)
        predicate_result, predicate_error_string = predicate(string)

        if predicate_result:

            return_string = string
            break
        else:
            print(predicate_error_string)

    return return_string


def vector_sum(lhs, rhs):
    """
    Calculates sum of XY vector
    :param lhs: Tuple/List containing X and Y coordinates as index 0 and 1
    :param rhs: Tuple/List containing X and Y coordinates as index 0 and 1
    :return: List containing X and Y sum
    """
    return [lhs[0] + rhs[0], lhs[1] + rhs[1]]


def save_game(save_path):
    """
    Attempts to save game to file in save_path
    :param save_path: String containing path to save file
    :return: Bool, whether game was saved or not
    """

    return_value = True
    logger.info(f"Attempting to save game at {save_path}...")

    try:

        with open(save_path, 'wb') as save_file:

            pickle.dump([dungeon_map.game_map, player.position], save_file)
            logger.info("Successfully saved game!")

    except (OSError, IOError) as exc:

        return_value = False
        logger.info(f"Could not save game! Caught exception: {str(exc)}")

    return return_value


def load_game(load_path):
    """
    Attempts to load game from load_path
    :param load_path: Path to file containing saved game
    :return: Bool, whether file was loaded or not
    """

    return_value = True
    logger.info(f"Attempting to load game at {load_path}...")

    try:

        with open(load_path, 'rb') as load_file:

            save_data = pickle.load(load_file)

            if isinstance(save_data, list) and len(save_data) == 2:

                dungeon_map.game_map = save_data[0]
                player.position = save_data[1]
                logger.info("Successfully loaded game.")

            else:

                return_value = False
                logger.info("Loading failed! Unpickled invalid data.")

    except (OSError, IOError) as exc:

        return_value = False
        logger.info(f"Loading failed! Caught exception: {str(exc)}")

    return return_value
