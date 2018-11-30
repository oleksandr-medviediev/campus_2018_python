import unittest
import sys

sys.path.append("..")
from dungeon_game_vkuksa.game_map import GameMap, GAME_CHARACTERS


class TestGameMapGetTitleCharacter(unittest.TestCase):

    def setUp(self):
        self.game_map = GameMap(map_size=5)

        row_empty = [GAME_CHARACTERS['Empty']] * 5
        row_treasure = [GAME_CHARACTERS['Treasure']] * 5
        row_trap = [GAME_CHARACTERS['Trap']] * 5

        self.game_map._GameMap__game_map = [row_empty, row_treasure, row_empty, row_trap, row_empty]

    def tearDown(self):
        del self.game_map

    def test_get_tile_character_1(self):
        self.assertEqual(self.game_map.get_tile_character(0, 0),
                         GAME_CHARACTERS['Empty'],
                         'get_tile_character returned wrong character')

    def test_get_tile_character_2(self):
        self.assertEqual(self.game_map.get_tile_character(0, 1),
                         GAME_CHARACTERS['Treasure'],
                         'get_tile_character returned wrong character')

    def test_get_tile_character_3(self):
        self.assertEqual(self.game_map.get_tile_character(0, 3),
                         GAME_CHARACTERS['Trap'],
                         'get_tile_character returned wrong character')

    def test_get_tile_character_4(self):
        self.assertEqual(self.game_map.get_tile_character(0, 0),
                         self.game_map.get_tile_character(0, 0),
                         'get_tile_character is inconsistent')

    def test_get_tile_character_5(self):
        with self.assertRaises(IndexError, msg='IndexError expected'):
            self.game_map.get_tile_character(-1, -1)


if __name__ == '__main__':
    unittest.main()
