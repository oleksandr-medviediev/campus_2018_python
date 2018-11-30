import unittest
import sys
import os
sys.path.insert(0, os.path.abspath('..'))


from player import Player


class PlayerTest(unittest.TestCase):     

    def test_resolve_new_position(self):

        test_player = Player('TestPlayer', [0,0])
        
        test_player.resolve_new_position('cell')
        self.assertEqual(test_player.bag, 0)
        self.assertEqual(test_player.hp, 3)

        test_player.resolve_new_position('treasure')
        self.assertEqual(test_player.bag, 1)
        self.assertEqual(test_player.hp, 3)

        test_player.resolve_new_position('trap')
        self.assertEqual(test_player.bag, 1)
        self.assertEqual(test_player.hp, 2)


    def test_check_player_status(self):

        test_player = Player('TestPlayer', [0,0])

        test_player.bag = 2
        test_player.resolve_new_position('treasure')

        self.assertEqual(test_player.check_player_status(),'You won!')

        test_player.bag = 2
        test_player.hp = 2

        self.assertNotEqual(test_player.check_player_status(),'You won!')
        self.assertNotEqual(test_player.check_player_status(),'You lost')
        

    def tearDown(self):
        print("It is called after every test function\n")


if __name__ == '__main__':
    unittest.main()
