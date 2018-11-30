import unittest
import sys

sys.path.append('..')
from dungeon_game_vkuksa.character import Character


class TestCharacter(unittest.TestCase):

    def setUp(self):
        self.character = Character('name')

    def tearDown(self):
        del self.character

    def test_1(self):
        self.assertEqual(self.character.character_name, 'name', 'Name getter is wrong')

    def test_2(self):
        self.character.increment_bag()
        self.assertEqual(self.character.bag, 1, 'Failed to increment bag')

    def test_3(self):
        self.character.increment_bag(2)
        self.assertEqual(self.character.bag, 2, 'Failed to increment bag')

    def test_4(self):
        self.character.decrement_hp()
        self.assertEqual(self.character.hp, 2, 'Failed to decrement hp')

    def test_5(self):
        self.character.decrement_hp(2)
        self.assertEqual(self.character.hp, 1, 'Failed to decrement hp')


if __name__ == '__main__':
    unittest.main()
