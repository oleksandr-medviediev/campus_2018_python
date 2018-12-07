from Enemy import Enemy
from DungeonMap import DungeonMap
import unittest as utest
from utils import tuple_diff, repeat

class TestEnemy(utest.TestCase):
    RUNS = 10


    def test_move_randomly_moves_one_tile_only(self):
        def single_run():
            dmap = DungeonMap(10)
            en = Enemy(dmap)

            start_pos = en.position
            en.move_randomly()
            diff = tuple_diff(en.position, start_pos)

            print(f'st {start_pos}')
            print(f'mv {en.position}')
            print(f'df {diff}')

            valid_diffs = { -1, 1, 0 }
            assert diff[0] in valid_diffs and diff[1] in valid_diffs

        repeat(single_run, self.RUNS)

