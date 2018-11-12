import pickle


def save(data, filename):
    with open(filename, 'wb') as file:
        pickle.dump(data, file)


def load(filename):
    with open(filename, 'rb') as file:
        return pickle.load(file)
