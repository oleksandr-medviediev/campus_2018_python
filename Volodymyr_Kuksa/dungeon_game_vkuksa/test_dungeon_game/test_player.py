import unittest
import sys

sys.path.append('..')
from dungeon_game_vkuksa.player import Player


class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = Player('name')
        self.player.set_position(5, 5)

    def tearDown(self):
        del self.player

    def test_1(self):
        position = self.player.get_position()
        self.assertEqual(position, (5, 5), 'get_position fail')

    def test_2(self):
        position = self.player.calculate_new_position('u')
        self.assertEqual(position, (5, 4), 'calculate_new_position fail')
        self.assertEqual(self.player.get_position(), (5, 5), 'player moved on calculate_new_position')

    def test_3(self):
        position = self.player.calculate_new_position('d')
        self.assertEqual(position, (5, 6), 'calculate_new_position fail')
        self.assertEqual(self.player.get_position(), (5, 5), 'player moved on calculate_new_position')

    def test_4(self):
        position = self.player.calculate_new_position('r')
        self.assertEqual(position, (6, 5), 'calculate_new_position fail')
        self.assertEqual(self.player.get_position(), (5, 5), 'player moved on calculate_new_position')

    def test_5(self):
        position = self.player.calculate_new_position('l')
        self.assertEqual(position, (4, 5), 'calculate_new_position fail')
        self.assertEqual(self.player.get_position(), (5, 5), 'player moved on calculate_new_position')


if __name__ == '__main__':
    unittest.main()
