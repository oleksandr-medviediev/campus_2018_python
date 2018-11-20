from player import Player, PLAYER_MOVES
from game_map import GameMap, GAME_CHARACTERS
from utils import query_player_input

POSSIBLE_MAP_SIZES = [str(i) for i in range(5, 21)]


class DungeonGame:

    def __init__(self):
        """
        DungeonGame constructor.
        """
        map_size = int(query_player_input('Enter map size: ', POSSIBLE_MAP_SIZES))
        self.game_map = GameMap(map_size=map_size)

        player_name = input('Enter your name: ')
        self.player = Player(player_name)
        self.player.randomize_position(map_size)

        while self.game_map.get_tile_character(*self.player.get_position()) != GAME_CHARACTERS['Empty']:
            self.player.randomize_position(map_size)

    def run_game(self):
        """
        Game loop.
        """
        while self.player.is_alive() and not self.player.is_bag_full():

            player_input = query_player_input(f'Enter move {PLAYER_MOVES.keys()}: ', tuple(PLAYER_MOVES.keys()))
            position = self.player.calculate_new_position(player_input)

            if self.game_map.is_valid_position(*position):
                
                self.player.set_position(*position)
                self.apply_tile_effects_to_player()
                self.game_map.mark_tile_as_visited(*position)

        if not self.player.is_alive():
            print('You Lost(')
        else:
            print('You Won!')

        print(self.game_map)

    def apply_tile_effects_to_player(self):
        """
        Apply to player effects of the tile on which he currently stands on.
        """
        tile_character = self.game_map.get_tile_character(*self.player.get_position())

        if tile_character == GAME_CHARACTERS['Treasure']:
            self.player.increment_bag()
        elif tile_character == GAME_CHARACTERS['Trap']:
            self.player.decrement_hp()
