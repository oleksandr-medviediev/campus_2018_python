import dungeon_map as dm

START_POSITION = (0, 0)

def play_game(size):
    # create map
    # d_map = dm.create_map(size)
    # place player at center
    center = (size / 2, size / 2)
    # loop



d_map = [[0, 0], [0, 0]]
ind = (0, 0)
adj = dm.get_adjacent(d_map, ind) 


