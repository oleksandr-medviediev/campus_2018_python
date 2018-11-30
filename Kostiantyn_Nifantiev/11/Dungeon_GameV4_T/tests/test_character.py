import unittest
import logging
import sys

sys.path.insert(0, '..')

from character import Character
from game_map import DungeonMap
from dungeon_logger import my_logger


class TestCharacter(unittest.TestCase):

    def test_init(self):

        test_char = Character()
        self.assertEqual(test_char.health, 3, "Wrong init HP!")
        self.assertEqual(test_char.treasures, 0, "Wrong init Treasure count!")


    def test_apply_damage(self):

        test_char = Character()
        former_hp = test_char.health
        test_char.apply_damage()
        self.assertLess(test_char.health, former_hp)


    def test_add_treasure(self):

        test_char = Character()
        former_treasure_count = test_char.treasures
        test_char.add_treasure()
        self.assertGreater(test_char.treasures, former_treasure_count)


    def test_reset(self):

        test_char = Character()
        test_char.add_treasure()
        test_char.apply_damage()
        test_char.reset()
        self.assertEqual(test_char.health, 3, "Wrong init HP!")
        self.assertEqual(test_char.treasures, 0, "Wrong init Treasure count!")


    def test_draw_character(self):

        test_char = Character()
        with self.assertLogs(my_logger, level = logging.INFO) as log:

            test_char.draw_character()

        self.assertEqual(log.output[0], "INFO:dungeon_logger:Health: [#][#][#] Treasures: [ ][ ][ ]")


    def test_is_dead(self):

        test_char = Character()
        test_char.health = 0
        is_dead = test_char.is_dead()
        self.assertTrue(is_dead, "Undead character!")


    def test_is_winner(self):

        test_char = Character()
        test_char.treasures = 3
        is_winner = test_char.is_winner
        self.assertTrue(is_winner, "Greedy character!")


if __name__ == '__main__':

    unittest.main()
