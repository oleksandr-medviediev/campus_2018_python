
import unittest


def load_src(name, fpath):
    import os
    import imp
    return imp.load_source(name, os.path.join(os.path.dirname(__file__), fpath))


game_terrain = load_src("game_terrain", "../game_terrain.py")
character = load_src("character", "../character.py")


class TestCharacter(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.__map_size = 10
        self.__map = game_terrain.GameTerrain(self.__map_size)
        self.__map.generate_new_map()

    def testPositionGeneration(self):
        self.assertEqual(self.__map.find_player_position(), character.position)
