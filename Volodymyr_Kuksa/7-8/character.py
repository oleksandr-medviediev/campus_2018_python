import dungeon_game_decorators


class Character:
    """
    Basic character class.
    """

    def __init__(self, name):
        """
        Character constructor.

        :param name: name of the character.
        """
        self.__character_name = name
        self.__bag = 0
        self.__hp = 3

    @dungeon_game_decorators.log_decor
    @dungeon_game_decorators.debug_decor
    def increment_bag(self, step=1):
        """
        Increment __bag by step.

        :param step: incremental step.
        :type step: int.

        :return: None.
        """
        self.__bag += step

    @dungeon_game_decorators.log_decor
    @dungeon_game_decorators.debug_decor
    def decrement_hp(self, step=1):
        """
        Decrement __hp by step.

        :param step: decremental step.
        :type step: int.

        :return: None.
        """
        self.__hp -= step

    @dungeon_game_decorators.log_decor
    @dungeon_game_decorators.debug_decor
    def is_alive(self):
        """
        Return True if character has more than 0 hit points.

        :return: True if character has more than 0 hit points, False otherwise.
        :rtype: bool.
        """
        return self.__hp > 0

    @dungeon_game_decorators.log_decor
    @dungeon_game_decorators.debug_decor
    def is_bag_full(self):
        """
        Return True if character has 3 or more treasures in bag.

        :return: True if character has 3 or more treasures in bag, False otherwise.
        :rtype: bool.
        """
        return self.__bag >= 3

    @property
    @dungeon_game_decorators.log_decor
    @dungeon_game_decorators.debug_decor
    def character_name(self):
        """
        Getter for name.

        :return: name of the character.
        :rtype: str.
        """
        return self.__character_name

    @character_name.setter
    @dungeon_game_decorators.log_decor
    @dungeon_game_decorators.debug_decor
    def character_name(self, new_name):
        """
        Setter for name.

        :param new_name: new name for the character.
        :type new_name: str.
        """
        self.__character_name = new_name

    @property
    @dungeon_game_decorators.log_decor
    @dungeon_game_decorators.debug_decor
    def hp(self):
        """
        Getter for hp.

        :return: hp.
        :rtype: int.
        """
        return self.__hp

    @hp.setter
    @dungeon_game_decorators.log_decor
    @dungeon_game_decorators.debug_decor
    def hp(self, new_hp):
        """
        Setter for hp.

        :param new_hp: new value of hp.
        :type new_hp: int.
        """
        self.__hp = new_hp

    @property
    @dungeon_game_decorators.log_decor
    @dungeon_game_decorators.debug_decor
    def bag(self):
        """
        Getter for bag.

        :return: bag.
        :rtype: int.
        """
        return self.__bag

    @bag.setter
    @dungeon_game_decorators.log_decor
    @dungeon_game_decorators.debug_decor
    def bag(self, new_bag):
        """
        Setter for bag.

        :param new_bag: new value of bag.
        :type new_bag: int.
        """
        self.__bag = new_bag
