from random import randint, choice
from copy import deepcopy
from pickle import dump, load, UnpicklingError
from os.path import isfile
from game_logger import logger
from decorator import debug_decorator, thread_lock_decorator
from utils import Position, print_dictionary, input_number_from_boundaries,\
process_yes_no_input
from trap import trap_legends, Trap
from dungeon_cell import treasure_cell, empty_cell, entrance_cell
from player import Player
from dungeon_map import DungeonMap
from custom_errors import NotValidSaveFileError
from enemy import Enemy, enemies_list
import hashlib
import threading
import text
import time

class DungeonGame:

    MIN_MAP_WIDTH = 5
    MAX_MAP_WIDTH = 50

    MIN_MAP_HEIGHT = 1
    MAX_MAP_HEIGHT= 50

    default_health = 3
    treasure_to_win = 3

    trap_rarity = 0.2
    treasure_rarity = 0.05

    enemy_turn_time = 3.0


    actions = {"go north":'w',
             "go east":'d',
             "go south":'s',
             "go west":'a',
             "check health":"h",
             "check bag":"b",
             "view map":'m',
             "view map legend":"lg",
             "save":'sv',
             "load":'ld',
             "exit":"e"}

    actions_cheat = {"go north":'w',
             "go east":'d',
             "go south":'s',
             "go west":'a',
             "check health":"h",
             "check bag":"b",
             "view map":'m',
             "view map legend":"lg",
             "save":'sv',
             "load":'ld',
             "exit":"e",
             "cheat view map":"cheat"}

    action_to_position = {
    "w":Position(0, 1),
    "d":Position(1,0),
    "s":Position(0, -1),
    "a":Position(-1, 0)
    }

    position_directions = [Position(0, 1), Position(1,0), Position(0, -1), Position(-1, 0)]

    dmap = DungeonMap()
    player = Player()
    enemy = choice(enemies_list)


    @debug_decorator
    def __init__(self):
        pass


    @debug_decorator
    def is_game_ended(self):
        """
        Checks if one of conditions for ending game is met:
        currently they are:
        1) Player collects treasure_to_win number of treasures.
        2) Player's health reaches zero.
        """
        is_game_over = (DungeonGame.player.bag >= DungeonGame.treasure_to_win
        or DungeonGame.player.health <= 0)

        return is_game_over


    @debug_decorator
    def init_new_game(self):
        """
        Initializes new games
        """
        logger.info(text.new_game_start)
        input()
        logger.info(text.administration)
        input()
        logger.info(text.enter_proficiency_prompt)
        user_input = input().lower()

        if user_input in DungeonGame.player.proficiencies:
            DungeonGame.player.proficiency = user_input
        else:
            DungeonGame.player.proficiency = "none"

        logger.info(text.enter_dungeon_width_prompt)
        width = input_number_from_boundaries(DungeonGame.MIN_MAP_WIDTH,\
         DungeonGame.MAX_MAP_WIDTH)

        logger.info(text.enter_dungeon_height_prompt)
        height = input_number_from_boundaries(DungeonGame.MIN_MAP_HEIGHT,\
         DungeonGame.MAX_MAP_HEIGHT)

        size = width * height

        number_of_treasures = max (size * DungeonGame.treasure_rarity,\
         DungeonGame.treasure_to_win)
        number_of_traps = min (size - number_of_treasures - 1, size * DungeonGame.trap_rarity)

        traps = Trap.generate_traps(number_of_traps)

        starting_position = Position.generate_random_position(width, height)

        DungeonGame.dmap.initialize(height, width, number_of_treasures, traps, starting_position)

        DungeonGame.player.health = DungeonGame.default_health
        DungeonGame.player.bag = 0
        DungeonGame.player.position = starting_position
        DungeonGame.player.discovered_map.initialize_discovered_map(height, width,\
         starting_position)

        self.respawn_enemy()


    @debug_decorator
    def process_player_commands(self):
        """
        Process player commands.
        """
        logger.info(text.action_prompt)
        user_input = input().lower()

        while (not user_input in DungeonGame.actions_cheat.keys()
         and not user_input in DungeonGame.actions_cheat.values()):
            logger.info(text.action_wrong)
            print_dictionary(DungeonGame.actions)
            user_input = input().lower()

        if user_input in DungeonGame.actions_cheat.keys():
            user_input = DungeonGame.actions_cheat[user_input]

        if user_input in DungeonGame.action_to_position.keys():
            move_position = DungeonGame.player.position + DungeonGame.action_to_position[user_input]

            if not DungeonGame.dmap.is_position_in_map(move_position):
                logger.info(choice(text.no_passage))
            else:
                DungeonGame.player.position = move_position
                self.process_room()

        elif user_input == "m":
            map_to_print = deepcopy(DungeonGame.player.discovered_map)
            map_to_print.assign_cell(DungeonGame.player.position, "p")
            map_to_print.print_map()

        elif user_input == "lg":
            print_dictionary(DungeonMap.discovery_dict)

        elif user_input == "h":
            logger.info(text.health_check)
            logger.info(text.health_description[DungeonGame.player.health])

        elif user_input == "b":
            logger.info(text.treasure_check.format(DungeonGame.player.bag))

        elif user_input == "ld":
            if isfile("./{}.pickle".format(DungeonGame.player.name)):
                self.load_game()
                logger.info(choice(text.load_ingame))
            else:
                logger.info(choice(text.on_no_save_file))

        elif user_input == "sv":
            logger.info(choice(text.on_save_1))
            self.save_game()
            logger.info(choice(text.on_save_2))

        elif user_input == "e":
            logger.info(choice(text.lets_end_this))
            while DungeonGame.player.is_alive():
                DungeonGame.player.take_damage()

        elif user_input == "cheat":
            map_to_print = deepcopy(DungeonGame.dmap)
            map_to_print.assign_cell(DungeonGame.player.position, "p")
            map_to_print.print_map()


    @debug_decorator
    def process_room(self):
        """
        Resolves possible trap encounters and prints feedback.
        """
        logger.info(text.tell_position.format(DungeonGame.player.position.x,\
         DungeonGame.player.position.y))

        current_cell = DungeonGame.dmap.cell(DungeonGame.player.position)

        if not current_cell:
            logger.debug("processing non-existant room!")
            return

        logger.debug("entered cell {}".format(current_cell))

        if DungeonGame.enemy.position == DungeonGame.player.position:

            logger.debug("enemy finds player")
            self.process_hostile_encounter(DungeonGame.enemy)
            self.respawn_enemy()

            if not self.player.is_alive():
                return

        current_cell = DungeonMap.cells_dict[current_cell]

        if current_cell.legend in trap_legends:
            self.process_hostile_encounter(current_cell)

            if not self.player.is_alive():
                return
        else:
            logger.info(choice(current_cell.encounter_description))

            if current_cell.legend == treasure_cell.legend:
                DungeonGame.player.bag += 1

        if DungeonGame.dmap.cell(DungeonGame.player.position) != entrance_cell.legend:
            DungeonGame.dmap.assign_cell(DungeonGame.player.position, empty_cell.legend)

        is_trap_nearby = DungeonGame.dmap.check_for_adjacent_types(DungeonGame.player.position,\
         trap_legends)

        is_treasure_nearby = DungeonGame.dmap.check_for_adjacent_types(DungeonGame.player.position,\
         treasure_cell.legend)

        if is_trap_nearby and not is_treasure_nearby:
            logger.info(choice(text.adjacent_trap))
            DungeonGame.player.discovered_map.assign_cell(DungeonGame.player.position,\
             DungeonMap.discovery_dict["trap near"])

        elif not is_trap_nearby and is_treasure_nearby:
            logger.info(choice(text.adjacent_treasure))
            DungeonGame.player.discovered_map.assign_cell(DungeonGame.player.position,\
             DungeonMap.discovery_dict["treasure near"])

        elif is_trap_nearby and is_treasure_nearby:
            logger.info(choice(text.adjacent_trap))
            logger.info(choice(text.also))
            logger.info(choice(text.adjacent_treasure))
            DungeonGame.player.discovered_map.assign_cell(DungeonGame.player.position,\
             DungeonMap.discovery_dict["treasure and trap near"])

        elif DungeonGame.dmap.cell(DungeonGame.player.position) == entrance_cell.legend:
            DungeonGame.player.discovered_map.assign_cell(DungeonGame.player.position,\
            DungeonMap.discovery_dict["entrance"])
        else:
            DungeonGame.player.discovered_map.assign_cell(DungeonGame.player.position,\
             DungeonMap.discovery_dict["empty"])


    @debug_decorator
    def save_game(self):
        """
        Saves current game.
        """
        hash = hashlib.md5(str(DungeonGame.player.name).encode());
        current_data = (str(hash), DungeonGame.player, DungeonGame.enemy, DungeonGame.dmap)
        save_file_name = "".join([DungeonGame.player.name, ".pickle"])

        logger.debug("saving to {}".format(save_file_name))

        with open(save_file_name, 'wb') as save_file:
            dump(current_data, save_file)


    @debug_decorator
    def load_game(self):
        """
        Loading game data from file.

        returns True on succsessful load, False on failed
        """


        save_file_name = "".join([DungeonGame.player.name, ".pickle"])

        logger.debug("loading from {}".format(save_file_name))

        with open(save_file_name, 'rb') as save_file:
            try:
                game_data = load(save_file)

            except UnpicklingError as error:
                try:
                    raise NotValidSaveFileError("UnpicklingError:{}".\
                    format(str(error)), save_file_name)
                except NotValidSaveFileError as custom_error:
                    logger.debug(str(custom_error))
                    return False

        hash = hashlib.md5(str(DungeonGame.player.name).encode());

        if str(hash) == game_data[0]:
            _, DungeonGame.player, DungeonGame.enemy, DungeonGame.dmap = game_data
            return True

        else:
            try:
                raise NotValidSaveFileError("Save file hash not verified.", save_file_name)
            except NotValidSaveFileError as custom_error:
                logger.debug(str(custom_error))
                return False


    @debug_decorator
    def respawn_enemy(self):
        """
        Respawns enemy at random not occupied by Player cell.
        """

        DungeonMap.enemy = choice(enemies_list)

        enemy_position = Position.generate_random_position(DungeonGame.dmap.width,\
        DungeonGame.dmap.height)

        while enemy_position == DungeonGame.player.position:
            enemy_position = Position.generate_random_position(DungeonGame.dmap.width,\
            DungeonGame.dmap.height)

        DungeonMap.enemy.position = enemy_position

        logger.debug("enemy spawned at {},{}".format(DungeonGame.enemy.position.x,\
        DungeonGame.enemy.position.y))


    @debug_decorator
    def process_enemy_turn(self):
        """
        Moves enemy to random ajucent cell
        """
        new_position = DungeonGame.enemy.position + choice(DungeonGame.position_directions)

        while not self.dmap.is_position_in_map(new_position):
            new_position = DungeonGame.enemy.position + choice(DungeonGame.position_directions)

        DungeonGame.enemy.position = new_position

        logger.debug("enemy moves to {},{}".format(DungeonGame.enemy.position.x,\
        DungeonGame.enemy.position.y))

        if DungeonGame.enemy.position == DungeonGame.player.position:
            logger.debug("enemy finds player")
            self.process_hostile_encounter(DungeonGame.enemy)
            self.respawn_enemy()


    @debug_decorator
    def process_enemy(self):
        """
        Process enemy turns, which are made in enemy_turn_time intervals.
        """
        time_of_last_turn = time.time()

        while not self.is_game_ended():

            current_time = time.time()

            if current_time - time_of_last_turn > DungeonGame.enemy_turn_time:
                self.process_enemy_turn()
                time_of_last_turn = current_time


    @debug_decorator
    @thread_lock_decorator
    def process_hostile_encounter(self, hostile_entity):
        """
        Resolves Player's encounter with Trap or Enemy.
        """
        logger.info(choice(hostile_entity.encounter_description))

        if DungeonGame.player.proficiency in hostile_entity.fight_description.keys():
            logger.info(choice(hostile_entity.fight_description[DungeonGame.player.proficiency]))
        else:
            logger.info(choice(hostile_entity.fight_description["other"]))

        is_damaged = DungeonGame.player.proficiency_immunity[DungeonGame.player.proficiency]\
         != hostile_entity.enemy_type

        if is_damaged:
            DungeonGame.player.take_damage()

        if DungeonGame.player.is_alive():
            if DungeonGame.player.proficiency in hostile_entity.survive_description.keys():
                logger.info(choice(hostile_entity.survive_description[DungeonGame.player.proficiency]))
            else:
                logger.info(choice(hostile_entity.survive_description["other"]))

        else:
            if DungeonGame.player.proficiency in hostile_entity.defeat_description.keys():
                logger.info(choice(hostile_entity.defeat_description[DungeonGame.player.proficiency]))
            else:
                logger.info(choice(hostile_entity.defeat_description["other"]))


    @debug_decorator
    def game_loop(self):
        """
        Game loop.
        """

        while True:

            logger.info(text.enter_name_prompt)

            name = input()
            name = list(filter(lambda c: c.isalpha(), name))
            name = "".join(name)

            if not name:
                name = "Anonymous"

            DungeonGame.player.name = name

            is_load_game = False

            if isfile("./{}.pickle".format(DungeonGame.player.name)):
                logger.info(text.load_game_on_start_prompt)
                is_load_game = process_yes_no_input()

            if is_load_game:
                self.load_game()
                logger.info(choice(text.load_on_start))
            else:
                self.init_new_game()

            threading.Thread(target=self.process_enemy).start()

            self.process_room()

            while not self.is_game_ended():
                self.process_player_commands()


            if DungeonGame.player.is_alive():
                logger.info(choice(text.won))
                logger.debug("DungeonGame.player won")
            else:
                logger.info(choice(text.lost))
                logger.debug("DungeonGame.player lost")

            input()

            logger.info(text.end_map_description)
            map_to_print = deepcopy(DungeonGame.dmap)
            map_to_print.assign_cell(DungeonGame.player.position, "p")
            map_to_print.print_map()
            print_dictionary(DungeonMap.cells_dict_explained)
            input()

            logger.info(text.play_again_prompt)

            is_play_again = process_yes_no_input()

            if not is_play_again:
                logger.debug("user exits game")
                break

            logger.debug("user decides to play again")
