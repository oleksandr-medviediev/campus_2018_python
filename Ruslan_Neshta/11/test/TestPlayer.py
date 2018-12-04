import unittest
from World import World
from Player import Player


class TestWorld(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.world = World(10)
        cls.player = Player(cls.world)

    def test_init_player_health(self):
        self.assertEqual(self.player.health, 3)

    def test_init_player_treasures(self):
        self.assertEqual(self.player.treasures, 0)


if __name__ == '__main__':
    unittest.main()
