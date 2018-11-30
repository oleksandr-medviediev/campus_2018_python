import unittest
import logging
import sys

sys.path.insert(0, '..')

from game_map import BasicMap
from dungeon_logger import my_logger


class TestBasicMap(unittest.TestCase):


    def setUp(self):

        self.wrong_map_examples_file = open("fixtures\wrong_map_sizes.txt", "r")
        wrong_map_examples = self.wrong_map_examples_file.read()
        wrong_map_examples = wrong_map_examples.split(",")
        self.numeric_wrong_map_examples = [[int(token) for token in map_request.split(':')] for map_request in wrong_map_examples]

    def tearDown(self):

        self.wrong_map_examples_file.close()

    def test_init(self):

        test_basic_map = BasicMap()
        self.assertEqual(test_basic_map.map_size, [20, 10])
        self.assertEqual(test_basic_map.dungeon_map, [])


    def test_reset_map_size(self):

        test_basic_map = BasicMap()
        test_basic_map.map_size = [5, 5]

        test_basic_map.reset_map_size()
        self.assertEqual(test_basic_map.map_size, [20, 10])


    def test_set_valid_map_size(self):

        test_basic_map = BasicMap()

        result = test_basic_map.set_map_size(10, 10)
        self.assertTrue(result)


    def test_set_invalid_map_size(self):

        test_basic_map = BasicMap()

        for wrong_map_size in self.numeric_wrong_map_examples:

            result = test_basic_map.set_map_size(*wrong_map_size)
            self.assertFalse(result)


if __name__ == '__main__':

    unittest.main()

