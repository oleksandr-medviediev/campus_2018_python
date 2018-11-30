import unittest
from random import choice
import sys
import test

sys.path.append('..')

from game_pkg import dun_map
from game_pkg import dun_player
from game_pkg import dungeon_enemy



class DunPlayerTests(unittest.TestCase):

    def test_player_move(self):

        game_map = dun_map.DungeonMap(10)
        player = dun_player.Player()
        game_map.set_player_on_map(player)
        player.hit_points = 1000000
        size = len(game_map.dun_map[0])
        
        for i in range(1000):
            
            player.command = choice(dun_player.COMMANDS)
            player.process_move(game_map)
            position = player.position
            self.assertGreater(size, position[0], 'X position bigger then map size')
            self.assertGreater(size, position[1], 'Y position bigger then map size')
            self.assertLessEqual(0, position[1], 'Y less then 0')
            self.assertLessEqual(0, position[0], 'X less then 0')
        
        print("test_player_move is OK\n")
    
    def test_player_damaged(self):

        player =dun_player.Player()
        player.hit_points = 1000
        for damage in range(100):

            old_hit_points = player.hit_points
            player.applay_damage(damage + 1)
            self.assertNotEqual(old_hit_points, player.hit_points)

        print("test_player_damaged is OK\n")

    def test_player_score(self):

        player = dun_player.Player()
        for score in range(100):

            old_score = player.treasure_picked
            player.change_score(score + 1)
            self.assertNotEqual(old_score, player.treasure_picked)

        print("test_player_score is OK\n")

class DunEnemyTest(unittest.TestCase):

    def test_enemy_move(self):

        game_map = dun_map.DungeonMap(10)
        enemy = dungeon_enemy.Enemy()
        enemy.position = dun_map.dungeon_map_generate.set_character_randomly(game_map.dun_map)
        size = len(game_map.dun_map[0])
        
        for i in range(1000):
            
            enemy.command = choice(dun_player.COMMANDS)
            enemy.process_move(game_map)
            position = enemy.position
            self.assertGreater(size, position[0], 'X position bigger then map size')
            self.assertGreater(size, position[1], 'Y position bigger then map size')
            self.assertLessEqual(0, position[1], 'Y less then 0')
            self.assertLessEqual(0, position[0], 'X less then 0')

        print("test_enemy_move is OK'n")

    def test_enemy_attack(self):

        enemy = dungeon_enemy.Enemy()
        player = dun_player.Player()
        player.hit_points = 100000
        for damage in range(100):

            old_hit_points = player.hit_points
            enemy.attack(player)
            self.assertNotEqual(old_hit_points, player.hit_points)

        print("test_enemy_attack is OK\n")

class DunMapTest(unittest.TestCase):

    def test_map_generate(self):

        for size in range(200):

            game_map = dun_map.dungeon_map_generate.generate_map(size + 1)
            self.assertEqual(len(game_map), len(game_map[0]))
        
        print('\n Map size is OK\n')
        

if __name__ == '__main__':

    unittest.main()
