import unittest
import dungeon_game_map as mm
import dungeon_game_player as mp
import dungeon_game as dng


class TestMapSize(unittest.TestCase):
    def setUp(self):
        self.game_map = mm.GameMap()
        self.game_map.create_map(8)


    def tearDown(self):
        self.game_map.game_matrix = []


    def test_map_size(self):
        self.assertGreaterEqual(self.game_map.get_map_size(), 8, "Incorect map size!")


    def test_player_position(self):
        position = self.game_map.player_position
        area = self.game_map.game_matrix
        self.assertEqual(area[position[0]][position[1]], "p", "Incorect player position")

    
    def test_enemy_position(self):
        position = self.game_map.enemy_position
        area = self.game_map.game_matrix
        self.assertEqual(area[position[0]][position[1]], "e", "Incorect enemy position")


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = mp.Player()


    def tearDown(self):
        self.player.position = []

    
    def test_health(self):
        self.assertLessEqual(self.player.health, 3)


    def test_treasure(self):
        self.assertGreaterEqual(self.player.treasure_number, 0)


    def test_position_out_of_range(self):
        position = self.player.position
        self.assertGreaterEqual(position[0] * position[1], 0)
    

class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = dng.DungeonGame()
        self.game.initialize()


    def tearDown(self):
        del(self.game)


    def test_player_direction(self):
        direction = self.game.update_player_directions()
        self.assertLessEqual(len(direction), 4)
    

    def test_enemy_direction(self):
        direction = self.game.update_enemy_directions()
        self.assertLessEqual(len(direction), 4)


if __name__ == ('__main__'):
    unittest.main()
