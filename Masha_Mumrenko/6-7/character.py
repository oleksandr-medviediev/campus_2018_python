class Character :

    def __init__(self, name):
        self.name = name
        self.__bag = 0
        self.__hp = 3


    @property
    def bag(self):
        return self.__bag


    @bag.setter
    def bag(self, bag):
        self.__bag = bag


    @property
    def hp(self):
        return self.__hp


    @hp.setter
    def hp(self, hp):
        self.__hp = hp
    
