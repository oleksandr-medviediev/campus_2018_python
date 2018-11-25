import logging
from random import choice
from player import Player, PLAYER_MOVES
import dungeon_game_decorators


class Enemy(Player):
    """
    Enemy class.
    """
    def __init__(self):
        """
        Enemy constructor.
        """
        super().__init__('enemy')

    @dungeon_game_decorators.log_decor
    @dungeon_game_decorators.debug_decor
    def random_move(self, map_size):
        """
        Move to random direction.

        :param map_size: size of the game map.
        :type map_size: int.
        """
        move = choice(list(PLAYER_MOVES.keys()))

        new_position = self.calculate_new_position(move)
        new_x, new_y = new_position

        if 0 <= new_x < map_size and 0 <= new_y < map_size:
            self.set_position(*new_position)

        logging.info(f'Enemy moved {new_position}')
