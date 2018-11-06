from map_generator import dungeon_map_generator
from random import randint


def spawn_player(width, height, dungeon_map):
    """
    Parameters corresponds to map size
    """
    while True:

        player_x = randint(0, width - 1)
        player_y = randint(0, height - 1)

        if dungeon_map[player_y][player_x] != '-':

            continue

        else:

            break

    return [player_x, player_y]


def make_move(move_direction, player_position, map_size):
    """
    Changes player position according to user input
    """

    if not move_direction in set(['w', 'd', 's', 'a']):

        print('Wrong direction! Try again!')

    old_position = player_position[:]


    if move_direction == 'w':

        if player_position[1] > 0:

            player_position[1] -=1
            print('You have moved up')

    elif move_direction == 'd':

        if player_position[0] < map_size[0] - 1:

            player_position[0] +=1
            print('You have moved right')

    elif move_direction == 's':

        if player_position[1] < map_size[1] - 1:

            player_position[1] +=1
            print('You have moved down')

    elif move_direction == 'a':

        if player_position[0] > 0:

            player_position[0] -=1
            print('You have moved left')

    if old_position == player_position:

        print("There is a wall!")


def check_around(player_x, player_y, map_size, dungeon_map, player_map):
    """
    This function performs check for treasures/traps in surrounding cells
    """
    is_treasure = False
    is_trap = False

    row_range = range(player_y - 1 if player_y - 1 > 0 else 0, player_y + 2 if player_y + 1 < map_size[1] else map_size[1])
    column_range = range(player_x - 1 if player_x - 1 > 0 else 0, player_x + 2 if player_x + 1 < map_size[0] else map_size[0])

    for y in row_range:

        for x in column_range:

            if dungeon_map[y][x] == 'T':

                is_treasure = True

            elif dungeon_map[y][x] == 'X':

                is_trap = True

    if is_treasure and is_trap:

        fill_cells = '!'

    elif is_treasure:

        fill_cells = 't'

    elif is_trap:

        fill_cells = 'x'

    else:

        fill_cells = '-'

    for y in row_range:

        for x in column_range:

            if not player_map[y][x] == '-':

                player_map[y][x] = fill_cells

    return (is_treasure, is_trap)



def game_loop():
    """
    Main game function contains game loop and some surrounding stuff
    """
    map_request = input('Enter preferable map size in format "width:height", or just press enter to play with default map:\n')

    if not len(map_request):

        map_size = [20, 10]

    else:

        map_size = [int(token) for token in map_request.split(':')]

    game_map = dungeon_map_generator(*map_size)

    player_map = [['?' for x in range(0, map_size[0])] for y in range(0, map_size[1])]

    player_position = spawn_player(*map_size, game_map)

    result_of_check = check_around(*player_position, map_size, game_map, player_map)

    player_map[player_position[1]][player_position[0]] = '@'

    for row in player_map:

        print("".join(row))

    if result_of_check[0]:

        print('There is a treasure!')

    elif result_of_check[1]:

        print('There is a trap!')

    while True:

        move = input('\nEnter your move, please (w - up, d - right, s - down, a - left):\n')

        player_map[player_position[1]][player_position[0]] = '-'

        make_move(move, player_position, map_size)

        result_of_check = check_around(*player_position, map_size, game_map, player_map)

        player_map[player_position[1]][player_position[0]] = '@'

        for row in player_map:

           print("".join(row))

        if result_of_check[0]:

            print('There is a treasure!')

        elif result_of_check[1]:

            print('There is a trap!')

        if game_map[player_position[1]][player_position[0]] == 'T':

            print("\n>>>This is a treasure! You are victorious!<<<\n")
            break

        elif game_map[player_position[1]][player_position[0]] == 'X':

            print("\n}}}This is a trap! You loose!{{{\n")
            break

        else:

            continue

    for row in game_map:

        print("".join(row))
