import unittest
import my_enemy


class MyEnemyTest(unittest.TestCase):

    def setUp(self):
        
        self.enemy_instance = my_enemy.Enemy()
        self.map_size = 5
        self.enemy_instance.initialize((3,2))


    def test_is_new_position_generated(self):

        _enemy_prev_position = self.enemy_instance.position

        self.enemy_instance.position = self.enemy_instance._Enemy__generate_next_position(self.map_size)

        _enemy_generated_position = self.enemy_instance.position

        self.assertNotEqual(_enemy_generated_position, _enemy_prev_position, 'New position is not generated')


    def tearDown(self):
        print('Exiting enemy tests')


if __name__ == '__main__':
    unittest.main()
