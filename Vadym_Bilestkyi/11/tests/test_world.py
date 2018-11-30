import sys
import random
import unittest

sys.path.append('..')

import world
import player


class TestWorld(unittest.TestCase):

    def setUp(self):
        self.size = 10
        self.world = world.World(size=self.size)
        self.world.spawn_player(player.Player('test_player'))

    def tearDown(self):
        del self.size
        del self.world

    def test_is_inside_method(self):
        self.assertTrue(not self.world.is_inside([-1, 0]))
        self.assertTrue(self.world.is_inside([0, 0]))
        self.assertTrue(self.world.is_inside([self.size / 2, 0]))
        self.assertTrue(not self.world.is_inside([0, self.size]))

    def test_place_cell_method(self):
        self.world.place_cell(2, 2, 'Trap')
        self.assertEqual(self.world.get_cell(2, 2), 'Trap')

    def test_get_neighbor_cells_method(self):
        neighbor = set(map(tuple, self.world.get_neighbor_cells([5, 5])))
        self.assertEqual(neighbor, {
            (4, 6),
            (5, 6),
            (6, 6),
            (4, 5),
            (6, 5),
            (4, 4),
            (5, 4),
            (6, 4)
        })

    def test_is_trap_around_method(self):
        neighbor = self.world.get_neighbor_cells([5, 5])
        self.world.place_cell(*random.choice(neighbor), 'Trap')
        self.assertTrue(self.world.is_trap_around())


if __name__ == '__main__':
    unittest.main()
