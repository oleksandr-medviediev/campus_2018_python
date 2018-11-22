class MyError(Exception):

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.messsage


class LoadDataError(MyError):

    def __init__(self, message):
        super().__init__(message)


class MapSizeError(MyError):

    def __init__(self, message):
        super().__init__(message)

class PlayerNotFoundError(MyError):

    def __init__(self, message):
        super().__init__(message)
