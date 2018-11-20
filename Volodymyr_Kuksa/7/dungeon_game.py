from player import Player
from game_map import GameMap
from utils import query_player_input

POSSIBLE_MAP_SIZES = [str(i) for i in range(5, 21)]


class DungeonGame:

    def __init__(self):

        player_name = input('Enter your name: ')
        self.player = Player(player_name)

        map_size = query_player_input('Enter map size: ', POSSIBLE_MAP_SIZES)
        self.game_map = GameMap(map_size=int(map_size))
        print(self.game_map)

    def run_game(self):
        pass
