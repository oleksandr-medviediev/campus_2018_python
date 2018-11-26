import pickle
import logging

import log
from exceptions import InvalidDataLoadedError, InputError
from decorators import log_decorator, debug_log_decorator


logger = logging.getLogger(log.LOGGER_NAME)


@log_decorator
@debug_log_decorator
def get_input(input_validator, input_message):
    """
    Gets input from user satisfying given predicate
    :param input_validator: Validates user input, raises InputError containing message
    :param input_message: Message to display user
    :return: Accepted string
    """

    return_string = ""
    while True:

        string = input(input_message)

        try:

            input_validator(string)

        except InputError as exc:

            print(str(exc))

        else:

            return_string = string
            break

    return return_string


def vector_sum(lhs, rhs):
    """
    Calculates sum of XY vector
    :param lhs: Tuple/List containing X and Y coordinates as index 0 and 1
    :param rhs: Tuple/List containing X and Y coordinates as index 0 and 1
    :return: List containing X and Y sum
    """
    return [lhs[0] + rhs[0], lhs[1] + rhs[1]]


@log_decorator
@debug_log_decorator
def save_game(save_path, active_map, active_player):
    """
    Attempts to save game to file in save_path
    :param save_path: String containing path to save file
    :param active_map: DungeonMap instance
    :param active_player: Player instance
    :return: Bool, whether game was saved or not
    """

    return_value = True
    logger.info(f"Attempting to save game at {save_path}...")

    try:

        with open(save_path, 'wb') as save_file:

            pickle.dump([
                active_map.game_map,
                active_player.position,
                active_player.hitpoints,
                active_player.bag],
                save_file)

            logger.info("Successfully saved game!")

    except pickle.PicklingError:

        return_value = False
        logger.info("Could not save game! Couldn't pickle save data.")

    except (OSError, IOError) as exc:

        return_value = False
        logger.info(f"Could not save game! Caught exception: {str(exc)}")

    return return_value


@log_decorator
@debug_log_decorator
def load_game(load_path, active_map, active_player):
    """
    Attempts to load game from load_path
    :param load_path: Path to file containing saved game
    :param active_map: DungeonMap instance
    :param active_player: Player instance
    :return: Bool, whether file was loaded or not
    """

    return_value = True
    logger.info(f"Attempting to load game at {load_path}...")

    try:

        with open(load_path, 'rb') as load_file:

            save_data = pickle.load(load_file)

            if isinstance(save_data, list) and len(save_data) == 4:

                if isinstance(save_data[0], list):
                    active_map.game_map = save_data[0]

                else:
                    raise InvalidDataLoadedError("Invalid game map format")

                if active_map.is_index_valid(save_data[1]) and save_data[2] > 0 and save_data[2] >= 0:

                    active_player.position = save_data[1]
                    active_player.hitpoints = save_data[2]
                    active_player.bag = save_data[3]
                    logger.info("Successfully loaded game.")

                else:
                    raise InvalidDataLoadedError("Invalid player data")

            else:
                raise InvalidDataLoadedError("Unpickled data has invalid format")

    except (MemoryError, pickle.UnpicklingError) as exc:

        return_value = False
        logger.info(f"Loading failed! File structure invalid, received {str(exc)}")

    except InvalidDataLoadedError as exc:

        return_value = False
        logger.info(f"Loading failed! Data error: {str(exc)}")

    except (OSError, IOError) as exc:

        return_value = False
        logger.info(f"Loading failed! Caught exception: {str(exc)}")

    return return_value
