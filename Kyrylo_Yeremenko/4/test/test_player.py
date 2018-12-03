import unittest
import random
from player import Player
from dungeon_map import DungeonMap


class TestPlayer(unittest.TestCase):

    def setUp(self):

        self.game_map = DungeonMap(10)
        self.player = Player(self.game_map)

    def test_init_position(self):

        self.assertTrue(self.game_map.is_index_valid(self.player.position))
        self.assertTrue(self.game_map.game_map[self.player.position[0]][self.player.position[1]] == DungeonMap.SYMBOL_TILE)

    def test_move(self):

        move_directions = ["U", "L", "R", "D"]
        move_coords = {"U": [-1, 0], "L": [0, -1], "R": [0, +1], "D": [+1, 0]}

        direction = random.choice(move_directions)

        player_pos = self.player.position

        if self.player.move(direction, self.game_map):

            self.assertTrue(self.player.position[0] == player_pos[0] + move_coords[direction][0])
            self.assertTrue(self.player.position[1] == player_pos[1] + move_coords[direction][1])

    def test_mark_last_pos(self):

        self.player.mark_last_pos(self.game_map)
        self.assertTrue(self.game_map.game_map[self.player.position[0]][self.player.position[1]] == DungeonMap.SYMBOL_LASTPOS)

    def test_is_dead(self):

        self.assertFalse(self.player.is_dead())
        self.player.decrease_hitpoints(5)
        self.assertTrue(self.player.is_dead())

    def test_is_bag_full(self):

        self.assertFalse(self.player.is_bag_full())
        self.player.bag += 1
        self.assertFalse(self.player.is_bag_full())
        self.player.bag += 2
        self.assertTrue(self.player.is_bag_full())

    def test_get_hitpoints(self):

        self.assertTrue(self.player.get_hitpoints() == self.player.hitpoints)

    def test_decrease_hitpoints(self):

        player_hitpoints = self.player.get_hitpoints()
        damage = 1

        self.player.decrease_hitpoints(damage)

        self.assertTrue(self.player.get_hitpoints() == (player_hitpoints - damage))

    def tearDown(self):
        del self.player


if __name__ == "__main__":
    unittest.main()
