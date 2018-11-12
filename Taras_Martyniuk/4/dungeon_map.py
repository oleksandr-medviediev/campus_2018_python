from random import randint
from itertools import product
from logging_defs import debug_logger as dlog
from random import shuffle
from math import floor


'''
    type aliases for module:
    Tile type enum - all possible objects for a dungeon tile
    dungeon map object is a 2D array holding Tile type enums
    Tile - 2D tuple of ints indicating indices in dungeon map 
'''
# tile type enum
Empty, Treasure, Trap = range(3)
TREASURE_QUOTA = 0.1
TRAP_QUOTA = 0.2


def create_map(size):
    '''
        creates a size * size dungeon map
        where 1/10 tiles are treasures and other 2/10 - traps

        :param size: int, > 0
        :returns: dungeon map (2D tile type array)
    '''
    count = size * size
    trap_count = floor(count * TRAP_QUOTA)
    treasure_count = floor(count * TREASURE_QUOTA)
    empty_count = count - trap_count - treasure_count

    treasures = [Treasure] * treasure_count
    traps = [Trap] * trap_count
    empties = [Empty] * empty_count

    dlog.debug(f'Created {treasure_count} treasures, {trap_count} traps, {empty_count} empties')

    combined = treasures
    combined.extend(traps)
    combined.extend(empties)
    
    shuffle(combined)
    dmap = list(chunks(combined, size))

    dlog.debug(f'Created a map of {len(combined)} elements (with size {size})')
    return dmap


def chunks(l, n):
    """
        Yield successive n-sized chunks from l.
    """
    for i in range(0, len(l), n):
        yield l[i:i + n]


def get_random_empty_tile(dmap):
    '''
        :param map: dungeon map object
        :returns: random Tile with empty type
    '''
    dlog.debug('get_random_empty_tile')
    rand_index = lambda: randint(0, len(dmap) - 1)

    while True:
        maybe_empty = (rand_index(), rand_index())
        dlog.debug(f'randomed tile: {maybe_empty}')

        if at(dmap, maybe_empty) == Empty:
            return maybe_empty


# it's a pity i can't just write array_2D[(0, 0)]
def at(dmap, tile):
    '''
        gets type of the Tile
        :param tile: Tile
    '''
    assert in_bounds(dmap, tile)
    return dmap[tile[0]][tile[1]]


def is_trap_nearby(dmap, tile):
    adj = get_adjacent(dmap, tile)
    return any(map(lambda t: t == Trap, adj))


def is_treasure_nearby(dmap, tile):
    adj = get_adjacent(dmap, tile)
    return any(map(lambda t: t == Treasure, adj))


def get_adjacent(dmap, tile):
    '''
        returns a list of all adjacent tiles types for param tile
        if it is a corner tile, returns only those that are in bounds
    '''
    assert in_bounds(dmap, tile)

    deltas = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    adjacent = map(lambda d: (d[0] + tile[0], d[1] + tile[1]), deltas)

    adj_in_bounds =  filter(lambda a: in_bounds(dmap, a), adjacent)
    adj_types = [at(dmap, t) for t in adj_in_bounds]
    return adj_types


def in_bounds(dmap, tile):
    '''
        checks if the Tile is inside dungeon map
    '''
    assert isinstance(tile, tuple)
    horiz_ok = tile[0] >= 0 and tile[0] < len(dmap)
    vert_ok = tile[1] >= 0 and tile[1] < len(dmap)

    return horiz_ok and vert_ok


def set_tile(dmap, tile, tile_type):
    '''
        changes the type of tile
        also, looks hideous because of all the brackets
    '''
    dmap[tile[0]][tile[1]] = tile_type


def map_to_str(dmap, curr_pos=None):
    '''
        :param dmap: dungeon map
        :returns: string where each line is map's row, displaying types of all tiles
    '''

    curr_pos_mark = 42
    tile_symbols = {
        Empty : '.',
        Treasure : '⛃',
        Trap : '💣',
        curr_pos_mark : 'Y'
    }
    changed = at(dmap, curr_pos)
    set_tile(dmap, curr_pos, curr_pos_mark)

    row_to_str = lambda row : " ".join(map(lambda t: tile_symbols[t], row))
    printed = "\n".join(map(row_to_str, dmap))
    set_tile(dmap, curr_pos, changed)
    return printed

