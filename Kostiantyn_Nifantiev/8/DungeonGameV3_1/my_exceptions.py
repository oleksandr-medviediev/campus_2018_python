
class MoveError(Exception):

    def __init__(self, message):
        
        self.message = " ".join(["Wrong move direction! " , message])


class MapCoordinatesError(Exception):

    def __init__(self, message, map_size, given_coordinate):

        self.message = " ".join(["Invalid map coordinates! ", message])


class MapSizeError(Exception):

    def __init__(self, message, given_width, given_height):

        self.message = message

        if not isinstance(given_width, int):

            self.given_width = "NaN"

        else:

            self.given_width = str(given_width)
    
        if not isinstance(given_height, int):

            self.given_height = "NaN"

        else:

            self.given_height = str(given_height)

    def __str__(self):

        return " ".join(["Invalid map size! Expected at least 5x5 size, \n", self.given_width, self.given_height, " has found instead", self.message])
