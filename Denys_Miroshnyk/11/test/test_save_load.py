
import unittest


def load_src(name, fpath):
    import os
    import imp
    return imp.load_source(name, os.path.join(os.path.dirname(__file__), fpath))


game_terrain = load_src("game_terrain", "../game_terrain.py")
character = load_src("character", "../character.py")
save_load = load_src("save_load", "../save_load.py")


class TestSaveLoad(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.__map_size = 10
        self.__map = game_terrain.GameTerrain(self.__map_size)
        self.__map.generate_new_map()

    def testSaveLoad(self):
        save_load.save_game(self.__map.terrain)

        saved_map = save_load.load_game()
        for i in range(1, self.__map_size + 2):
            for j in range(1, self.__map_size + 2):
                self.assertEqual(self.__map.terrain[i][j], saved_map[i][j])

        self.assertEqual(self.__map.find_player_position(), character.position)
