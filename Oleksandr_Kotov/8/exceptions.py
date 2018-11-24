
class TerrainGenerationError(Exception):
    def __init__(self, scale):
        self.__scale = scale

    def __str__(self):

        string = "Terrain generaion exception raised."
        string.join(F" Trying to set scale to {self.__scale}.")

        return string


class GameCommandError(Exception):

    def __init__(self, command):
        self.__command = command

    def __str__(self):

        string = F"Unknown game command: {self.__command}"

        return string


class MenuCommandError(Exception):

    def __init__(self, command):
        self.__command = command

    def __str__(self):

        string = F"Unknown menu command: {self.__command}"

        return string
