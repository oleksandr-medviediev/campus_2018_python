class Character:
    """
    Basic character class.
    """
    def __init__(self, name):
        """
        Character constructor.
        :__name: name of the character.
        :__bag: number of treasures the character has.
        :__hp: number of hit points the character has.

        :param name: name of the character.
        """
        self.__name = name
        self.__bag = 0
        self.__hp = 3

    def increment_bag(self, step=1):
        """
        Increment __bag by step.

        :param step: incremental step.
        :type step: int.

        :return: None.
        """
        self.__bag += step

    def decrement_hp(self, step=1):
        """
        Decrement __hp by step.

        :param step: decremental step.
        :type step: int.

        :return: None.
        """
        self.__hp -= step

    def is_alive(self):
        """
        Return True if character has more than 0 hit points.

        :return: True if character has more than 0 hit points, False otherwise.
        :rtype: bool.
        """
        return self.__hp > 0

    def is_bag_full(self):
        """
        Return True if character has 3 or more treasures in bag.

        :return: True if character has 3 or more treasures in bag, False otherwise.
        :rtype: bool.
        """
        return self.__bag >= 3

    @property
    def name(self):
        """
        Getter for name just for fun)

        :return: name of the character.
        :rtype: str.
        """
        return self.__name

    @name.setter
    def name(self, name):
        """
        Setter for name just for fun)

        :param name: new name for the character.

        :return: None.
        """
        self.__name = name
