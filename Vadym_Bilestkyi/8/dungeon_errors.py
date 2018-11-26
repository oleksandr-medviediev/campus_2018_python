class OutOfMapError(Exception):
    """ Raised when player tries to move outside the map """


class InvalidMapSizeError(Exception):
    """ Raised when attempting to create a map with invalid size """


class NoSavedGamesError(Exception):
    def __init__(self):
        super().__init__('No saved games.')
