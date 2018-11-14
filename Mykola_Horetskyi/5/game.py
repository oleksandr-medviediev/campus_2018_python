import random
import map_generator
import text
import copy
import pickle
import os.path
from game_logger import logger

SAVE_FILE_NAME = "dungeon_game_save.pickle"

MIN_MAP_SIZE = 5
MAX_MAP_SIZE = 50

actions = {"go north":'w',
         "go east":'d',
         "go south":'s',
         "go west":'a',
         "view map":'m',
         "save":'sv',
         "load":'ld'}

map_sizes = {"smallest":5,
              "small":10,
              "medium":20,
              "big":30,
              "very big":40,
              "biggest":50}

directions= {"north":(0, 1),
             "east":(1,0),
             "south":(0, -1),
             "west":(-1, 0)}

direction_opposites = {"north":"south",
             "east":"west",
             "south":"north",
             "west":"east"}

def input_map_size():
    """
    Prompts player to input map size.

    Returns:
        map_size (int)
    """

    logger.info(text.dungeon_size_promt)
    logger.debug("expecting map size input from user")
    user_input = input().lower()

    map_size = None

    while not map_size:

        if (user_input.isdigit()
        and int(user_input) >= MIN_MAP_SIZE
        and int(user_input) <= MAX_MAP_SIZE):
            map_size = int(user_input)

        else:
            for key in map_sizes.keys():
                if user_input.lower() == key:
                    map_size = map_sizes[key]

        if not map_size:
            logger.debug("incorrect map size input from user")
            logger.info(text.dungeon_size_hint)
            logger.debug("expecting map size input from user")
            user_input = input()

    return map_size


def init_game():
    """
    Initializes game, creating all needed variables.

    Returns:
    dmap - list of lists representing dungeon map
    discovered_map - parts of dungeon map discovered by player
    start_x (int) x-coordinate of player start position
    start_y (int) y-coordinate of player start position
    treasure_number (int) number of treasures in dungeon
    """

    logger.debug("starting new game initialization")

    map_size = input_map_size()

    start_x = random.randint(0, map_size - 1)
    start_y = random.randint(0, map_size - 1)

    trap_number = map_size * map_size // 10

    treasure_number = map_size * map_size // 20

    dmap = map_generator.generate_dungeon_map(map_size, map_size,
                                              start_x, start_y,
                                              trap_number, treasure_number)

    discovered_map = [[map_generator.tiles['unknown'] for i in range(map_size)]
                      for j in range(map_size)]

    return dmap, discovered_map, start_x, start_y, treasure_number


def check_for_adjacent_type(dmap,pos_x, pos_y, tile_type):
    """
    Checks whether there are any tile of specified type in adjucent tiles

    Returns:
        (bool) True if 1 or more specified type in adjucent tiles,
        False otherwise
    """

    logger.debug("checking adjacent rooms of {},{} for {} tiles".format(pos_x, pos_y, tile_type))

    is_adjacent = False

    for direction in directions.values():
        x = pos_x + direction[0]
        y = pos_y + direction[1]

        if (x > 0 and y > 0 and x < len(dmap) and y < len(dmap[0])
        and dmap[x][y] == map_generator.tiles[tile_type]):
            is_adjacent = True
            break

    logger.debug("adjacent rooms checked with result: {}".format(is_adjacent))
    return is_adjacent



def enter_room(dmap, discovered_map, pos_x, pos_y, direction, treasure_number,
               treasure_collected, is_player_alive):
    """
    Process entering the room.
    """

    logger.info(text.enter_room.format(direction))
    logger.info(text.tell_position.format(pos_x, pos_y))
    logger.debug("player enters {},{}".format(pos_x, pos_y))

    if dmap[pos_x][pos_y] == map_generator.tiles['empty']:
        logger.info(random.choice(text.no_encounter))
        logger.debug("player encounters nothing at {},{}".format(pos_x, pos_y))


    elif dmap[pos_x][pos_y] == map_generator.tiles['trap']:
        logger.info(random.choice(text.trap_encounter))
        logger.debug("player encounters trap at {},{}".format(pos_x, pos_y))
        is_player_alive = False

    elif dmap[pos_x][pos_y] == map_generator.tiles['treasure']:
        logger.info(random.choice(text.treasure_encounter))
        logger.debug("player encounters treasure at {},{}".format(pos_x, pos_y))
        treasure_number -= 1
        treasure_collected +=1
        if treasure_number == 0:
            logger.debug("player collects final treasure at {},{}".format(pos_x, pos_y))

    if not is_player_alive:
        logger.debug("player dies at {},{}".format(pos_x, pos_y))
        return dmap, discovered_map, pos_x, pos_y, treasure_number, treasure_collected, is_player_alive

    is_adjustant_traps = check_for_adjacent_type(dmap,pos_x, pos_y, 'trap')
    is_adjustant_treasure = check_for_adjacent_type(dmap,pos_x, pos_y, 'treasure')

    if is_adjustant_traps and not is_adjustant_treasure:
        logger.info(random.choice(text.adjacent_trap))
        discovered_map[pos_x][pos_y] = map_generator.tiles['bordering trap']

    elif not is_adjustant_traps and is_adjustant_treasure:
        logger.info(random.choice(text.adjacent_treasure))
        discovered_map[pos_x][pos_y] = map_generator.tiles['bordering treasure']

    elif is_adjustant_treasure and is_adjustant_traps:
        discovered_map[pos_x][pos_y] = map_generator.tiles['bordering treasure and trap']
        logger.info(random.choice(text.adjacent_trap))
        logger.info(random.choice(text.also))
        logger.info(random.choice(text.adjacent_treasure))

    else:
            discovered_map[pos_x][pos_y] = map_generator.tiles['empty']

    return dmap, discovered_map, pos_x, pos_y, treasure_number, treasure_collected, is_player_alive


def process_player_commands(dmap, discovered_map, pos_x, pos_y,
                            treasure_number, treasure_collected,
                            is_player_alive):
    """
    Process player commands.
    """

    logger.info(text.action_prompt)
    user_input = input().lower()

    while not user_input in actions.keys() and not user_input in actions.values():
        logger.info(text.action_wrong)
        logger.debug("user enters incorrect input")
        user_input = input().lower()

    if user_input == 'view map' or  user_input == actions['view map']:

        logger.debug("player views map")
        printed_map = copy.deepcopy(discovered_map)
        printed_map[pos_x][pos_y] = map_generator.tiles['player']
        map_generator.print_dungeon_map(printed_map)
        logger.info(text.legend_prompt)
        user_input = input().lower()

        if user_input == 'l':
            logger.debug("player views legend")
            input(text.legend)

    elif user_input =='save' or user_input == actions['save']:
        logger.debug("user attempts save game")
        save_game(dmap, discovered_map, pos_x, pos_y, treasure_collected)
        logger.info(random.choice(text.fall_asleep_1))
        logger.info(random.choice(text.fall_asleep_2))

    elif user_input =='load' or user_input == actions['load']:
        logger.debug("user attempts load game")

        if os.path.isfile("./{}".format(SAVE_FILE_NAME)):

            dmap, discovered_map, pos_x, pos_y,\
            treasure_collected = load_game()

            logger.info(random.choice(text.load_game_ingame))

            dmap, discovered_map, pos_x, pos_y, treasure_number,\
            treasure_collected, is_player_alive = \
                enter_room(dmap, discovered_map, pos_x, pos_y,
                random.choice(text.enter_room_wake_up), treasure_number,
                treasure_collected, is_player_alive)
        else:
            logger.debug("no save file exist to load")
            logger.info(random.choice(text.no_save_file_ingame))

    else:

        for direction in directions.keys():

            if (" ".join(['go', direction]) == user_input
                or actions["".join(['go ', direction])] == user_input):
                logger.debug("player attemots to go {} to".format(direction,
                                      pos_x + directions[direction][0],
                                      pos_y + directions[direction][1]))

                if map_generator.is_position_in_map(dmap,
                                      pos_x + directions[direction][0],
                                      pos_y + directions[direction][1]):

                    pos_x += directions[direction][0]
                    pos_y += directions[direction][1]


                    dmap, discovered_map, pos_x, pos_y, treasure_number,\
                    treasure_collected, is_player_alive = \
                               enter_room(dmap, discovered_map, pos_x, pos_y, direction_opposites[direction],
                               treasure_number, treasure_collected, is_player_alive)

                else:
                    logger.info(random.choice(text.no_passage))

                    logger.debug("player can't go {} to".format(direction,
                                      pos_x + directions[direction][0],
                                      pos_y + directions[direction][1]))

                break

    return dmap, discovered_map, pos_x, pos_y, treasure_number, treasure_collected, is_player_alive


def save_game(dmap, discovered_map, pos_x, pos_y, treasure_collected):
    """
    Saves current game data.
    """

    logger.debug("saving current game")

    current_data = (dmap, discovered_map, pos_x, pos_y, treasure_collected)

    with open(SAVE_FILE_NAME, 'wb') as dungeon_save_file:
        pickle.dump(current_data, dungeon_save_file)

    logger.debug("game is saved in{}".format(SAVE_FILE_NAME))


def load_game():
    """
    Loading game data from file.
    """

    logger.debug("loading game")

    with open(SAVE_FILE_NAME, 'rb') as dungeon_save_file:
        game_data = pickle.load(dungeon_save_file)

    logger.debug("game is loaded from{}".format(SAVE_FILE_NAME))

    return game_data


def game_loop():
    """
    Game loop.
    """

    while True:

        is_game_started = False

        is_player_alive = True
        treasure_collected = 0

        if os.path.isfile("./{}".format(SAVE_FILE_NAME)):

            logger.info(text.load_or_new_game_prompt)
            user_input = input().lower()

            if (user_input == "load"):

                dmap, discovered_map, pos_x, pos_y,\
                treasure_collected = load_game()

                treasure_number = map_generator.count_tiles_of_type(dmap,
                'treasure');

                is_game_started = True

                logger.info(random.choice(text.load_game_start))

                input()

                dmap, discovered_map, pos_x, pos_y, treasure_number,\
                treasure_collected, is_player_alive= \
                    enter_room(dmap, discovered_map, pos_x, pos_y,
                    random.choice(text.enter_room_wake_up), treasure_number,
                    treasure_collected, is_player_alive)

        if not is_game_started:

            logger.info(text.start)
            input()
            dmap, discovered_map, pos_x, pos_y, treasure_number = init_game()
            logger.debug("new game initialized")
            total_treasure = treasure_number

            logger.info(random.choice(text.go_to_dungeon))
            input()
            logger.info(random.choice(text.enter_dungeon))
            input()

            dmap, discovered_map, pos_x, pos_y, treasure_number,\
            treasure_collected, is_player_alive= \
                enter_room(dmap, discovered_map, pos_x, pos_y, text.entrance, treasure_number,
                treasure_collected, is_player_alive)

        while is_player_alive and treasure_number != 0:

            dmap, discovered_map, pos_x, pos_y, treasure_number,\
            treasure_collected, is_player_alive = \
                process_player_commands(dmap, discovered_map, pos_x, pos_y,
                treasure_number, treasure_collected, is_player_alive)

        input()

        if is_player_alive:
            logger.info(random.choice(text.won))
            logger.debug("player won")
        else:
            logger.info(random.choice(text.lost))
            logger.debug("player lost")

            logger.info(text.game_statistics.format(*[treasure_collected,
            treasure_collected + treasure_number]))

        input()

        map_generator.print_dungeon_map(dmap)
        logger.info(text.end_map_description)

        input()

        logger.info(text.play_again_prompt)
        logger.debug("expecting play again confirmation input from user")
        user_input = input().lower()

        if user_input == 'y' or user_input == 'yes':
            logger.debug("user decides to play again")
            continue
        elif user_input == 'n' or user_input == 'no':
            logger.debug("user decides not to play again")
            break

        logger.info(text.play_again_hint)
        logger.debug("incorrect input from user")
        logger.debug("expecting play again confirmation input from user")
        user_input = input().lower()

        if user_input != 'y' and user_input != 'yes':
            logger.debug("user decides not to play again")
            break

        logger.debug("user decides to play again")
