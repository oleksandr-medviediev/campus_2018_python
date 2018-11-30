class InvalidDirectionException(Exception):
    def __init__(self, position, direction):
        self.position = position
        self.direction = direction
        self.message = "Player in position {0}, {1} cannot move in " + self.direction + " direction".format(self.position[0], self.position[1])


    def __str__(self):
        return(self.message)


class InvalidPositionException(Exception):
    def __init__(self, position):
        self.position = position


    def __str__(self):
        return("PLayer move out of map! Current position is {0}, {1}".format(self.position[o], self.position[1]))


class MapException(Exception):
    def __init__(self, message):
        self.message = message


    def __str__(self):
        return self.message 
