import unittest

import constants
from player import Player

class TestEnemyBehaviour(unittest.TestCase):

    def setUp(self):
        self.map_size = constants.MIN_MAP_SIZE
        self.player = Player(0, 0)

    
    def tearDown(self):
        del self.player


    def test_get_coordinates(self):

        self.player.x = 5
        self.player.y = 4

        self.assertEqual((5, 4), self.player.get_coordinates(), 'Method get_coordinates return wrong result.')


    def test_move_to_up(self):
        
        self.player.x = 1
        self.player.y = 1

        self.player.move_to(constants.UP_INDEX)

        # using inversed values x & y
        self.assertEqual((0, 1), self.player.get_coordinates(), 'Player move up wrong.')


if __name__ == '__main__':
    unittest.main()
