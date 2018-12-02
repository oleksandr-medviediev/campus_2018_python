import unittest
from sys import path
from contextlib import contextmanager


path.append('..')

from UpdateList import UpdateList
from DungeonGameErrors import NonUpdatableClildError


class TestUpdateList(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        '''
        Used to create a new UpdateList instance for test.
        '''
        cls.__update_list = UpdateList()


    def test_add_child(self):
        '''
        Test if update list is able to add new child
        '''
        new_update_list = UpdateList()
        self.__update_list.add_child(new_update_list)
        self.assertEqual(len(self.__update_list.get_children()), 1)


    def test_update(self):
        '''
        Tests is update list updates children
        '''
        class TestUpdateClass(UpdateList):
            def __init__(self):
                self.some_value = None
            def update(self):
                self.some_value = 42

        test_class = TestUpdateClass()
        self.__update_list.add_child(test_class)
        self.__update_list.update()
        self.assertIsNotNone(test_class.some_value)


    def test_non_updatable_child(self):
        '''
        Tests how update list will act if we will attempt to add a non-updatable child.
        '''
        some_object = object()
        with self.assertRaises(NonUpdatableClildError) as error_check:
            self.__update_list.add_child(some_object)


if __name__ == '__main__':
    unittest.main()
