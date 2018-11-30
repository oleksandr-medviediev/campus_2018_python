import unittest
import sys
import os
sys.path.insert(0, os.path.abspath('..'))

from game import DungeonGame

class GameEndTest(unittest.TestCase):


    def setUp(self):

        self.dungeonGame = DungeonGame()

    def testHealthGameEnd(self):

        self.dungeonGame.player.health = 0
        self.dungeonGame.player.bag = 0

        self.assertTrue(self.dungeonGame.is_game_ended())

    def testBagGameEnd(self):
        self.dungeonGame.player.health = DungeonGame.default_health
        self.dungeonGame.player.bag = DungeonGame.treasure_to_win

        self.assertTrue(self.dungeonGame.is_game_ended())

    def tearDown(self):

        print('Game end test ended.')


if __name__ == '__main__':
    unittest.main()
