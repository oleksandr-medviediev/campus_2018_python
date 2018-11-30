import unittest
from game_map import GameMap


class GameMapTest(unittest.TestCase):
    
    game_map = GameMap()
    game_map.mapsize = 9    
  
    def test_generate_cells(self):
        
        cells = self.game_map.generate_cells(12)   
        respond = self.game_map.mapsize * self.game_map.mapsize // 12
          
        self.assertEqual(respond, len(cells))

if __name__ == '__main__':
    unittest.main()
          