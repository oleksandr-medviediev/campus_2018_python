import unittest

import sys
sys.path.append("..")

from game_map import GameMap

class TestGameMap(unittest.TestCase):

    def setUp(self):
        self.map = GameMap(10)


    def tearDown(self):
        self.map = None


    def test_get_player_valid_directions(self):
        valid_directions = self.map.get_player_valid_directions()
        self.assertNotEqual(len(valid_directions), 0, "Player should always have valid direction!")

    def test_get_player_pos(self):
        position = self.map.get_player_pos()
        self.assertNotEqual(position.x, -1, "Player position is not correct!")
        self.assertNotEqual(position.y, -1, "Player position is not correct!")

    def test_get_enemy_pos(self):
        position = self.map.get_enemy_pos()
        self.assertNotEqual(position.x, -1, "Enemy position is not correct!")
        self.assertNotEqual(position.y, -1, "Enemy position is not correct!")

if __name__ == '__main__':
    unittest.main()