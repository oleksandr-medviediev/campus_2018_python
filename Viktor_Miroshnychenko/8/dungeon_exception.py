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


class MapCageError(Exception):

    def __init__(self, map, position, message):
        """
        :param map: map of the game
        :type map: DungeonMap

        :param position: position on the map
        :type position: list[int, int]

        :param message: message
        :type message: str
        """

        self.message = 'MapCageError. Invalid data in cage: ' + str(position[0]) + ',' + str(position[1]) + message
        self.map = map

    def __str__(self):

        self.map.print_debug_map()
        return self.message
