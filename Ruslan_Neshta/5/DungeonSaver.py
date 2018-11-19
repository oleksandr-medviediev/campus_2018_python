import json
import pickle
from DungeonLogger import main_logger


SAVE = 'DungeonGame'


def save_game(game, type='b'):
    """
    Saves game into a file

    :param game: dict of in game objects
    :param type: b for binary, j for json formats
    :return: nothing
    :rtype: None
    """

    main_logger.debug(f'started {game}, {type}')
    if type == 'b':
        save_pickle(game)

    elif type == 'j':
        save_json(game)

    else:
        raise RuntimeError(f'invalid type "{type}" got')

    main_logger.debug(f'ended')


def save_pickle(game):
    """
    Saves game into binary format

    :param game: dict of in game objects
    :return: nothing
    :rtype: None
    """

    main_logger.debug(f'started')

    with open(SAVE, 'wb') as save:
        pickle.dump(game, save, protocol=3)

    main_logger.debug(f'ended')


def save_json(game):
    """
    Saves game into json format

    :param game: dict of in game objects
    :return: nothing
    :rtype: None
    """

    main_logger.debug(f'started {game}')
    name = SAVE + '.json'

    with open(name, 'w') as save:
        json.dump(game, save)

    main_logger.debug(f'ended')


def load_game():
    """
    Loads game from file

    :return: dict of in game objects
    :rtype: dict
    """

    main_logger.debug(f'started')
    try:
        game = load_pickle()

    except FileNotFoundError:
        game = load_json()

    main_logger.debug(f'ended')
    return game


def load_pickle():
    """
    Loads game state from binary file

    :return: dict of in game objects
    :rtype: dict
    """

    main_logger.debug(f'started')

    with open(SAVE, 'rb') as save:
        result = pickle.load(save)

    main_logger.debug(f'ended {result}')
    return result


def load_json():
    """
    Loads game state from json file

    :return: dict of in game objects
    :rtype: dict
    """

    main_logger.debug(f'started')
    name = SAVE + '.json'

    with open(name, 'r') as save:
        game = json.load(save)

    main_logger.debug(f'ended {game}')
    return game


if __name__ == "__main__":
    a = [[1,2,3], [4,5,6]]
    save_game(a)
    r = load_game()
    print(r)
