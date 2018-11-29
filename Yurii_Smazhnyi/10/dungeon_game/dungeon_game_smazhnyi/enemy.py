import random
from vector2 import Vector2
import decorators
from dungeon_input import DungeonInput
from game_map import GameMap
import custom_log
from dungeon_exceptions import PlayerHPErorr


class Enemy:
    """
    In-game player.
    """

    def __init__(self):
        """
        :param name: player's name
        :name type: string
        :param start_hp: initial hp
        :start_hp type: int
        """

        self.position = Vector2()
        self.cell_stepped_on = GameMap.GROUND_SYMBOL

    @decorators.info_decorator
    @decorators.debug_decorator
    def move(self, game_map):
        """
        Move enemy in random direction on given map

        :param game_map: item to be applied
        :game_map type: list of strings
        :returns: None.
        :rtype: None.
        """

        self.position = game_map.get_enemy_pos()

        valid_directions = game_map.get_enemy_valid_directions()

        old_cell_stepped_on = self.cell_stepped_on

        self.cell_stepped_on = game_map.move_enemy(random.choice(valid_directions))

        stepped_on_player = False

        if self.cell_stepped_on == GameMap.PLAYER_SYMBOL:

            game_map.spawn_enemy()
            self.cell_stepped_on = GameMap.GROUND_SYMBOL
            stepped_on_player = True

        game_map.replace_character(self.position, old_cell_stepped_on)

        return stepped_on_player


