from . import dungeon_game_logger
from .character import Character


class Player(Character):

    def __init__(self, x, y):

        super().__init__()
        self.x = x
        self.y = y

    def input(self, level):
        """
        getting input from stdin
        """

        MOVES = {
            'left': (-1, 0),
            'right': (1, 0),
            'up': (0, -1),
            'down': (0, 1)
        }

        while True:

            move = input('Enter your move (`left`, `right`, `up`, `down` or `save`): ')

            if move == 'save':
                level.save()
            elif move not in MOVES:
                dungeon_game_logger.logger.warn('Wrong input! It should be one of this: `left`, `right`, `up`, `down`')
            else:
                break

        return MOVES[move]

    def on_location_changed(self, new_cell):
        """
        callback which called when character changing location
            :param str new_cell: new location which is current position for character
        """

        if new_cell == '!':
            self.hit(1)
        elif new_cell == '$':
            self._bag += 1

    def hit(self, damage):
        """
        decrease player's health
            :param int damage: magnitude of damage
        """

        self._health -= damage

    def is_dead(self):
        """
        checks if player is already dead
        """

        is_dead = self._health <= 0

        return is_dead

    def is_won(self):
        """
        checks if player is already won
        """

        won = self._bag >= 3

        return won
