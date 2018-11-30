import unittest

import constants
from enemy import Enemy
from player import Player

class TestEnemyBehaviour(unittest.TestCase):

    def setUp(self):
        self.map_size = constants.MIN_MAP_SIZE
        self.enemy = Enemy(0, 0, self.map_size)

    
    def tearDown(self):
        del self.enemy


    def test_is_possible_to_move_out_map(self):

        is_possible = self.enemy.is_possible_to_move(constants.LEFT_INDEX)
        self.assertEqual(is_possible, False, 'Enemy can not move out the map')

    
    def test_is_possible_to_move_within_map(self):

        is_possible = self.enemy.is_possible_to_move(constants.RIGHT_INDEX)
        self.assertEqual(is_possible, True, 'Enemy can move within the map')


    def test_enemy_damaging(self):

        player = Player(0, 0)

        startHP = player.hp
        self.enemy.damage(player)
        endHP = player.hp

        self.assertNotEqual(startHP, endHP, 'Enemy has not damaged the player')


if __name__ == '__main__':
    unittest.main()
