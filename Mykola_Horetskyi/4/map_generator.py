import random

tiles = {'unknown':'?',
         'empty':'0',
         'bordering treasure':'1',
         'bordering trap':'2',
         'bordering treasure and trap':'3',
         'player':'p',
         'treasure':'t',
         'trap':'#'}


def print_dungeon_map(dungeon_map):
    """
    Prints dungeon map
    """

    printed_map = [[row[i] for row in dungeon_map]
                   for i in range(len(dungeon_map[0]))]

    printed_map. reverse()
    
    for row in printed_map:
        for cell in row:
            print(str(cell), ' ', end='')

        print('')
    

def generate_dungeon_map(width, height, start_x, start_y, trap_number, treasure_number):
    """
    Generates dungeon map

    Args:
        width (int) 
        height (int)
        start_x(int)
        start_y(int)
        trap_number(int) number of traps on map
        treasure_number(int) number of treasures on map

    Returns:
        list of lists represanting map
     """

    if trap_number + treasure_number > height * width:
        return

    dmap = [[tiles['empty'] for i in range(height)] for j in range(width)]

    dmap[start_x][start_y] = tiles['player']

    while trap_number > 0:
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)

        if dmap[x][y] == tiles['empty']:
            dmap[x][y] = tiles['trap']
            trap_number -= 1

    while treasure_number > 0:
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)

        if dmap[x][y] == tiles['empty']:
            dmap[x][y] = tiles['treasure']
            treasure_number -= 1

    return dmap


def is_position_in_map(dmap, pos_x, pos_y):
    """
    Checks whether dungeon map has tile with specified coordinates.

    Args:
    dmap list of lists represanting dungeon map
    pos_x (int) x-coordinate of tile in question
    pos_y (int) y coordinate of tile in qustion

    Returns:
    (bool) True if dungeon map has tile with this coordinates,
           False otherwise
    """

    map_height = len(dmap)
    map_width = len(dmap[0])

    is_inside = (pos_x >= 0
                 and pos_y >= 0
                 and pos_x < map_width
                 and pos_y < map_height)

    return is_inside

    

