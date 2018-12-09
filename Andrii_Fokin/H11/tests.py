
import unittest

from Actor import Actor
from Map_ import Map_


class ActorTest(unittest.TestCase):

    actor = Actor()


    def setUp(self):
        self.actor_position = self.actor.position.copy()


    def tearDown(self):
        self.actor_position = None


    def test_move(self):

        self.actor.move("Up")
        self.assertFalse(self.actor_position == self.actor.position)


    def test_undo_move(self):

        self.actor.move("Up")
        self.actor.undo_move()
        self.assertTrue(self.actor_position == self.actor.position)



class MapTest(unittest.TestCase):
    game_map = Map_(10)
    full_map_size = game_map.size

    def test_free_call(self):
        cell = self.game_map.get_free_cell()
        self.assertTrue(self.game_map.get_cell_type(cell) == self.game_map.cell_free)


    def test_borders(self):

        for i in range(self.full_map_size):
            self.assertTrue(self.game_map.get_cell_type([0, i]) == self.game_map.cell_border)
            self.assertTrue(self.game_map.get_cell_type([self.full_map_size - 1, i]) == self.game_map.cell_border)

            self.assertTrue(self.game_map.get_cell_type([i, 0]) == self.game_map.cell_border)
            self.assertTrue(self.game_map.get_cell_type([i, self.full_map_size - 1]) == self.game_map.cell_border)


if __name__ == "__main__":
    unittest.main()
