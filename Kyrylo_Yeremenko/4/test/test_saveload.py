import unittest
import os
from player import Player
from dungeon_map import DungeonMap
from utils import save_game, load_game


class TestSaveLoad(unittest.TestCase):

    def setUp(self):

        self.map_size = 10

        self.active_map = DungeonMap(self.map_size)
        self.player = Player(self.active_map)

        self.loaded_map = DungeonMap(0, False)
        self.loaded_player = Player(self.loaded_map)

        self.file_path = 'test_save.dat'

    def test_save_load(self):

        self.assertTrue(save_game(self.file_path, self.active_map, self.player))
        self.assertTrue(load_game(self.file_path, self.loaded_map, self.loaded_player))

        self.assertTrue(len(self.active_map.game_map) == len(self.loaded_map.game_map))

        for row_index in range(len(self.active_map.game_map)):

            self.assertTrue(len(self.active_map.game_map[row_index]) == len(self.loaded_map.game_map[row_index]))
            for col_index in range(len(self.active_map.game_map[row_index])):
                self.assertTrue(self.active_map.game_map[row_index][col_index] == self.loaded_map.game_map[row_index][col_index])

        self.assertTrue(self.player.hitpoints == self.loaded_player.hitpoints)
        self.assertTrue(self.player.bag == self.loaded_player.bag)
        self.assertTrue(self.player.position[0] == self.loaded_player.position[0])
        self.assertTrue(self.player.position[1] == self.loaded_player.position[1])

    def tearDown(self):
        os.remove(self.file_path)


if __name__ == "__main__":
    unittest.main()
