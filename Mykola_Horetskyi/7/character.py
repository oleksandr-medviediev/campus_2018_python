from decorator import debug_decorator


class Character:


    def __init__(self):
        """
        Constructor of character class.
        """
        self.name = ""
        self.position = Position(0,0)

    @debug_decorator
    def initialize(self, name, position):
        """
        Initializes character class.
        """
        self.name = name
        self.position = position
