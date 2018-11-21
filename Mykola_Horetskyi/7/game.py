from random import randint, choice
from copy import deepcopy
from pickle import dump, load
from os.path import isfile
from game_logger import logger
from decorator import debug_decorator
from utils import Position, print_dictionary, input_number_from_boundaries
from trap import trap_legends, Trap
from dungeon_cell import treasure_cell, empty_cell, entrance_cell
from player import Player, proficiency_immunity, proficiencies
import dungeon_map
import text


MIN_MAP_WIDTH = 5
MAX_MAP_WIDTH = 50

MIN_MAP_HEIGHT = 1
MAX_MAP_HEIGHT= 50

default_health = 3
treasure_to_win = 3

trap_rarity = 0.2
treasure_rarity = 0.05


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

action_to_diraction = {
"w":"north",
"d":"east",
"s":"south",
"a":"west"
}

directions_dict= {"north":Position(0, 1),
             "east":Position(1,0),
             "south":Position(0, -1),
             "west":Position(-1, 0)}


@debug_decorator
def process_yes_no_input():
    """
    Processes input that shoul be either accept or decline

    return: (bool) True for accept, False for decline
    """
    user_input = input().lower()

    if user_input == "y" or user_input == "yes":
        return True

    elif user_input == "n" or user_input =="no":
        return False

    logger.info(text.wrong_y_n_input)

    user_input = input().lower()

    if user_input == "y" or user_input == "yes":
        return True

    return False


@debug_decorator
def init_new_game(player):
    """
    Initializes new games
    """
    logger.info(text.new_game_start)
    input()
    logger.info(text.administration)
    input()
    logger.info(text.enter_proficiency_prompt)
    user_input = input().lower()

    if user_input in proficiencies:
        player.proficiency = user_input
    else:
        player.proficiency = "none"

    logger.info(text.enter_dungeon_width_prompt)
    width = input_number_from_boundaries(MIN_MAP_WIDTH, MAX_MAP_WIDTH)

    logger.info(text.enter_dungeon_height_prompt)
    height = input_number_from_boundaries(MIN_MAP_HEIGHT, MAX_MAP_HEIGHT)

    size = width * height

    number_of_treasures = max (size * treasure_rarity, treasure_to_win)
    number_of_traps = min (size - number_of_treasures - 1, size * trap_rarity)

    traps = Trap.generate_traps(number_of_traps)

    starting_position = Position.generate_random_position(width, height)

    dmap = dungeon_map.DungeonMap()
    dmap.initialize(height, width, number_of_treasures, traps, starting_position)

    player.health = default_health
    player.bag = 0
    player.position = starting_position
    player.discovered_map.initialize_discovered_map(height, width,\
     starting_position)


    return player, dmap



@debug_decorator
def process_player_commands(player, dmap):
    """
    Process player commands.
    """
    logger.info(text.action_prompt)
    user_input = input().lower()

    if user_input == "cheat":
        map_to_print = deepcopy(dmap)
        map_to_print.assign_cell(player.position, "p")
        map_to_print.print_map()
        return player, dmap

    while not user_input in actions.keys() and not user_input in actions.values():
        logger.info(text.action_wrong)
        print_dictionary(actions)
        user_input = input().lower()

    if user_input in actions.keys():
        user_input = actions[user_input]

    if user_input in action_to_diraction.keys():
        user_input = action_to_diraction[user_input]

        move_position = player.position + directions_dict[user_input]

        if not dmap.is_position_in_map(move_position):
            logger.info(choice(text.no_passage))
        else:
            player.position = move_position
            player, dmap =  process_room(player, dmap)

    elif user_input == "m":
        map_to_print = deepcopy(player.discovered_map)
        map_to_print.assign_cell(player.position, "p")
        map_to_print.print_map()

    elif user_input == "lg":
        print_dictionary(dungeon_map.discovery_dict)

    elif user_input == "h":
        logger.info(text.health_check)
        logger.info(text.health_description[player.health])

    elif user_input == "b":
        logger.info(text.treasure_check.format(player.bag))

    elif user_input == "ld":
        if isfile("./{}.pickle".format(player.name)):
            player, dmap = load_game(player.name)
            logger.info(choice(text.load_ingame))
        else:
            logger.info(choice(text.on_no_save_file))

    elif user_input == "sv":
        logger.info(choice(text.on_save_1))
        save_game(player, dmap)
        logger.info(choice(text.on_save_2))

    elif user_input == "e":
        logger.info(choice(text.lets_end_this))
        while player.is_alive():
            player.take_damage()

    return player, dmap


@debug_decorator
def process_room(player, dmap):
    """
    Resolves possible trap encounters and prints feedback.
    """
    logger.info(text.tell_position.format(player.position.x, player.position.y))

    current_cell = dmap.cell(player.position)

    if not current_cell:
        logger.debug("processing non-existant room!")
        return player, dmap

    logger.debug("entered cell {}".format(current_cell))

    current_cell = dungeon_map.cells_dict[current_cell]

    logger.info(choice(current_cell.description))
    input()

    if current_cell.legend == treasure_cell.legend:
        player.bag += 1

    elif current_cell.legend in trap_legends:
        if player.proficiency in current_cell.fight_description.keys():
            logger.info(choice(current_cell.fight_description[player.proficiency]))
        else:
            logger.info(choice(current_cell.fight_description["other"]))
        input()

        is_damaged = proficiency_immunity[player.proficiency] != current_cell.trap_type

        if is_damaged:
            player.take_damage()

        if player.is_alive():
            if player.proficiency in current_cell.survive_description.keys():
                logger.info(choice(current_cell.survive_description[player.proficiency]))
            else:
                logger.info(choice(current_cell.survive_description["other"]))
            input()

        else:
            if player.proficiency in current_cell.defeat_description.keys():
                logger.info(choice(current_cell.defeat_description[player.proficiency]))
            else:
                logger.info(choice(current_cell.defeat_description["other"]))
            input()
            return player, dmap

    if dmap.cell(player.position) != entrance_cell.legend:
        dmap.assign_cell(player.position, empty_cell.legend)

    is_trap_nearby = dmap.check_for_adjacent_types(player.position, trap_legends)
    is_treasure_nearby = dmap.check_for_adjacent_types(player.position, treasure_cell.legend)

    if is_trap_nearby and not is_treasure_nearby:
        logger.info(choice(text.adjacent_trap))
        player.discovered_map.assign_cell(player.position, dungeon_map.discovery_dict["trap near"])
        input()
    elif not is_trap_nearby and is_treasure_nearby:
        logger.info(choice(text.adjacent_treasure))
        player.discovered_map.assign_cell(player.position, dungeon_map.discovery_dict["treasure near"])
        input()
    elif is_trap_nearby and is_treasure_nearby:
        logger.info(choice(text.adjacent_trap))
        logger.info(choice(text.also))
        logger.info(choice(text.adjacent_treasure))
        player.discovered_map.assign_cell(player.position, dungeon_map.discovery_dict["treasure and trap near"])
        input
    else:
        player.discovered_map.assign_cell(player.position, dungeon_map.discovery_dict["empty"])

    return player, dmap



@debug_decorator
def save_game(player, dmap):
    """
    Saves current game.
    """
    current_data = (player, dmap)
    save_file_name = "".join([player.name, ".pickle"])

    logger.debug("saving to {}".format(save_file_name))

    with open(save_file_name, 'wb') as save_file:
        dump(current_data, save_file)


@debug_decorator
def load_game(name):
    """
    Loading game data from file.
    """

    save_file_name = "".join([name, ".pickle"])

    logger.debug("loading from {}".format(save_file_name))

    with open(save_file_name, 'rb') as save_file:
        game_data = load(save_file)

    return game_data


@debug_decorator
def game_loop():
    """
    Game loop.
    """

    while True:

        player = Player()

        logger.info(text.enter_name_prompt)

        name = input()
        name = list(filter(lambda c: c.isalpha(), name))
        name = "".join(name)

        if not name:
            name = "Anonymous"

        player.name = name

        is_load_game = False

        if isfile("./{}.pickle".format(player.name)):
            logger.info(text.load_game_on_start_prompt)
            is_load_game = process_yes_no_input()

        if is_load_game:
            player, dmap = load_game(player.name)
            logger.info(choice(text.load_on_start))
        else:
            player, dmap = init_new_game(player)

        player, dmap = process_room(player, dmap)

        while player.is_alive() and player.bag < treasure_to_win:

            player, dmap = process_player_commands(player, dmap)


        if player.is_alive():
            logger.info(choice(text.won))
            logger.debug("player won")
        else:
            logger.info(choice(text.lost))
            logger.debug("player lost")

        input()

        logger.info(text.end_map_description)
        dmap.print_map()
        print_dictionary(dungeon_map.cells_dict_explained)
        input()

        logger.info(text.play_again_prompt)

        is_play_again = process_yes_no_input()

        if not is_play_again:
            logger.debug("user exits game")
            break

        logger.debug("user decides to play again")
