import unittest
import sys

sys.path.append('..')

import enemy


class TestEnemy(unittest.TestCase):

    def test_enemy_movement(self):

        enemy_entity = enemy.Enemy(2) 

        oldPosition = enemy_entity.position

        enemy_entity.move()

        self.assertNotEqual(
            oldPosition,
            enemy_entity.position, 
            'enemy movement failure')

if __name__ == "__main__":
    unittest.main()
