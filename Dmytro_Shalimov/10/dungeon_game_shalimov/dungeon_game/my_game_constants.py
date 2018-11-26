EMPTY_CELL = '#'
TREASURE = 'T'
TRAP = 'C'
PLAYER = 'P'
ENEMY = 'E'
DEAD_PLAYER = 'X'

CELL_TYPES_INFO_MESSAGES = {TREASURE: 'There is a treasure nearby', TRAP: 'Careful! A trap is near'}

PLAYER_MOVE_DIRECTIONS_NAMES = ['u', 'd', 'l', 'r']
PLAYER_MOVE_DIRECTIONS_BY_NAMES = {'u': (-1, 0), 'd': (1, 0), 'l': (0, -1), 'r': (0, 1)}

SAVE_GAME_HEADER = 'this is valid saved game file'

ENEMY_MOVE_INTERVAL = 5
