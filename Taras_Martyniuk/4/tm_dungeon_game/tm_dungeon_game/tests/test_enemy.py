from Enemy import Enemy
from DungeonMap import DungeonMap
import unittest as utest
from utils import tuple_diff, repeat

class TestEnemy(utest.TestCase):
    RUNS = 10


    def setUp(self):
        self.dmap = DungeonMap(10)
        self.enemy = Enemy(self.dmap)


    def test_move_randomly_moves_one_tile_only(self):
        def single_run():
            start_pos = self.enemy.position
            self.enemy.move_randomly()
            diff = tuple_diff(self.enemy.position, start_pos)

            valid_diffs = { -1, 1, 0 }
            assert diff[0] in valid_diffs and diff[1] in valid_diffs

        repeat(single_run, self.RUNS)

    
    def test_move_randomly_moves_in_bounds(self):
        def single_run():
            self.enemy.position = (0, 0)
            self.enemy.move_randomly()
            self.assertTrue(self.dmap.in_bounds(self.enemy.position)) 
