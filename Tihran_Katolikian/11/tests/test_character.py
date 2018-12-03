import unittest
from sys import path
from random import choice
import time


path.append('..')


from Character import Character
from DungeonMap import DungeonMap
import DungeonGameConfig


class TestCharacter(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        '''
        Inits a new enemy.
        '''
        cls.__map = DungeonMap()
        map_size = 10
        cls.__map.generate_new_map(map_size)
        cls.__player = Character('Test', 10, cls.__map)


    def test_receiving_damage(self):
        '''
        Tests if character is moving.
        '''
        start_hp = self.__player.get_hp()
        self.__player.receive_damage(2)
        self.assertEqual(start_hp - 2, self.__player.get_hp())


    def test_treasures(self):
        '''
        Tests the initial value of treasures.
        '''
        expected_treaures_number = 0
        self.assertEqual(self.__player.get_treasures_number(), expected_treaures_number)


    def test_kill_character(self):
        '''
        Tests if character can be killed.
        '''
        self.__player.receive_damage(100)
        self.assertFalse(self.__player.is_alive())


if __name__ == '__main__':
    unittest.main()
