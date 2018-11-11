import pickle

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
