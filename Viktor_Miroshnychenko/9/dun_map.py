from copy import deepcopy
import dungeon_map_generate
import dungeon_logic
import dungeon_decorators
import dungeon_logger
import dun_player
import dungeon_exception


class DungeonMap:

    def __init__(self, size):
        """
        :param size: size of  the square map
        :type size: int
        """
        
        self.dun_map = dungeon_map_generate.generate_map(size)


    @dungeon_decorators.debug_time_decor
    @dungeon_decorators.debug_decor
    def set_player_on_map(self, player):
        """
        :param player: player that must be set on the map
        :type player: Player
        """

        player.position = dungeon_map_generate.set_character_randomly(self.dun_map)

    @dungeon_decorators.debug_time_decor
    @dungeon_decorators.debug_decor
    def print_debug_map(self):
        """
        :description: print map to info stream
        """

        for row in self.dun_map:

            dungeon_logger.logger.info(f'{row}')

    @dungeon_decorators.debug_time_decor
    @dungeon_decorators.debug_decor
    def print_map(self):
        """
        :description: print map withoud bombs and tresures
        """

        dun_map = deepcopy(self.dun_map)
        for row in dun_map:

            for it in range(len(row)):

                if row[it] != '0' and row[it] != 'y':
                    row[it] = ' '

            dungeon_logger.logger.info(f'{row}')
