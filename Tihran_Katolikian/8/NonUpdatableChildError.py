# to be honest, I don't think this class is nesessary

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
