import threading
import time


exitFlag = 0

from random import choice
from enemy import Enemy

class EnemyThread(threading.Thread):

    def __init__(self, threadID, name, enemy, map_size):

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
