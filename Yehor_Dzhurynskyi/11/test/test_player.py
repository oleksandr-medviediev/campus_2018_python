import sys
import unittest

sys.path.append('..')

from player import Player
import dungeon_game_error


class PlayerTest(unittest.TestCase):

    def setUp(self):
        self.__player = Player(0, 0)

    def test_came_on_trap(self):

        old_hp = self.__player.health
        self.__player.on_location_changed('!')
        new_hp = self.__player.health

        self.assertTrue(old_hp - new_hp == 1)

    def test_came_on_treasure(self):

        old_bag = self.__player.bag
        self.__player.on_location_changed('$')
        new_bag = self.__player.bag

        self.assertTrue(new_bag - old_bag == 1)

    def test_death(self):

        self.__player.hit(100)
        self.assertTrue(self.__player.is_dead())

    def tearDown(self):
        del self.__player

if __name__ == '__main__':
    unittest.main()
