import unittest
from World import World


class TestWorld(unittest.TestCase):
    def setUp(self):
        self.world = World(3)
        self.game_save = {}

    def tearDown(self):
        self.world = []

    def test_init_player_position(self):
        self.world.init_player_position(1, 1)
        self.assertEqual(self.world.world[1][1], World.player)

    def test_save(self):
        self.world.save(self.game_save)
        self.assertNotEqual(self.game_save, {})

    def test_load(self):
        with self.assertRaises(KeyError):
            self.world.load({})

        world_copy = self.world.world.copy()
        self.world.save(self.game_save)
        self.world.load(self.game_save)
        self.assertEqual(world_copy, self.world.world)


if __name__ == '__main__':
    unittest.main()
