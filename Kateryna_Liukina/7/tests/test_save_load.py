import sys
import unittest

sys.path.append('..')
import Dungeon_Game
import game_map
import player

class TestSaveLoadGame(unittest.TestCase):

    def setUp(self):
        
        self.map_size = [10, 10]
        self.map = game_map.GameMap(self.map_size, 0.3, 0.2)
        self.player = player.Player(self.map)


    def test_save_load(self):     
        Dungeon_Game.save(self.map, self.player)

        map_, player_ = Dungeon_Game.load()


        for i in range(self.map_size[0]):
            for j in range(self.map_size[1]):
                self.assertEqual(map_.map_[i][j], self.map.map_[i][j])
        
        self.assertEqual(player_.position[0], self.player.position[0])
        self.assertEqual(player_.position[1], self.player.position[1])
    

if __name__ == '__main__':
    unittest.main()
