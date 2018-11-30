import unittest
import logging
import sys

sys.path.insert(0, '..')

from character import Player
from game_map import DungeonMap
from dungeon_logger import my_logger


class TestPlayer(unittest.TestCase):

    def setUp(self):

        self.map_for_player_test = DungeonMap()
        self.map_for_player_test.set_map_size(10, 10)
        self.map_for_player_test.generate_map()
        self.map_size = self.map_for_player_test.map_size


    def tearDown(self):

        self.map_for_player_test.reset_map_size()


    def test_randomize_initial_position(self):

        test_player = Player()
        test_player.randomize_initial_position(self.map_for_player_test)

        self.assertIn(test_player.player_x, range(0, self.map_for_player_test.map_size[0]))
        self.assertIn(test_player.player_y, range(0, self.map_for_player_test.map_size[1]))


    def test_valid_move(self):

        valid_moves = [('w', 'You have moved up'), ('a', 'You have moved left' ), ('s', 'You have moved down'), ('d', 'You have moved right')]
        test_player = Player()
        test_player.randomize_initial_position(self.map_for_player_test)
        test_player.player_x = self.map_for_player_test.map_size[0] / 2
        test_player.player_y = self.map_for_player_test.map_size[1] / 2

        for move, move_message in valid_moves:

            with self.assertLogs(my_logger, level = logging.INFO) as log:

                result = test_player.make_move(move, *self.map_for_player_test.map_size)
                self.assertTrue(result)

            self.assertEqual(log.output[0], ''.join(["INFO:dungeon_logger:", move_message]))


    def test_invalid_move(self):

        test_player = Player()
        test_player.randomize_initial_position(self.map_for_player_test)
        self.assertFalse(result)


if __name__ == '__main__':

    unittest.main()

