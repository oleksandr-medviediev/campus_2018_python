import sys
import unittest

sys.path.append('..')
import game_map
import player


class TestPlayer(unittest.TestCase):

    def setUp(self):
        
        self.map_size = [10, 10]
        self.map = game_map.GameMap(self.map_size, 0.3, 0.2)
        self.player = player.Player(self.map)


    def test_player_lost(self):     
        self.player.hp = 0
        self.assertTrue(self.player.is_lost())
         
    def test_player_won(self):     
        self.player.treasure = 3
        self.assertTrue(self.player.is_won())

if __name__ == '__main__':
    unittest.main()
