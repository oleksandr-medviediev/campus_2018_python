class MyError(Exception):

    def __init__(self, message):
        
        super().__init__(self)
        self.message = message

    def __str__(self):
        return self.message


class LoadDataError(MyError):

    pass


class MapSizeError(MyError):

    pass

class CharacterNotFoundError(MyError):

    pass
