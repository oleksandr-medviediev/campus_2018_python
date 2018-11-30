import unittest
import sys

sys.path.append('..')

import terrain


class TestTerrain(unittest.TestCase):

    def setUp(self):
        self.__terrain = terrain.Terrain(1)

    def test_generation(self):

        self.assertIn(
            "s",
            str(self.__terrain), 
            "start position generation failure")

    def test_exception(self):
        with self.assertRaises(IndexError):
            self.__terrain.get_square(2, 2)

if __name__ == "__main__":
    unittest.main()
