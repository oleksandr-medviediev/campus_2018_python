
import unittest
from dungeon_map import DungeonMap


class TestDungeonMap(unittest.TestCase):

    def setUp(self):

        self.map_size = 10
        self.dungeon_map = DungeonMap(self.map_size)

    def test_generate(self):

        # Map is generated in SetUp
        self.assertTrue(len(self.dungeon_map.game_map) == self.map_size)

        trap_count = 0
        treasure_count = 0

        for row in self.dungeon_map.game_map:

            self.assertTrue(len(row) == self.map_size)

            for tile in row:

                if tile == DungeonMap.SYMBOL_TREASURE:
                    treasure_count += 1
                elif tile == DungeonMap.SYMBOL_TRAP:
                    trap_count += 1

        self.assertTrue(trap_count == int((self.map_size ** 2) / DungeonMap.RATIO_TRAPS))
        self.assertTrue(treasure_count == int((self.map_size ** 2) / DungeonMap.RATIO_TREASURE))

    def tearDown(self):
        self.dungeon_map.game_map.clear()


if __name__ == "__main__":
    unittest.main()
