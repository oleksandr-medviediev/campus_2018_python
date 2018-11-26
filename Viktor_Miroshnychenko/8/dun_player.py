import dungeon_decorators
import dun_map


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
        while self.command not in MENU_COMMANDS and  self.command not in dun_map.COMMANDS:

            self.command = input('Enter valid command\n')


    @dungeon_decorators.debug_time_decor
    @dungeon_decorators.debug_decor
    def applay_damage(self, damage):
        """
        :param damage: damage to applay
        :type damage: int
        """

        self.hit_points -= damage


    @dungeon_decorators.debug_time_decor
    @dungeon_decorators.debug_decor
    def change_score(self, diff):
        """
        :param diff: score difference
        :type diff: int
        """

        self.treasure_picked += diff
    

