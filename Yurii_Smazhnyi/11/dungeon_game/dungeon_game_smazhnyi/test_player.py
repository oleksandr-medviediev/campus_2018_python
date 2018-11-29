import unittest
from game_map import GameMap
from player import Player

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = Player("Test", 3)


    def tearDown(self):
        self.player = None


    def test_apply_treasure(self):
        start_bag = self.player.bag

        self.player.apply_item(GameMap.TREASURE_SYMBOL)

        self.assertEqual(start_bag+1, self.player.bag, "Treasure Wasn't Applied Correctly")


    def test_apply_trap(self):
        start_hp = self.player.hp

        self.player.apply_item(GameMap.TRAP_SYMBOL)

        self.assertEqual(start_hp-1, self.player.hp, "Trap Wasn't Applied Correctly")


if __name__ == '__main__':
    unittest.main()