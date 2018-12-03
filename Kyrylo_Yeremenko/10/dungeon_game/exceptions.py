"""
This module defines user exceptions for task 8.1 from Coding Campus 2018 Python course
(Dungeon Game)
"""


class MapInitError(Exception):

    def __init__(self, message):
        """
        Class constructor
        :param message: Exception message
        """
        Exception.__init__(self, message)


class InputError(Exception):

    def __init__(self, message):
        """
        Class constructor
        :param message: Exception message
        """
        Exception.__init__(self, message)


class InvalidDataLoadedError(Exception):

    def __init__(self, message):
        """
        Class constructor
        :param message: Exception message
        """
        Exception.__init__(self, message)
