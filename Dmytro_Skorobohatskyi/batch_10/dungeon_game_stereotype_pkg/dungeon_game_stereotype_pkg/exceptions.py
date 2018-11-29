class UserError(Exception):

    def __init__(self, message, value):
        self.message = message
        self.value = value


    def __str__(self):
        return self.message


class WrongMapSizeError(UserError):

    def __init__(self, minimum_size):
        super().__init__("Wrong map size.", minimum_size)


    def __str__(self):
        return self.message + " Minimum value is {}".format(self.value)


class WrongPlayerChoiceError(Exception):

    def __str__(self):
        return "Wrong command choice."
