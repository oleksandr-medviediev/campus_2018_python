class Character:
    
    def __init__(self):
        self.hp = 3
        self.bag = 0


    @property
    def hp(self):
        return self.__hp


    @hp.setter
    def hp(self, value):
        self.__hp = value


    @property
    def bag(self):
        return self.__bag


    @bag.setter
    def bag(self, value):
        self.__bag = value

        
    def is_alive(self):
        """ Function check if player can continue game.

            Returns: (bool): return True if hp > 0, otherwise - return False
        """

        return self.hp > 0

    def is_winner(self):
        """ Function check if player won the game.

            Returns: (bool): return True if bag == 3, otherwise - return False
        """

        return self.bag == 3

    def increase_treasure_amount(self):
        """ Function increase self.bag by 1 point. """

        self.bag += 1

    def get_trapped(self):
        """ Function decrease self.hp by 1 point. """
        self.hp -= 1
