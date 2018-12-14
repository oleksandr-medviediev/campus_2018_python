import unittest


def load_src(name, fpath):
    import os
    import imp
    return imp.load_source(name, os.path.join(os.path.dirname(__file__), fpath))


game_terrain = load_src("game_terrain", "game_terrain.py")


class TestGameTerrain(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.__map_size = 10
        self.__map = game_terrain.GameTerrain(self.__map_size)

    def test_map_size(self):
        self.assertEqual(self.__map.size, self.__map_size)

    def test_generate_new_map(self):
        self.__map.generate_new_map()
        self.assertIsNotNone(self.__map.terrain)