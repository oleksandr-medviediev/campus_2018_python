import sys
import unittest

sys.path.append('..')
import game_map


class TestCoordinatesGenerator(unittest.TestCase):

    def setUp(self):

        self.map_size = [10, 10]
        self.map = game_map.GameMap(self.map_size, 0.3, 0.2)


    def test_generate_function(self):     

        coordinates = self.map.generate_coordinates()
        self.assertTrue(isinstance(coordinates, list))
        self.assertEqual(len(coordinates), 2)
        self.assertLess(coordinates[0], self.map_size[0])
        self.assertLess(coordinates[1], self.map_size[1])
        self.assertEqual(self.map.map_[coordinates[0]][coordinates[1]], 0)
         

if __name__ == '__main__':
    unittest.main()
