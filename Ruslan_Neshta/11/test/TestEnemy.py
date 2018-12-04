import unittest
from World import World
from Player import Player
from Enemy import Enemy


class TestWorld(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.world = World(10)
        cls.player = Player(cls.world)
        cls.enemy = Enemy(cls.world)

    def test_init_enemy_position(self):
        player_pos = [self.player.x, self.player.y]
        enemy_pos = [self.enemy.x, self.enemy.y]
        self.assertNotEqual(player_pos, enemy_pos)

    def test_player_daamage(self):
        self.world.update_player_position(self.player, self.enemy.x, self.enemy.y)
        self.assertEqual(self.player.health, 2)


if __name__ == '__main__':
    unittest.main()
