

class LoadGameError(Exception):

    def __init__(self, message = ''):

        self.message = f'Could not load the game {message}'


class SaveGameError(Exception):

    def __init__(self, message = ''):

            self.message = f'Could not save the game {message}'


class OutOfMapRangeError(IndexError):

    pass


class PlayerMoveError(Exception):

    pass
