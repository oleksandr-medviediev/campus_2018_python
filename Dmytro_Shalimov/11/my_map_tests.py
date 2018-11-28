import unittest
import my_map


class MyMapTests(unittest.TestCase):

    def setUp(self):

       self.map_instance = my_map.MyMap()
       self.map_size_input = int(input('Enter map size: '))

    def test_generated_map_size_equals_input_map_size(self):

       self.map_instance.initialize(self.map_size_input)
       _elements = 0

       for row in self.map_instance.generated_map:
           _elements += len(row)
       
       self.assertEqual(_elements / len(self.map_instance.generated_map), self.map_size_input,
                       'generated map size is not correct')

    def tearDown(self):
        print('Exiting map tests')


if __name__ == '__main__':
    unittest.main()
