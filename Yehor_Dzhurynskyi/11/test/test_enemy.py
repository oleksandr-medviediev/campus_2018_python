import unittest

sys.path.append('..')

from level import Level
from enemy import Enemy
import dungeon_game_error


class EnemyTest(unittest.TestCase):

    def setUp(self):
        self.__level = Level.generate(8)
        self.__enemy = Enemy(self.__level)

    def test_move(self):

        old_x, old_y = self.__enemy.x, self.__enemy.y
        self.__enemy.move()
        new_x, new_y = self.__enemy.x, self.__enemy.y

        moved_on_x = abs(old_x - new_x) == 1
        moved_on_y = abs(old_y - new_y) == 1

        correct_move = (moved_on_x or moved_on_y) and not (moved_on_x and moved_on_y)
        self.assertTrue(correct_move, 'Move is incorrect')

    def test_respawn(self):

        self.__enemy.respawn()
        is_correct_pos = self.__enemy.x < self.__level.size and self.__enemy.y < self.__level.size
        self.assertTrue(is_correct_pos, 'new point on respawn in incorrent')

    def tearDown(self):
        del self.__level
        del self.__enemy

if __name__ == '__main__':
    unittest.main()
