import unittest
import sys

sys.path.append('..')

from game_map import Map
from game_map import Position


class TestMap(unittest.TestCase):
    def test_init(self):
        size = 100
        treasures = 10
        traps = 11
        mgame_map = Map(Position(size, size), treasures, traps)

        mmap = mgame_map.game_map
        treasuresCount = 0
        trapsCount = 0
        for line in mmap:
            treasuresCount += line.count("!")
            trapsCount += line.count("x")

        self.assertEqual(treasuresCount, treasures)
        self.assertEqual(traps, trapsCount)

if __name__ == '__main__':
    unittest.main()
