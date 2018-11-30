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


class NonUpdatableClildError(Exception):

    def __init__(self, non_updatable_child):
        '''
        Constructor of non updatable child error exception.
        It is raised when someone attempts to add a child to update list that is not a heir of update list so cannot be
        updated.
        :param non_updatable_child: an object that had been attempted to add to update list, but failed;
        :type non_updatable_child: any type.
        '''
        self.__object = non_updatable_child


    def __str__(self):
        return f'"{type(self.__object)}" is not "UpdateList".'


class NoSavedDataFileError(Exception):

    def __init__(self, file_address):
        '''
        Constructor of no saved data file error exception.
        :param file_address: an address on save data file that wasn't found;
        :type file_address: str.
        '''
        self.__file_address = file_address


    def __str__(self):
        return f'Couldn\'t file a save data file on address: {self.__file_address}'
