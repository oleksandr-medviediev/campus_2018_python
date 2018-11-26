import threading

from logging_utility import logging_debug_decorator
from logging_utility import logging_info_decorator

from game_map import Position


class Player:
    @logging_debug_decorator
    @logging_info_decorator
    def __init__(self, position, hp, bag_counter):
        """
        Initializes instance of player.

        Args:
            position (Position): player initial position.
            hp (int): player initial hp.
            bag_counter: player intial bag counter(treasures).
        """
        self.position = position
        self.__hp = hp if hp > 0 else 0
        self.bag_counter = bag_counter if bag_counter > 0 else 0

        self.mrlock = threading.RLock()
        self.hp_lock = threading.RLock()

    @property
    def hp(self):
        self.hp_lock.acquire()
        res = self.__hp
        self.hp_lock.release()
        return res

    @hp.setter
    def hp(self, hp):
        self.hp_lock.acquire()
        self.__hp = hp if hp > 0 else 0
        self.hp_lock.release()

    @logging_debug_decorator
    @logging_info_decorator
    def move(self, action):
        """
        Args:
            action (str): action Up/Down/Left/Right.
        """
        self.mrlock.acquire()
        if action == "Up":
            self.position.y -= 1
        elif action == "Down":
            self.position.y += 1

        if action == "Left":
            self.position.x -= 1
        elif action == "Right":
            self.position.x += 1
        self.mrlock.release()


    @logging_debug_decorator
    @logging_info_decorator
    def move_with_restr(self, action, restriction):
        """
        Args:
            action (str): action Up/Down/Left/Right.
            restriction (position): restriction on max x & y.
        """
        # TO DO: make this a decorator for move
        self.move(action)

        if self.position.x < 0:
            self.position.x = 0
        if self.position.y < 0:
            self.position.y = 0

        if self.position.x >= restriction.x:
            self.position.x = restriction.x - 1
        if self.position.y >= restriction.y:
            self.position.y = restriction.y - 1
