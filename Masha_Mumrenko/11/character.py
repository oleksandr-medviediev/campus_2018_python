import logger_decorator


class Character :

    def __init__(self, name, position):
        self.name = name
        self.__bag = 0
        self.__hp = 3
        self.__position = position


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


    @property
    def position(self):
        return self.__position


    @position.setter
    def position(self, position):
        self.__position = position


    @logger_decorator.time_logger_decorator
    @logger_decorator.debug_logger_decorator
    def move(self, direction):
        """
        Changes the position of player
        :param: value how to change the position
        :paramtype: tuple(int,int)
        """
        self.__position[0] = self.__position[0] + direction[0]
        self.__position[1] = self.__position[1] + direction[1]          

        
    @logger_decorator.time_logger_decorator
    @logger_decorator.debug_logger_decorator
    def move_opposite(self, direction):
        """
        Changes the position of player opposite to given direction
        :param: value how to change the position
        :paramtype: tuple(int,int)
        """
        self.__position[0] = self.__position[0] - direction[0]
        self.__position[1] = self.__position[1] - direction[1]
        
            
    @logger_decorator.time_logger_decorator
    @logger_decorator.debug_logger_decorator
    def check_new_position(self, borders):
        """
        Checks if position is in borders of map
        :param: size of map
        :paramtype: tuple(int,int)
        """
        is_inside_map = False
        
        if 0 <= self.__position[0] < borders[1] and 0 <= self.__position[1] < borders[0]:
            is_inside_map = True

        return is_inside_map
    
