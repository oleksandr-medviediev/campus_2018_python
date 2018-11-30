import sys
import unittest

sys.path.append('..')

import map_generator


class TestMapGenerator(unittest.TestCase):

    def test_generate_function(self):
        map = map_generator.generate(10)

        self.assertTrue(isinstance(map, list))
        self.assertEqual(len(map), 10)

        for row in map:
            self.assertTrue(isinstance(row, list))
            self.assertEqual(len(row), 10)

            for cell in row:
                self.assertTrue(cell in ('Trap', 'Treasure', None))


if __name__ == '__main__':
    unittest.main()
