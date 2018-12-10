from DungeonMap import DungeonMap, Empty
import unittest as utest
from exceptions import AlreadyDeadError
from utils import repeat


class TestDungeonMap(utest.TestCase):
    RAND_RUNS = 20


    def setUp(self):
        self.dmap = DungeonMap(10)


    def test_get_rand_empty_tile_returns_in_bounds_tile(self):
        def bounds_check():
            self.assertTrue(self.dmap.in_bounds(self.dmap.get_random_empty_tile()))
        repeat(bounds_check, self.RAND_RUNS)

    
    def test_get_rand_empty_tile_returns_empty(self):
        def returns_empty():
            self.assertEqual(self.dmap.get_random_empty_tile(), Empty)
