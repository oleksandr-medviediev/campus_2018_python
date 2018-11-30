import sys
import unittest

sys.path.append('..')

import player


class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = player.Player('test_player')

    def tearDown(self):
        del self.player

    def test_hurt_method(self):
        old_hp = self.player._hp
        self.player.hurt('test_script')
        self.assertEqual(self.player._hp, old_hp - 1)

    def test_is_dead_method(self):
        self.assertFalse(self.player.is_dead())

        for _ in range(3):
            self.player.hurt('test_script')

        self.assertTrue(self.player.is_dead())

    def test_pickup_treasure_method(self):
        old_bag = self.player._bag
        self.player.pickup_treasure()
        self.assertEqual(self.player._bag, old_bag + 1)

    def test_is_rich_method(self):
        self.assertFalse(self.player.is_rich())

        for _ in range(3):
            self.player.pickup_treasure()

        self.assertTrue(self.player.is_rich())


if __name__ == '__main__':
    unittest.main()
