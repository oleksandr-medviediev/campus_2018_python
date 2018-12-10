
class CustomException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class PlayerInputError(CustomException):
    def __init__(self, value):
        self.message = f"\nPlayer inputed: {value} " 
