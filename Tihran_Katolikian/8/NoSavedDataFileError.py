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
