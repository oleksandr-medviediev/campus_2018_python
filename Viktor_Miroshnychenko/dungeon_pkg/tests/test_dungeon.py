import unittest
from random import choice
import sys
import test

sys.path.append('..')

from game_pkg import dun_map
from game_pkg import dun_player
from game_pkg import dungeon_enemy



class DunPlayerTests(unittest.TestCase):

    def setUp(self):

        self.game_map = dun_map.DungeonMap(10)
        self.player = dun_player.Player()
        self.game_map.set_player_on_map(self.player)
        self.player.hit_points = 1000000
        self.size = len(self.game_map.dun_map[0])
    
    def tearDown(self):

        del self.player
        del self.game_map
        del self.size

    def test_player_move(self):

        for i in range(1000):
            
            self.player.command = choice(dun_player.COMMANDS)
            self.player.process_move(self.game_map)
            position = self.player.position
            self.assertGreater(self.size, position[0], 'X position bigger then map size')
            self.assertGreater(self.size, position[1], 'Y position bigger then map size')
            self.assertLessEqual(0, position[1], 'Y less then 0')
            self.assertLessEqual(0, position[0], 'X less then 0')
        
        print("test_player_move is OK\n")
    
    def test_player_damaged(self):

        for damage in range(100):

            old_hit_points = self.player.hit_points
            self.player.applay_damage(damage + 1)
            self.assertNotEqual(old_hit_points, self.player.hit_points)

        print("test_player_damaged is OK\n")

    def test_player_score(self):

        for score in range(100):

            old_score = self.player.treasure_picked
            self.player.change_score(score + 1)
            self.assertNotEqual(old_score, self.player.treasure_picked)

        print("test_player_score is OK\n")

class DunEnemyTest(unittest.TestCase):

    def setUp(self):

        self.game_map = dun_map.DungeonMap(10)
        self.enemy = dungeon_enemy.Enemy()
        self.enemy.position = dun_map.dungeon_map_generate.set_character_randomly(self.game_map.dun_map)
        self.size = len(self.game_map.dun_map[0])
        self.player = dun_player.Player()
        self.player.hit_points = 100000

    def tearDown(self):

        del self.game_map
        del self.enemy
        del self.size
        del self.player

    def test_enemy_move(self):

        for i in range(1000):
            
            self.enemy.command = choice(dun_player.COMMANDS)
            self.enemy.process_move(self.game_map)
            position = self.enemy.position
            self.assertGreater(self.size, position[0], 'X position bigger then map size')
            self.assertGreater(self.size, position[1], 'Y position bigger then map size')
            self.assertLessEqual(0, position[1], 'Y less then 0')
            self.assertLessEqual(0, position[0], 'X less then 0')

        print("test_enemy_move is OK'n")

    def test_enemy_attack(self):

        for damage in range(100):

            old_hit_points = self.player.hit_points
            self.enemy.attack(self.player)
            self.assertNotEqual(old_hit_points, self.player.hit_points)

        print("test_enemy_attack is OK\n")

class DunMapTest(unittest.TestCase):

    def setUp(self):

        self.game_map = dun_map.dungeon_map_generate.generate_map(10)

    def tearDown(self):

        del self.game_map

    def test_map_generate(self):

        for row in self.game_map:

            self.assertEqual(len(self.game_map), len(row))
        
        print('\n Map size is OK\n')
        

if __name__ == '__main__':

    unittest.main()
