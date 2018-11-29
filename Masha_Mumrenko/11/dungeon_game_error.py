class DungeonGameError(Exception):
    """
    Custom error class for game
    """
    def __init__(self,message):
        self.message = message


    def __str__(self):
        return self.message



class MapSizeValueError(DungeonGameError):
    """
    Custom error class that is responsible for map size value
    """
    def __init__(self, value):
        self.message = f"Map size is too big and equals {value}"


class CommandError(DungeonGameError):
    """
    Custom error class that is responsible for command input error
    """
    def __init__(self):
        self.message = f"Such command is not in the list"


class PlayerDeadError(DungeonGameError):
    """
    Custom error class that is responsible for referencing dead player error
    """
    def __init__(self):
        self.message = f"Play is dead"   
