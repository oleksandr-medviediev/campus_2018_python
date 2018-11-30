import unittest
import sys
import os
sys.path.insert(0, os.path.abspath('..'))

from utils import Position
from game import DungeonGame
from dungeon_map import DungeonMap

class EnemyRespawnCheck(unittest.TestCase):


    def setUp(self):

        self.dungeonGame = DungeonGame()
        #initializing map with 2 cells
        DungeonGame.dmap.initialize(2,1,0,[],Position(0,0))

        #setting enemy and player position to be the same
        DungeonGame.player.position = Position(0,0);
        DungeonGame.enemy.position = Position(0,0);


    def testEncounter(self):

        self.dungeonGame.respawn_enemy()

        #check that enemy position is not the same after respawn
        self.assertNotEqual(DungeonGame.player.position,\
         DungeonGame.enemy.position)


    def tearDown(self):

        print('Enemy respawn test ended.')


if __name__ == '__main__':
    unittest.main()
