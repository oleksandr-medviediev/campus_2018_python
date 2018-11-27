from random import choice
import dun_player as dp
import dungeon_logic
import dun_map


class Enemy(dp.Character):

    def __init__(self):

        dp.Character.__init__(self, 1)
        self.damage = 1
        self.position = [0, 0]

    def attack(self, character):
        """
        :param character: character that should be attacked
        :type character: dun_player.Character
        """

        character.hit_points -= self.damage

    @property
    def position(self):
        return self.__position
    
    @position.setter
    def position(self, position):
        self.__position = position
    
    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, damage):
        self.__damage = damage

    def process_move(self, dungeon_map):
        """
        :param dungeon_map: map of the game
        :type dungeon_map: DungeonMap
        """

        game_map = dungeon_map.dun_map
        size = len(game_map[0])
        command = choice(dp.COMMANDS)
        
        move_ret_val = dungeon_logic.make_move_if_possible(self.position, size, command)
