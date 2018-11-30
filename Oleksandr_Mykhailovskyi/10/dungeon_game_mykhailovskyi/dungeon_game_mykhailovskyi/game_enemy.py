import random
import threading

from enum import Enum

from .player import Player
from .player import Position

from .game_exceptions import StateError


# TO DO: add saving enemy to another file (e.g. enemysave.txt).


looking_phrases = [
    "Arrrgh!",
    "I'm gonna find ya and kill ya!",
    "I'll find you eventually!"
    ]
found_phrases = ["Here you are!", "Now you die!"]


class EnemyState(Enum):
    ATTACKING = 1,
    MOVING = 2,
    IDLE = 3,


class Enemy:
    """
    Enemy class implemented as state machine.
    Currently supported states are(class EnemyState): ATTACKING, MOVING, IDLE.
    """
    def __init__(self, hp, damage, pos, min_resp_pos, max_resp_pos):
        self.hp = hp
        self.damage = damage

        self.__position = pos
        self.min_resp_pos = min_resp_pos
        self.max_resp_pos = max_resp_pos

        self.range = Position(1, 1)
        self.state = EnemyState.IDLE

        self.mrlock = threading.RLock()

    @property
    def position(self):
        self.mrlock.acquire()
        res = self.__position
        self.mrlock.release()
        return res

    @position.setter
    def position(self, value):
        self.mrlock.acquire()
        self.__position = value
        self.mrlock.release()

    def on_attack(self, player):
        """
        Enemy attack wrapper. Does not check anything, 
        contains attack logic.

        Args:
            player (Player): ingame player.
        """
        self.mrlock.acquire()

        player.hp -= self.damage

        self.position.x = player.position.x
        self.position.y = player.position.y
        while self.position.x == player.position.x and \
                self.position.y == player.position.y:
            print(self.position)
            print(self.min_resp_pos)
            print(self.max_resp_pos)
            self.position.x = random.randint(self.min_resp_pos.x, self.max_resp_pos.x - 1)
            self.position.y = random.randint(self.min_resp_pos.y, self.max_resp_pos.y - 1)

        # print phrase
        max_rand = len(found_phrases) - 1
        rand_phrase_idx = random.randint(0, max_rand)
        print(found_phrases[rand_phrase_idx])

        # teleport to random position
        resp_pos = Position(0, 0)
        resp_pos.x = random.randint(self.min_resp_pos.x, self.max_resp_pos.x)
        resp_pos.y = random.randint(self.min_resp_pos.y, self.max_resp_pos.y)
        self.position = resp_pos

        self.state = EnemyState.IDLE

        self.mrlock.release()

    def on_move(self, player):
        """
        Move logic wrapper.

        Args:
            player (Player): ingame player.
        """

        self.mrlock.acquire()

        # move to random cell around or not move
        min_pos = Position(self.position.x - 1, self.position.y - 1)
        max_pos = Position(self.position.x + 1, self.position.y + 1)

        min_pos.clamp(self.min_resp_pos, self.max_resp_pos)
        max_pos.clamp(self.min_resp_pos, self.max_resp_pos)

        self.position.x = random.randint(min_pos.x, max_pos.x)
        self.position.y = random.randint(min_pos.y, max_pos.y)
        while self.position.x == player.position.x and \
                self.position.y == player.position.y:
            self.position.x = random.randint(min_pos.x, max_pos.x)
            self.position.y = random.randint(min_pos.y, max_pos.y)

        print(self.position)

        # print phrase
        max_rand = len(looking_phrases) - 1
        rand_phrase_idx = random.randint(0, max_rand)
        print(looking_phrases[rand_phrase_idx])

        self.state = EnemyState.IDLE

        self.mrlock.release()

    def on_idle(self, player):
        """
        Decider logic wrapper.
        In this state enemy decides what to do.

        Args:
            player (Player): ingame player.
        """
        self.mrlock.acquire()

        player_pos = player.position

        if abs(player_pos.x - self.position.x) <= 1 and \
           abs(player_pos.y - self.position.y) <= 1:
            # in range
            self.state = EnemyState.ATTACKING
        else:
            self.state = EnemyState.MOVING

        self.update(player)

        self.mrlock.release()

    def update(self, player):
        if self.state == EnemyState.ATTACKING:
            self.on_attack(player)
        elif self.state == EnemyState.MOVING:
            self.on_move(player)
        elif self.state == EnemyState.IDLE:
            self.on_idle(player)
        else:
            raise StateError(f'{self.state} is not supported in this context.',
                             [EnemyState.ATTACKING,
                              EnemyState.MOVING,
                              EnemyState.IDLE])
