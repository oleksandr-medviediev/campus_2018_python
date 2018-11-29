from threading import Thread
from enemy import Enemy
from game_map import GameMap

class EnemyThread(Thread):
    def __init__(self, enemy, player, game_map, event):
        Thread.__init__(self)
        self.stopped = event
        self._map = game_map
        self._enemy = enemy
        self._player = player

    def run(self):
        while not self.stopped.wait(0.01):
            stepped_on_player = self._enemy.move(self._map)

            if stepped_on_player:

                self._player.apply_item(GameMap.ENEMY_SYMBOL)
