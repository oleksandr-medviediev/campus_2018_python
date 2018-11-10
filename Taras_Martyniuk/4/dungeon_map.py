from random import randint
from itertools import product
'''
    Tile type enum - all possible objects for a dungeon tile (defined below)
    dungeon map object is a 2D array holding Tile type enums
'''

# tile type enum
Empty, Treasure, Trap = range(3)
TREASURE_QUOTA = 0.1
MINE_QUOTA = 0.2


def create_map(size):
    pass


def get_random_empty_tile(map):
    '''
        :param map: dungeon map object
        :returns: 2D tuple of indices of random empty tile
    '''
    rand_index = lambda: randint(0, len(map))

    while True:
        maybe_empty = (rand_index(), rand_index())
        if maybe_empty == Empty:
            return maybe_empty


# it's a pity i can't just write array_2D[(0, 0)]
def at(map, tile):
    '''
        gets the tile type by tuple of indices
        :param tile: 2d tuple
    '''
    return map[tile[0]][tile[1]]


def is_trap_nearby(map, tile):
    pass


def is_mine_nearby(map, tile):
    pass


def get_adjacent(d_map, tile):
    '''
        returns a list of all adjacent tiles types for param tile
        if it is a corner tile, returns only those that are in bounds
    '''
    deltas = product([0, 1], repeat=2)

    print(f'ds : {deltas}')
    adjacent = map(lambda d: (d[0] + tile[0], d[1] + tile[1]), deltas)

    print(f'adj : {adjacent}')


    adj_in_bounds =  filter(lambda a: in_bounds(d_map, a), adjacent)
    adj_types = [d_map.at(t) for t in adj_in_bounds]
    return adj_types

def in_bounds(map, tile):
    pass
