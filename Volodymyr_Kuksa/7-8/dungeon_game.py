import pickle
import logging
from player import Player, PLAYER_MOVES
from game_map import GameMap, GAME_CHARACTERS
from utils import query_player_input
import dungeon_game_decorators

FILE_NAME = 'save_file.dg'

LOAD_COMMAND = 'load'
SAVE_COMMAND = 'save'

POSSIBLE_MAP_SIZES = [str(i) for i in range(5, 21)]
VALID_RUNTIME_INPUTS = (*PLAYER_MOVES.keys(), SAVE_COMMAND)


class DungeonGame:

    @dungeon_game_decorators.log_decor
    @dungeon_game_decorators.debug_decor
    def __init__(self):
        """
        DungeonGame constructor.
        """
        player_input = query_player_input('Load last game (y/n)? ', ('y', 'n'))

        if player_input == 'y':

            self.game_map = GameMap()
            self.player = Player('')

            try:
                self.on_game_load()
            except FileNotFoundError as error:
                logging.error(error)
                logging.info('Save file not found, new game started.')
            else:
                return

        map_size = int(query_player_input('Enter map size: ', POSSIBLE_MAP_SIZES))
        self.game_map = GameMap(map_size=map_size)

        player_name = input('Enter your name: ')
        self.player = Player(player_name)
        self.player.randomize_position(map_size)

        while self.game_map.get_tile_character(*self.player.get_position()) != GAME_CHARACTERS['Empty']:
            self.player.randomize_position(map_size)

    @dungeon_game_decorators.log_decor
    @dungeon_game_decorators.debug_decor
    def run_game(self):
        """
        Game loop.
        """
        while self.player.is_alive() and not self.player.is_bag_full():

            player_input = query_player_input(f'\nEnter move {VALID_RUNTIME_INPUTS}: ', VALID_RUNTIME_INPUTS)

            if player_input == SAVE_COMMAND:

                self.on_game_save()
                continue

            position = self.player.calculate_new_position(player_input)

            try:
                self.game_map.get_tile_character(*position)
            except IndexError as error:
                logging.error(error)
                logging.info('That path is blocked!')
            else:
                self.player.set_position(*position)
                self.apply_tile_effects_to_player()
                self.game_map.mark_tile_as_visited(*position)

            self.print_game_state()

        self.on_game_end()

    @dungeon_game_decorators.log_decor
    @dungeon_game_decorators.debug_decor
    def on_game_end(self):
        """
        Output game results.
        """
        if not self.player.is_alive():
            logging.info('\nYou Lost(')
        else:
            logging.info('\nYou Won!')

        logging.info(self.game_map)

    @dungeon_game_decorators.log_decor
    @dungeon_game_decorators.debug_decor
    def on_game_save(self):
        """
        Save game to file.
        """
        data = [self.game_map, self.player.get_position(), self.player.character_name, self.player.hp, self.player.bag]

        with open(FILE_NAME, 'wb') as save_file:
            pickle.dump(data, save_file, protocol=3)

    @dungeon_game_decorators.log_decor
    @dungeon_game_decorators.debug_decor
    def on_game_load(self):
        """
        Load game from file.
        """
        with open(FILE_NAME, 'rb') as save_file:
            data = pickle.load(save_file)

        self.game_map = data[0]
        self.player.set_position(*data[1])
        self.player.character_name = data[2]
        self.player.hp = data[3]
        self.player.bag = data[4]

    @dungeon_game_decorators.log_decor
    @dungeon_game_decorators.debug_decor
    def apply_tile_effects_to_player(self):
        """
        Apply to player effects of the tile on which he currently stands on.
        """
        tile_character = self.game_map.get_tile_character(*self.player.get_position())

        if tile_character == GAME_CHARACTERS['Treasure']:

            logging.info('Treasure collected!')
            self.player.increment_bag()

        elif tile_character == GAME_CHARACTERS['Trap']:

            logging.info('Player damaged.')
            self.player.decrement_hp()

    @dungeon_game_decorators.log_decor
    @dungeon_game_decorators.debug_decor
    def print_game_state(self):

        logging.info(self.player)
        self.game_map.print_state_on_position(*self.player.get_position())
