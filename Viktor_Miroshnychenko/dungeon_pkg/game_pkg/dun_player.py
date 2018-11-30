import dungeon_decorators
import dungeon_logic
import dungeon_exception
import dungeon_logger
import dun_map
import dungeon_exception as dexc


COMMANDS = ['r', 'l', 'u', 'd']
WARNINGS = {'bomb':'Bomb is near you!',
            'treasue':'Tresure is near you'}
MENU_COMMANDS = ['save', 'load']


class Character:

    def __init__(self, hit_points):
        """
        :
        """

        self.hit_points = hit_points
        self.position = [0, 0]


class Player(Character):

    def __init__(self):
        """
        :param dun_map: map where player must be created
        
        """
        
        Character.__init__(self, 3)
        self.command = ""
        self.treasure_picked = 0


    @dungeon_decorators.debug_time_decor
    @dungeon_decorators.debug_decor
    def get_command(self):

        self.command = ""
        while self.command not in MENU_COMMANDS and  self.command not in COMMANDS:

            self.command = input('Enter valid command\n')


    @dungeon_decorators.debug_time_decor
    @dungeon_decorators.debug_decor
    def applay_damage(self, damage):
        """
        :param damage: damage to applay
        :type damage: int
        """

        if damage < 0:
            raise dexc.DamageError(f'{damage}')
        self.hit_points -= damage


    @dungeon_decorators.debug_time_decor
    @dungeon_decorators.debug_decor
    def change_score(self, diff):
        """
        :param diff: score difference
        :type diff: int
        """

        self.treasure_picked += diff
    
    @dungeon_decorators.debug_time_decor
    @dungeon_decorators.debug_decor
    def process_move(self, dung_map):
        """
        :param dung_map: map of the game
        :type dung_map: DungeonMap
        """

        position = self.position
        size = len(dung_map.dun_map)
        command = self.command
        game_map = dung_map.dun_map

        if command not in COMMANDS:
            raise dungeon_exception.CommandError('Invalid command was entered!')

        dungeon_logger.logger.debug(f"Move with command: {command}")
    
        try:
            game_map[position[0]][position[1]] = '0'
        except TypeError as error:
            dungeon_logger.logger.info(f'TypeError occured: {error}')
        move_ret_val = dungeon_logic.make_move_if_possible(position, size, command)
        
        if move_ret_val == False:

            dungeon_logger.logger.info('Move is not possible')
            game_map[position[0]][position[1]] = 'y'

            return
        
        cage_state = dungeon_logic.check_pos(game_map, position)
        cages = dungeon_logic.check_closest_pos(game_map, position, size)
        for cage in cages:
            dungeon_logger.logger.info(WARNINGS[cage])

        try:
            game_map[position[0]][position[1]] = 'y'
        except IndexError as error:
            dungeon_logger.logger.info(f'Player on wrong position/n IndexError: {error}')

        if cage_state == 'bomb':
            
            try:
                self.applay_damage(1)
            except dungeon_exception.DamageError as error:
                dungeon_logger.logger.info(f'DamageError raised: {error}')
            dungeon_logger.logger.info('You picked the bomb')
        
        elif cage_state == 'treasue':
            self.change_score(1)
            dungeon_logger.logger.info('You picked the treasure')

        elif cage_state is not 'empty':
            raise dungeon_exception.MapCageError(game_map, position, cage_state)

