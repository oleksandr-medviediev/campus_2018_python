from my_decorator import log_wrapper, debug_wrapper
from my_character import Character


class Player(Character):

    @log_wrapper
    @debug_wrapper
    def __init__(self):
        """
        Player class constructor
        """

        super().__init__()
        self.name = ''
        self.position = ()


    @log_wrapper
    @debug_wrapper
    def initialize(self, hp, name, position):
        """
        Initializes player's attributes

        :param int hp:
        :param str name:
        :param tuple position:
        """

        super().initialize(hp)
        self.name = name
        self.position = position

        return None
