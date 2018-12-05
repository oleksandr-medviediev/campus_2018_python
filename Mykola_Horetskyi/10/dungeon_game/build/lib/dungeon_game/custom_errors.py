class Error(Exception):
    """
    Base class for custom errors.
    """

    def __init__(self, message):
        """
        Constructor of Error class.

        param: message explanation of the error
        """
        self.message = message


class DungeonMapInitializationError(Error):
    """
    Exception raised when Initialize for DungeonMap is called
    with wrong parameters
    """

    def __init__(self, message):
        """
        Constructor of MapInitializationError class.

        param: message explanation of the error
        """
        super().__init__(message)

class DungeonMapCellOutOfBoundsError(Error):
    """
    Exeption raised when attempting to access cell outside of DungeonMap boundaries.
    """

    def __init__(self, message, position):
        """
        Constructor of DungeonMapCellOutOfBoundsError class.
        param: message explanation of the error
        param: positionof the unaccessible cell
        """
        super().__init__(message)
        self.position = position



    def __str__(self):
        """
        Returns error description.
        """
        return "{}\nCell coordinates {},{} is out of dungeon map bounds"\
        .format(self.message, self.position.x, self.position.y)


class NotValidSaveFileError(Error):
    """
    Exeption raised when loading not valid save file.
    """

    def __init__(self, message, filename):
        """
        Constructor of MapInitializationError class.

        param: message explanation of the error
        """
        super().__init__(message)
        self.filename = filename

    def __str__(self):
        """
        Returns error description.
        """
        return "{}\nSave file {} is not valid."\
        .format(self.message, self.filename)
