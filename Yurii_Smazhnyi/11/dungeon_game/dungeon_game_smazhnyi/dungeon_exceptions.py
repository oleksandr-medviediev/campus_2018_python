class MapGeneratorError(Exception):
    def __init__(self, msg):
        """
        :param msg: exception message.
        :msg type: str.
        """

        self.msg = msg


class IncorrectCommandError(Exception):
    def __init__(self, msg):
        """
        :param msg: exception message.
        :msg type: str.
        """

        self.msg = msg


class PlayerHPErorr(Exception):
    def __init__(self, msg):
        """
        :param msg: exception message.
        :msg type: str.
        """

        self.msg = msg
