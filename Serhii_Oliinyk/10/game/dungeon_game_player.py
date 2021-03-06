import dungeon_game_logger as log


class Character:
    def __init__(self):
        self.__health = 3
        self.__treasure_number = 0


    @property
    def health(self):
        return self.__health

    
    @health.setter
    def health(self, health):
        self.__health = health


    @property
    def treasure_number(self):
        return self.__treasure_number

    
    @treasure_number.setter
    def treasure_number(self, treasure_number):
        self.__treasure_number = treasure_number


class Player(Character):
    def __init__(self):
        super().__init__()
        self.__position = [0, 0]


    def increase_treasure_and_check_on_win(self):
        """
        Increase counter of treasure number and check if treasure number == 3.

        :return: True or False.
        :rtype: bool.

        """
        self.treasure_number += 1

        result = False
        if self.treasure_number == 3:
            log.logger.info("\nYou win!\n")
            result = True
        
        return result
    

    def decrease_health_and_check_on_lose(self):
        """
        Descrease counter of health number and check if health == 0.

        :return: True or False.
        :rtype: bool.

        """
        self.health -= 1

        result = False
        if self.health == 0:
            log.logger.info("\nYou lose!\n")
            result = True

        return result
    

    def is_player_dead(self):
        """
        Check if player dead.

        :return: True or False.
        :rtype: bool.

        """
        return self.health == 0


    def is_player_win(self):
        """
        Check if player win.

        :return: True or False.
        :rtype: bool.

        """
        return self.treasure_number == 3


    @property
    def position(self):
        return self.__position


    @position.setter
    def position(self, position):
        self.__position = position
