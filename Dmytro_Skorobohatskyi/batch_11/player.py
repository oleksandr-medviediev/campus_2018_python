from character import Character
from utilities import Utilities
from decorators import DebugDecorator, InfoDecorator
from logging_system import logger


class Player(Character):

    def __init__(self, x, y):
        super().__init__()

        self.x = x
        self.y = y


    def __str__(self):
        
        return "Player" 

    
    @DebugDecorator()
    def get_coordinates(self):

        """ Function return player's coordinates.

            Return: 
                (int, int): specified coordinates.
        """

        x, y = self.x, self.y

        return x, y


    @DebugDecorator()
    def move_to(self, direction_index):

        """ Function shifts player in specified direction

            Args:
                direction_index(int): index presenting direction

            Returns:
                (none)
        """
        
        shift_x, shift_y = Utilities.get_shift_by_direction(direction_index)

        self.x += shift_x
        self.y += shift_y
