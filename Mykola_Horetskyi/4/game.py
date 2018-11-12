import random
import map_generator
import text
import copy


MIN_MAP_SIZE = 5
MAX_MAP_SIZE = 50

actions = {"go north":'w',
         "go east":'d',
         "go south":'s',
         "go west":'a',
         "view map":'m'}

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

    user_input = input(text.dungeon_size_promt).lower()

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
            user_input = input(text.dungeon_size_hint)
    
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

    for direction in directions.values():
        x = pos_x + direction[0]
        y = pos_y + direction[1]

        if (x > 0 and y > 0 and x < len(dmap) and y < len(dmap[0])
        and dmap[x][y] == map_generator.tiles[tile_type]):
            return True

    return False
    
    

def enter_room(dmap, discovered_map, pos_x, pos_y, direction, treasure_number,
               is_player_alive, is_treasure_collected):
    """
    Process entering the room.
    """

    print(text.enter_room, direction, '.')
    print("You are at position", str(pos_x), ", ", str(pos_y))

    if dmap[pos_x][pos_y] == map_generator.tiles['empty']:
        print(random.choice(text.no_encounter))
        
    elif dmap[pos_x][pos_y] == map_generator.tiles['trap']:
        print(random.choice(text.trap_encounter))
        is_player_alive = False
        
    elif dmap[pos_x][pos_y] == map_generator.tiles['treasure']:
        print(random.choice(text.treasure_encounter))
        treasure_number -= 1
        if treasure_number == 0:
            is_treasure_collected = True

    if not is_player_alive:
        return dmap, discovered_map, pos_x, pos_y, treasure_number, is_player_alive, is_treasure_collected
    
    is_adjustant_traps = check_for_adjacent_type(dmap,pos_x, pos_y, 'trap')
    is_adjustant_treasure = check_for_adjacent_type(dmap,pos_x, pos_y, 'treasure')

    if discovered_map[pos_x][pos_y] == map_generator.tiles['unknown']:
        
        if is_adjustant_traps and not is_adjustant_treasure:
            print(random.choice(text.adjacent_trap))
            discovered_map[pos_x][pos_y] = map_generator.tiles['bordering trap']

        elif not is_adjustant_traps and is_adjustant_treasure:
            print(random.choice(text.adjacent_treasure))
            discovered_map[pos_x][pos_y] = map_generator.tiles['bordering treasure']

        elif is_adjustant_treasure and is_adjustant_traps:
            discovered_map[pos_x][pos_y] = map_generator.tiles['bordering treasure and trap']
            print(random.choice(text.adjacent_trap))
            print(random.choice(text.also))
            print(random.choice(text.adjacent_treasure))
            
        else:
            discovered_map[pos_x][pos_y] = map_generator.tiles['empty']

    return dmap, discovered_map, pos_x, pos_y, treasure_number, is_player_alive, is_treasure_collected


def process_player_commands(dmap, discovered_map, pos_x, pos_y,
                            treasure_number, is_player_alive,
                            is_treasure_collected):
    """
    Process player commands.
    """

    user_input = input(text.action_prompt).lower()

    while not user_input in actions.keys() and not user_input in actions.values():
        user_input = input(text.action_wrong).lower()
    
    if user_input == 'view map' or  user_input == actions['view map']:
        
        printed_map = copy.deepcopy(discovered_map)
        printed_map[pos_x][pos_y] = map_generator.tiles['player']
        map_generator.print_dungeon_map(printed_map)
        user_input = input(text.legend_prompt).lower()
        
        if user_input == 'l':
            input(text.legend)

    else:
        
        for direction in directions.keys():
        
            if (" ".join(['go', direction]) == user_input
                or actions["".join(['go ', direction])] == user_input):

                if map_generator.is_position_in_map(dmap,
                                      pos_x + directions[direction][0],
                                      pos_y + directions[direction][1]):
                    
                    pos_x += directions[direction][0]
                    pos_y += directions[direction][1]
                    
                    dmap, discovered_map, pos_x, pos_y, treasure_number,\
                    is_player_alive, is_treasure_collected = \
                               enter_room(dmap, discovered_map, pos_x, pos_y, direction_opposites[direction],
                               treasure_number, is_player_alive, is_treasure_collected)

                else:
                    print(random.choice(text.no_passage))

                break

    return dmap, discovered_map, pos_x, pos_y, treasure_number, is_player_alive, is_treasure_collected
        
                

def game_loop():
    """
    Game loop.
    """

    input(text.start)
    
    while True:
        
        dmap, discovered_map, pos_x, pos_y, treasure_number = init_game()

        is_player_alive = True
        is_treasure_collected = False

        total_treasure = treasure_number

        input(random.choice(text.go_to_dungeon))
        input(random.choice(text.enter_dungeon))
        
        dmap, discovered_map, pos_x, pos_y, treasure_number,\
        is_player_alive, is_treasure_collected = \
            enter_room(dmap, discovered_map, pos_x, pos_y, text.entrance, treasure_number,
            is_player_alive, is_treasure_collected)

        while is_player_alive and not is_treasure_collected:
            
            dmap, discovered_map, pos_x, pos_y, treasure_number,\
            is_player_alive, is_treasure_collected = \
                process_player_commands(dmap, discovered_map, pos_x, pos_y,
                treasure_number, is_player_alive, is_treasure_collected)

        if is_player_alive:
            input(random.choice(text.won))
        else:
            input(random.choice(text.lost))
     
            print(text.game_statistics.format(*[total_treasure - treasure_number, total_treasure]))

        map_generator.print_dungeon_map(dmap)
        print(text.end_map_description)

        user_input = input(text.play_again_prompt).lower()

        if user_input == 'y' or user_input == 'yes':
            continue
        elif user_input == 'n' or user_input == 'no':
            break

        user_input = input(text.play_again_hint).lower()

        if user_input != 'y' and user_input != 'yes':
            break
            
                  
                  
