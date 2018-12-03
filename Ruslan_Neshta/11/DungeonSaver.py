import json
import pickle
from os import path
from DungeonLogger import debugger_output
from DungeonLogger import main_logger

SAVE = 'DungeonGame'


@debugger_output()
def save_game(game, type='b'):
    """
    Saves game into a file

    :param game: dict of in game objects
    :param type: b for binary, j for json formats
    :return: nothing
    :rtype: None
    """

    if type == 'b':
        save_pickle(game)

    elif type == 'j':
        save_json(game)

    else:
        raise RuntimeError('invalid type "{}" got'.format(type))


@debugger_output()
def save_pickle(game):
    """
    Saves game into binary format

    :param game: dict of in game objects
    :return: nothing
    :rtype: None
    """

    with open(SAVE, 'wb') as save:
        pickle.dump(game, save, protocol=3)


@debugger_output()
def save_json(game):
    """
    Saves game into json format

    :param game: dict of in game objects
    :return: nothing
    :rtype: None
    """

    name = SAVE + '.json'

    with open(name, 'w') as save:
        json.dump(game, save)


@debugger_output()
def load_game():
    """
    Loads game from file

    :return: dict of in game objects
    :rtype: dict
    """

    game = {}
    try:
        if path.isfile(SAVE):
            main_logger.info('Can\'t find saved game')
        else:
            game = load_pickle()

    except IOError:
        main_logger.info('Can\'t read data from file')

    except OSError:
        main_logger.info('Can\'t open file')
        
    except MemoryError:
        main_logger.info('Can\'t load game: not enough memory available')

    return game


@debugger_output()
def load_pickle():
    """
    Loads game state from binary file

    :return: dict of in game objects
    :rtype: dict
    """
    
    with open(SAVE, 'rb') as save:
        result = pickle.load(save)

    return result


@debugger_output()
def load_json():
    """
    Loads game state from json file

    :return: dict of in game objects
    :rtype: dict
    """

    name = SAVE + '.json'

    with open(name, 'r') as save:
        game = json.load(save)

    return game


if __name__ == "__main__":
    a = [[1, 2, 3], [4, 5, 6]]
    save_game(a)
    r = load_game()
    print(r)
