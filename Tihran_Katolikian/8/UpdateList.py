class UpdateList:

    def __init__(self):
        '''
        The constructor of the UpdateList.
        '''
        self.__children = []
    

    def update(self):
        '''
        Method update is used to do anything object need to do in current state. In usual case, any class that
        inherits UpdateList and overrides update method should call it's parent super().update()
        '''
        for child in self.__children:
            child.update()


    def add_child(self, child):
        '''
        Adds a child to UpdateList. It will be updated with it.
        :param child: a child;
        :type child: UpdateList.
        '''
        self.__children.append(child)

    
    def add_children(self, *children):
        '''
        Adds children to UpdateList. They will be updated with it.
        :param *children: a children;
        :type children: a tuple of UpdateLists.
        '''
        self.__children.extend(children)
