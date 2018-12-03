import unittest
import sys

sys.path.append('..')

from player import Position
from player import Player
from game_world import GameWorld


class TestPlayer(unittest.TestCase):
    def test_move_unsupported_actions(self):
        specimen = Player(Position(0, 0), 1, 1)

        unsupported_actions = ["Save", "Load", "Help", "Abracadabra"]

        unchangedPos = Position(specimen.position.x, specimen.position.y)
        for action in unsupported_actions:
            specimen.move(action)

            pos = specimen.position

            self.assertEqual(pos.x, unchangedPos.x)
            self.assertEqual(pos.y, unchangedPos.y)

    def test_init(self):
        # test init with nuacceptable values
        specimen = Player(Position(0, 0), -1, -1)
        self.assertEqual(specimen.bag_counter, 0)
        self.assertEqual(specimen.hp, 0)

    # --------- Move tests
    def test_move_up(self):
        specimen = Player(Position(0, 0), 1, 1)
        unchangedPos = Position(specimen.position.x, specimen.position.y)

        specimen.move("Up")
        self.assertEqual(specimen.position.x, unchangedPos.x)
        self.assertEqual(specimen.position.y, unchangedPos.y - 1)

    def test_move_left(self):
        specimen = Player(Position(0, 0), 1, 1)
        unchangedPos = Position(specimen.position.x, specimen.position.y)

        specimen.move("Left")
        self.assertEqual(specimen.position.x, unchangedPos.x - 1)
        self.assertEqual(specimen.position.y, unchangedPos.y)

    def test_move_right(self):
        specimen = Player(Position(0, 0), 1, 1)
        unchangedPos = Position(specimen.position.x, specimen.position.y)

        # test move Right
        specimen.move("Right")
        self.assertEqual(specimen.position.x, unchangedPos.x + 1)
        self.assertEqual(specimen.position.y, unchangedPos.y)

    def test_move_down(self):
        specimen = Player(Position(0, 0), 1, 1)
        unchangedPos = Position(specimen.position.x, specimen.position.y)

        specimen.move("Down")
        self.assertEqual(specimen.position.x, unchangedPos.x)
        self.assertEqual(specimen.position.y, unchangedPos.y + 1)


    # --------- Move with restrictions test
    def test_move_with_restricts_1(self):
        specimen = Player(Position(0, 0), 1, 1)
        unchanged_pos = Position(specimen.position.x, specimen.position.y)
        restriction = Position(1, 1)

        # test move Up
        specimen.move_with_restr("Up", restriction)
        self.assertEqual(specimen.position.x, unchanged_pos.x)
        self.assertEqual(specimen.position.y, unchanged_pos.y)

        # test move Left
        specimen.move_with_restr("Left", restriction)
        self.assertEqual(specimen.position.x, unchanged_pos.x)
        self.assertEqual(specimen.position.y, unchanged_pos.y)

        # test move Right
        specimen.move_with_restr("Right", restriction)
        self.assertEqual(specimen.position.x, unchanged_pos.x)
        self.assertEqual(specimen.position.y, unchanged_pos.y)

        # test move Down
        specimen.move_with_restr("Down", restriction)
        self.assertEqual(specimen.position.x, unchanged_pos.x)
        self.assertEqual(specimen.position.y, unchanged_pos.y)


if __name__ == '__main__':
    unittest.main()
