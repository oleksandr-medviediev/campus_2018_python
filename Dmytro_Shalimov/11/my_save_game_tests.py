import unittest
import os
import my_game_flow


class MyGameFlowSaveGameTest(unittest.TestCase):

    def setUp(self):

        self.game_flow = my_game_flow.MyGameFlow()
        self.file_extension = '.pickle'


    def __count_files_by_extension(self, extension):
        """
        Counts files by given extension in module directory

        :param str extension:
        :return number of files woth given extension
        :rtype int
        """

        _files_amount = 0;

        for root, dirs, files in os.walk('.'):

            for file in files:    

                if file.endswith(extension):
                    _files_amount += 1

        return _files_amount


    def test_is_save_game_file_created(self):

        _files_amount_before_saving = self.__count_files_by_extension(self.file_extension)
        
        self.game_flow._MyGameFlow__process_save_game()

        _files_amount_after_saving = self.__count_files_by_extension(self.file_extension)

        self.assertGreater(_files_amount_after_saving, _files_amount_before_saving, 'File was not created')


    def tearDown(self):
        print('Exiting game flow save game test')


if __name__ == '__main__':
    unittest.main()   
