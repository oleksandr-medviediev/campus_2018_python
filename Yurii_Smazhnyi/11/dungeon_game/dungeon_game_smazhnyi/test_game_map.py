import unittest
from game_map import GameMap

class TestGameMap(unittest.TestCase):

    def setUp(self):
        self.map = GameMap(10)


    def tearDown(self):
        self.map = None


if __name__ == '__main__':
    unittest.main()