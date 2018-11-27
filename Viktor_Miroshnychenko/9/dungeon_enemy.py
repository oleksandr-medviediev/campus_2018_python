import dun_player as dp


class Enemy(dp.Character):

    def __init__(self):

        dp.Character.__init__(self, 1)
        self.damage = 1

    def attack(self, character):
        """
        :param character: character that should be attacked
        :type character: dun_player.Character
        """

        character.hit_points -= self.damage
    
    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, damage):
        self.__damage = damage
