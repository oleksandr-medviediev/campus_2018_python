import unittest
import sys

sys.path.append('..')

import constants
from utilities import Utilities

class TestUtilities(unittest.TestCase):

    def test_get_shift_by_right(self):

        index = constants.RIGHT_INDEX
        shift_x, shift_y = constants.all_shifts[index]['x'], constants.all_shifts[index]['y']
        expected_shift_x, expected_shift_y = Utilities.get_shift_by_direction(index)

        self.assertEqual((shift_x, shift_y), (expected_shift_x, expected_shift_y), 'Method get_shift_by_direction work wrong')


    def test_get_new_coordinates_to_down(self):

        new_x, new_y = Utilities.get_new_coordinates(constants.DOWN_INDEX, 0, 0)
        self.assertTrue((new_x, new_y) == (1, 0), 'Method get_new_coordinates work wrong for down direction.')


if __name__ == '__main__':
    unittest.main()
