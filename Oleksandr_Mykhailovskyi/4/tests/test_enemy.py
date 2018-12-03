import unittest
import sys

sys.path.append('..')

from game_enemy import Enemy
from game_enemy import Position
from game_enemy import EnemyState

from player import Player


class TestGameEnemy(unittest.TestCase):
    def setUp(self):
        self.enemy = Enemy(10, 1, Position(0, 0), Position(0, 0), Position(10, 10))
        self.player = Player(Position(1, 1), 10, 1)

    def tearDown(self):
        del self.enemy

    def test_init(self):
        self.assertEqual(self.enemy.hp, 10)
        self.assertEqual(self.enemy.damage, 1)

    def test_idle_state(self):
        self.enemy.on_idle(self.player)
        self.assertEqual(self.enemy.state, EnemyState.IDLE)

    def test_attack_state(self):
        player_hp = int(self.player.hp)
        self.enemy.on_attack(self.player)
        self.assertNotEqual(player_hp, self.player.hp)




if __name__ == '__main__':
    unittest.main()
