import pickle
from os.path import exists

def save_to_file(obj):

    """ Function write obj to file using pickle

        Args:
            obj(picklable object): object need to save

        Returns:
            (none)

    """
    
    with open ('saved_game.txt', 'wb') as file:
        pickle.dump(obj, file)


def load_from_file():

    """ Function read obj from file using pickle

        Args:
            (none)

        Returns:
            (picklable object): object need to load

    """
    
    file = open ('saved_game.txt', 'rb')
    obj = pickle.load(file)

    file.close()

    return obj


def check_loading_file():

    """ Function checks if existing loading file.

        Args:
            (none)

        Returns:
            bool: return True if file exists, otherwise - return False

    """
    
    is_file_existing = exists('saved_game.txt')

    return is_file_existing
