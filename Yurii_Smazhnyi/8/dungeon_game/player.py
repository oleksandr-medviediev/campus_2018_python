from vector2 import Vector2
import decorators
from dungeon_input import DungeonInput
from game_map import GameMap
import custom_log
from dungeon_exceptions import PlayerHPErorr

class Player:
    """
    In-game player.
    """

    def __init__(self, name, start_hp):
        """
        :param name: player's name
        :name type: string
        :param start_hp: initial hp
        :start_hp type: int
        """

        try:
            if(start_hp <= 0):
                raise PlayerHPErorr
            self.hp = start_hp
        except PlayerHPErorr:
            custom_log.logger.warning("Start HP of player cannot be set zero or below!")
            self.hp = 1

        self.name = name
        self.bag = 0
        self.position = Vector2()

        self.is_trap_near_player = False
        self.is_treasure_near_player = False


    @decorators.info_decorator
    @decorators.debug_decorator
    def check_status(self, game_map):
        """
        Checks is traps or treasures are near player
        and save result to player.

        :returns: None.
        :rtype: None.
        """

        self.is_treasure_near_player = game_map.is_item_near_player(GameMap.TREASURE_SYMBOL)
        self.is_trap_near_player = game_map.is_item_near_player(GameMap.TRAP_SYMBOL)


    @decorators.info_decorator
    @decorators.debug_decorator
    def print_status(self):
        """
        Prints current player's status

        :returns: None.
        :rtype: None.
        """

        custom_log.logger.info(f"Traps Near You - {self.is_trap_near_player}")
        custom_log.logger.info(f"Treasure Near You - {self.is_treasure_near_player}")
        custom_log.logger.info(f"Your HP - {self.hp}")
        custom_log.logger.info(f"Treasure found - {self.bag}")


    @decorators.info_decorator
    @decorators.debug_decorator
    def apply_item(self, item):
        """
        Applies item on player

        :param item: item to be applied
        :item type: string
        :returns: None.
        :rtype: None.
        """

        if item == GameMap.TREASURE_SYMBOL:
            custom_log.logger.info(f"You've collected the Treasure!!!")

            self.bag += 1

        elif item == GameMap.TRAP_SYMBOL:
            custom_log.logger.info(f"You've stepped on the Trap!!!")
            self.hp -= 1


    @decorators.info_decorator
    @decorators.debug_decorator
    def move(self, game_map, direction):
        """
        Move player in given direction on given map

        :param game_map: item to be applied
        :game_map type: list of strings
        :param direction: direction to move
        :direction type: string
        :returns: None.
        :rtype: None.
        """

        self.apply_item(game_map.move_player(direction))