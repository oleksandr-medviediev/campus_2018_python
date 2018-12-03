import unittest

sys.path.append('..')

from level import Level
import dungeon_game_error


class LevelTest(unittest.TestCase):

    def setUp(self):
        self.__level = Level.generate(8)

    def test_cell_at_out_of_bounds(self):
        with self.assertRaises(dungeon_game_error.CellOutOfBoundsDungeonGameError):
            self.__level.cell_at(50, 50)

    def test_cell_correctness(self):

        filter_func = lambda cell: cell != '_' and cell != '$' and cell != '!'
        unrecognized_cells = list(filter(filter_func, self.__level.level_data))
        self.assertTrue(len(unrecognized_cells) == 0, "Unrecognized cell symbol")

    def test_random_inner_point(self):

        randomed_x, randomed_y = self.__level.random_inner_point()
        self.assertTrue(randomed_x < self.__level.size and randomed_y < self.__level.size)

    def tearDown(self):
        del self.__level


if __name__ == '__main__':
    unittest.main()
