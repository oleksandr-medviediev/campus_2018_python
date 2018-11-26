class CannotSaveGameError(Exception):

    def __init__(self, save_data_file_address, causing_exception):
        '''
        Constructor of file data was being attempted to save to.
        :param save_data_file_address: an address of file when data saved.
        :param causing_exception: an exception that caused the problem.
        :type save_data_file_address: str;
        :type causing_exception: Exception.
        '''
        self.__file_address = save_data_file_address
        self.__causing_exception = causing_exception


    def __str__(self):
        return f'Exception "{type(self.__causing_exception)}" caused a problem: {self.__causing_exception} so game\
        wasn\'t saved'
