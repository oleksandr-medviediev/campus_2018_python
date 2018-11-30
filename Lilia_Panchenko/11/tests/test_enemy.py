import unittest
from enemy import Enemy
from player import Player


class EnemyTest(unittest.TestCase):
    
    enemy = Enemy()
    player = Player()
    
    def test_is_attacked_player(self):
        self.enemy.position = self.player.position = [2, 1]
        mapsize = 8
        self.assertTrue(self.enemy.is_attacked_player(self.player))
        self.enemy.move(8)
        self.assertFalse(self.enemy.is_attacked_player(self.player))

if __name__ == '__main__':
    unittest.main()
