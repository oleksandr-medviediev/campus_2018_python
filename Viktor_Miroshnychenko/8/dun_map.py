from copy import deepcopy
import dungeon_map_generate
import dungeon_logic
import dungeon_decorators
import dungeon_logger
import dun_player
import dungeon_exception



COMMANDS = ['r', 'l', 'u', 'd']
WARNINGS = {'bomb':'Bomb is near you!',
            'treasue':'Tresure is near you'}


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

        player.position = dungeon_map_generate.set_player_randomly(self.dun_map)


    @dungeon_decorators.debug_time_decor
    @dungeon_decorators.debug_decor
    def process_move(self, player):
        """
        :param player: player that must make a move
        :type player: Player
        """

        position = player.position
        size = len(self.dun_map[0])
        command = player.command
        if command not in COMMANDS:
            raise dungeon_exception.CommandError('Invalid command was entered!')

        dungeon_logger.logger.debug(f"Move with command: {command}")
    
        try:
            self.dun_map[position[0]][position[1]] = '0'
        except TypeError as error:
            dungeon_logger.logger.info(f'TypeError occured: {error}')
        move_ret_val = dungeon_logic.make_move_if_possible(position, size, command)
        
        if move_ret_val == False:

            dungeon_logger.logger.info('Move is not possible')
            self.dun_map[position[0]][position[1]] = 'y'

            return
        
        cage_state = dungeon_logic.check_pos(self.dun_map, position)
        cages = dungeon_logic.check_closest_pos(self.dun_map, position, size)
        for cage in cages:
            dungeon_logger.logger.info(WARNINGS[cage])

        try:
            self.dun_map[position[0]][position[1]] = 'y'
        except IndexError as error:
            dungeon_logger.logger.info(f'Player on wrong position/n IndexError: {error}')

        if cage_state == 'bomb':
            
            try:
                player.applay_damage(1)
            except dungeon_exception.DamageError as error:
                dungeon_logger.logger.info(f'DamageError raised: {error}')
            dungeon_logger.logger.info('You picked the bomb')
        
        elif cage_state == 'treasue':
            player.change_score(1)
            dungeon_logger.logger.info('You picked the treasure')

        elif cage_state is not 'empty':
            raise dungeon_exception.MapCageError(self, position, cage_state)

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
