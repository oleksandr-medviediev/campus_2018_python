class CommandError(Exception):

    def __init__(self, message):

        self.message = message

    def __str__(self):

        return self.message


class DamageError(Exception):

    def __init__(self, message):

        self.message = 'Negative damage was applied: ' + message

    def __str__(self):

        return self.message 