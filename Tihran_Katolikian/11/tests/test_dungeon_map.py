import unittest
from sys import path


path.append('..')


from DungeonMap import DungeonMap, DungeonCell


class TestDungeonMap(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        '''
        Inits all data required for tests
        '''
        cls.__map_size = 10
        cls.__map = DungeonMap()


    def test_create_new_map(self):
        '''
        Tests if dungeon map is created correctly.
        '''
        self.__map.generate_new_map(self.__map_size)
        self.assertIsNotNone(self.__map.dungeon_map)


    def test_map_size(self):
        '''
        Tests if map size is as we expect it to be.
        '''
        cells_count = 0
        for row in self.__map.dungeon_map:
            cells_count += len(row)

        self.assertEqual(cells_count, self.__map_size ** 2)


    def test_traps_count(self):
        '''
        Tests a number of traps.
        '''
        traps = 0
        is_trap = lambda x: x is DungeonCell.TRAP
        for row in self.__map.dungeon_map:
            traps += sum(1 for cell in row if is_trap(cell))

        trap_quota = 0.1
        self.assertEqual(self.__map_size ** 2 * trap_quota, traps)


if __name__ == '__main__':
    unittest.main()
