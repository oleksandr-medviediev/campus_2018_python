import unittest
from serializer import Serializer

class TestSerializer(unittest.TestCase):

    def setUp(self):
        self.map = GameMap(10)


    def tearDown(self):
        self.map = None


    def test_save(self):
        Serializer.save_map(self.map)
        map_file = open(Serializer.FILE_NAME,"rb")
        self.assertIsNotNone(map_file, "Save File Was not created")


    def test_load(self):
        Serializer.save_map(self.map)
        self.map = Serializer.load_map()
        self.assertIsNotNone(self.map, "File Was Not Loaded")


if __name__ == '__main__':
    unittest.main()