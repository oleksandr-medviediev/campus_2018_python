import unittest
import sys
import os
sys.path.insert(0, os.path.abspath('..'))

import logic_module
import files_module


class GameSaveTest(unittest.TestCase):

    def setUp(self):

        self.game = logic_module.Game(10,10, 'TestName')
        self.map_size = (self.game.game_map.map_size_x, self.game.game_map.map_size_y)
        files_module.save_game_state(self.game.game_map.generated_map,
                                     self.game.player.position, self.map_size, self.game.player.bag,
                                     self.game.player.hp, self.game.player.name, self.game.enemy.position)

    def test_save_file(self):

        saved_object_list = files_module.load_game()
        loaded_map, map_size = saved_object_list[0], saved_object_list[1]
        position, bag, hp = saved_object_list[2], saved_object_list[3], saved_object_list[4]
        name, enemy_position = saved_object_list[5], saved_object_list[6]

        equality = True;
        
        equlity = equality and (self.game.game_map.generated_map == loaded_map)
        equlity = equality and (map_size == self.map_size)
        equality = equality and (self.game.player.position == position) and (self.game.player.bag == bag) and (self.game.player.hp == hp)
        equality = equality and (self.game.player.name == name) and (self.game.enemy.position == enemy_position)

        self.assertTrue(equality)


    def tearDown(self):

        os.remove(files_module.SAVE_FILE_NAME)


if __name__ == '__main__':
    unittest.main()
