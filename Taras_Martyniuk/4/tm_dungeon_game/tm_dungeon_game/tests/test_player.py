from Player import Player
from DungeonMap import DungeonMap
import unittest as utest
from exceptions import AlreadyDeadError


class TestPlayer(utest.TestCase):
    # i need no teardown as i recreate my member objects for every test
    def setUp(self):
        self.dmap = DungeonMap(20)
        self.player = Player(10, self.dmap, lambda: None)


    def test_try_move_returns_true_if_moving_in_bounds(self):
        center = (self.dmap.size / 2, self.dmap.size / 2)
        self.player.position = center

        move = (1, 0)
        self.assertTrue(self.player.try_move(move))


    def test_try_move_cannot_move_diagonally(self):
        def move_diag():
            diag_move = (1, -1)
            self.player.try_move(diag_move)

        self.assertRaises(ValueError, move_diag)


    def test_lose_health_subtracts_one_health(self):
        start_health = self.player.health
        self.player.lose_health()

        self.assertEqual(self.player.health, start_health - 1)


    def test_lose_health_returns_true_if_killed(self):
        one_shot_player = Player(1, self.dmap, lambda: None)
        self.assertTrue(one_shot_player.lose_health())
    

    def test_lose_health_throws_if_no_more_health(self):
        dead_player = Player(1, self.dmap, lambda: None)
        dead_player.lose_health()

        self.assertRaises(AlreadyDeadError, lambda: dead_player.lose_health())
