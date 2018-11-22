from my_decorator import log_wrapper, debug_wrapper


class Character:

    @log_wrapper
    @debug_wrapper
    def __init__(self):
        """
        Character class constructor
        """

        self.hp = 0
        self.bag = 0


    @log_wrapper
    @debug_wrapper
    def initialize(self, hp):
        """
        Initializes character's attributes

        :param int hp: 'hp' is a traps amount minus 1
        """

        self.hp = hp - 1
        

    @log_wrapper
    @debug_wrapper
    def add_treasure(self):
        """
        Adds 1 treasure to the 'bag' attribute
        """

        self.bag += 1


    @log_wrapper
    @debug_wrapper
    def resolve_trap_effect(self):
        """
        Subtracts 1 from 'hp' attribute 
        """

        self.hp -= 1
