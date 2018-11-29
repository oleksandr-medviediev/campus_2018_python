import unittest
import sys
import os
sys.path.insert(0, os.path.abspath('..'))

import map_creator


class GameMapTest(unittest.TestCase):

    def setUp(self):
        
        map_size_x,map_size_y = 7,8
        self.game_map = map_creator.DungeonGameMap(map_size_x,map_size_y)

        self.right_count_traps = 5
        self.right_count_treasures = 2

        
    def test_generate_characters(self):

        map_square = self.game_map.map_size_x * self.game_map.map_size_y
        generated_characters = self.game_map.generate_characters(map_square)
        
        count_traps = generated_characters.count(self.game_map.game_entities['trap'])
        count_treasures = generated_characters.count(self.game_map.game_entities['treasure'])

        self.assertEqual(self.right_count_traps, count_traps)
        self.assertEqual(self.right_count_treasures, count_treasures)


    def test_spawn_player(self):

        map_square = self.game_map.map_size_x * self.game_map.map_size_y
        generated_characters = self.game_map.generate_characters(map_square)

        traps_and_treasures_indeces = [index for index, item in enumerate(generated_characters) if item == self.game_map.game_entities['treasure']
                                       or item == self.game_map.game_entities['trap']]

        position = self.game_map.spawn_player(generated_characters)
        position_index = position[1] * self.game_map.map_size_x + position[0]
        
        self.assertTrue(position_index not in traps_and_treasures_indeces)


    def tearDown(self):
        print("There is nothing actually to tear down for tests\n")


if __name__ == '__main__':
    unittest.main()


              

        
        




        
