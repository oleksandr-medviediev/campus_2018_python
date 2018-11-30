import unittest
import sys

sys.path.append('..')

import player


class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.__player = player.Player(1, 1, 1)

    def test_player_movement(self):
        
        position = (1, 2)

        self.__player.set_position(*position)

        self.assertEquals(
            self.__player.position, 
            position, 
            "player set_position failure"
            )

    def test_player_treasure_granting(self):

        oldBag = self.__player.bag

        self.__player.grant_treasure(1)

        self.assertNotEqual(
            oldBag, 
            self.__player.bag, 
            "grant_treasure failure")

    def test_player_damaging(self):

        oldHealth = self.__player.health

        self.__player.damage(1)

        self.assertEqual(self.__player.health, oldHealth - 1, "player damage failure")

    def tearDown(self):
        del self.__player

if __name__ == "__main__":
    unittest.main()
