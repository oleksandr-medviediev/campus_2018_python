class Character:
    """
    class which represents moveable entity
    """

    def __init__(self):

        self._health = 3
        self._bag = 0


    def input(self):
        """
        getting input from stdin
        """
        raise NotImplementedError


    def on_location_changed(self, new_cell):
        """
        callback which called when character changing location
            :param str new_cell: new location which is current position for character
        """
        raise NotImplementedError


    def is_dead(self):
        """
        checks if player is already dead
        """
        raise NotImplementedError


    def is_won(self):
        """
        checks if player is already won
        """
        raise NotImplementedError


    @property
    def health(self):
        """
        number of health
            :param self: 
        """
        return self._health


    @property
    def bag(self):
        """
        number of bags
        """
        return self._bag