import dungeon_map as dm
from logging_defs import debug_logger as dlog

player_moves = {
    ''
}

def play_game(size):
    # create map
    dmap = dm.create_map(size)
    print(dm.map_to_str(dmap))

    # d_map = dm.create_map(size)
    # place player at center
    start = dm.get_random_empty_tile(dmap)
    dlog.debug(f'Starting at {start}')
    # loop






