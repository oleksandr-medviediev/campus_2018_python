import pickle
from dungeon_logging import with_logging


@with_logging
def save(data, filename):
    with open(filename, 'wb') as file:
        pickle.dump(data, file)


@with_logging
def load(filename):
    with open(filename, 'rb') as file:
        return pickle.load(file)
