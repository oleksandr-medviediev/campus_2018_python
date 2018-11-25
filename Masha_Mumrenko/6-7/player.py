from character import Character
import logger_decorator

class Player(Character):

    @logger_decorator.time_logger_decorator
    @logger_decorator.debug_logger_decorator
    def __init__(self, name, position):
        
        Character.__init__(self, name, position)


    @logger_decorator.time_logger_decorator
    @logger_decorator.debug_logger_decorator
    def reinit(self, name, position, bag, hp):
        """
        Assigns new values to class attributes
        :param name: loaded name
        :paramtype name: str
        :param position: loaded position
        :paramtype position: list(int,int)
        :param bag: loaded value of bag
        :paramtype bag: int
        :param hp: loaded value of hp
        :paramtype hp: int
        """
        self.name = name
        self.position = position
        self.bag = bag
        self.hp = hp
        

    @logger_decorator.time_logger_decorator
    @logger_decorator.debug_logger_decorator
    def resolve_new_position(self,current_position_status):
        """
        Checks current position cell status
        :param: character of current cell
        :paramtype: str
        """
        if current_position_status == 'treasure' :
            self.bag += 1
        elif current_position_status == 'trap' :
            self.hp -=1


    @logger_decorator.time_logger_decorator
    @logger_decorator.debug_logger_decorator
    def take_damage(self):
        """
        Reduces the hp in one point
        """
        self.hp -=1


    @logger_decorator.time_logger_decorator
    @logger_decorator.debug_logger_decorator
    def check_player_status(self):
        """
        Checks players status (won, lost)
        """
        status = 'Playing'
        if self.bag >= 3 :
            status = 'You won!'
        elif self.hp <= 0 :
            status = 'You lost'

        return status
