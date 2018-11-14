import random
from game_logger import logger
import os 

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

    logger.debug("print_dungeon_map function invoked")
    
    printed_map = [[row[i] for row in dungeon_map]
                   for i in range(len(dungeon_map[0]))]

    printed_map. reverse()
    
    for row in printed_map:
        for cell in row:
            print(str(cell), " ", end = '')

        print('')

    logger.debug("map printed")
    

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

    logger.debug("generate_dungeon_map function invoked")
    
    if trap_number + treasure_number > height * width:
        logger.debug("generate_dungeon_map has incorrect parameters")
        return

    logger.debug("generaing map with width {} and height {}".format(width, height))
    
    dmap = [[tiles['empty'] for i in range(height)] for j in range(width)]

    dmap[start_x][start_y] = tiles['player']

    logger.debug("generating {} traps".format(trap_number))
    while trap_number > 0:
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)

        if dmap[x][y] == tiles['empty']:
            dmap[x][y] = tiles['trap']
            trap_number -= 1

    logger.debug("traps generated")
    
    logger.debug("generating {} treasures".format(treasure_number))
    while treasure_number > 0:
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)

        if dmap[x][y] == tiles['empty']:
            dmap[x][y] = tiles['treasure']
            treasure_number -= 1

    logger.debug("treasures generated")

    logger.debug("dungeon map generated")

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

    logger.debug("is_position_in_map function invoked for position {}, {}".format(pos_x, pos_y))

    map_height = len(dmap)
    map_width = len(dmap[0])

    is_inside = (pos_x >= 0
                 and pos_y >= 0
                 and pos_x < map_width
                 and pos_y < map_height)

    logger.debug("position {},{} checked. It's existance in map is {}".format(pos_x, pos_y, is_inside))

    return is_inside


def count_tiles_of_type(dmap, tile_type):
    """
    Counts tiles of specified type in dungeon map
    
    Args:
    dmap list of lists represanting dungeon map
    tile_type type of tiles in question

    Returns:
    (int) number of tiles of specified type in dungeon map
    """

    logger.debug("generate_dungeon_map function invoked for type {}".format(tile_type))

    number_of_tiles = 0

    for column in dmap:
        number_of_tiles += column.count(tiles[tile_type])

    return number_of_tiles
    

