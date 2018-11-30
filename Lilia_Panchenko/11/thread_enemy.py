import threading
import time

from random import choice
from enemy import Enemy


exitFlag = 0

class EnemyThread(threading.Thread):
    """
    Class to separate enemy from other game. To make enemy move independently from player's actions
    """

    def __init__(self, threadID, name, enemy, map_size):
        """
        Constructor for EnemyThread class
        """
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.enemy = enemy
        self.map_size = map_size
        print("ms", map_size)


    def run(self):
        while True:
            if exitFlag:
                threadName.exit()

            print("moved enemy", self.enemy.position)
            self.enemy.move(self.map_size)
            time.sleep(3)
