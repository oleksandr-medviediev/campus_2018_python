from threading import Event
from threading import Thread

class GameLoop:
    def __init__(self):
        self.game_over_event = Event()