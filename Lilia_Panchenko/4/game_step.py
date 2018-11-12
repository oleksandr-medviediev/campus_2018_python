import map_generating as mg


def init_game():

    mg.init()

    global player_position
    player_position = list(mg.spawn_player())

    global is_player_lost
    is_player_lost = False

    global is_player_won
    is_player_won = False



def is_game_ended():

    if is_player_lost or is_player_won:
        return True
    return False


def print_game_result():

    if is_player_lost:
        print('So sorry! You have lost this game')
    elif is_player_won:
        print('Congratulations! You have won')
        
        
def print_game_map():

    TRAP = '#'
    TREASURE = '*'
    PLAYER = '!'
    EMPTY_CELL = '.'

    game_map = mg.game_map
    game_map = [[TRAP if cell == -1 else cell for cell in row] for row in game_map ]
    game_map = [[TREASURE if cell == 1 else cell for cell in row] for row in game_map ]
    game_map = [[EMPTY_CELL if cell == 0 else cell for cell in row] for row in game_map ]

    game_map[player_position[0]][player_position[1]] = PLAYER

    for r in game_map:
        print(*r)

    print(player_position)
      

def get_neighbour_values():

    neighbour_cells = [[player_position[0] + direction[0], player_position[1] + direction[1]]  for direction in list(DIRECTION_TO_MOVE.values())]
    neighbour_cells = list(filter(lambda cell: cell[0] >= 0 and cell[1] >= 0 and cell[0] < mg.mapsize and cell[1] < mg.mapsize, neighbour_cells))

    print(neighbour_cells)

    neighbour_cells_values = [mg.game_map[cell[0]][cell[1]] for cell in neighbour_cells]

    return neighbour_cells_values


def notify_player_about_traps():

    neighbour_values = get_neighbour_values()
    neighbour_values.sort()
   

    has_traps = neighbour_values[0] == -1
    if has_traps:
        print('Be careful! Trap is somewhere near you!')


def notify_player_about_treasures():

    neighbour_values = get_neighbour_values()
    neighbour_values.sort(reverse = True)

    has_treasures = neighbour_values[0] == 1
    if has_treasures:
        print('You are close to win! Treasure is somewhere near you')


def perform_next_step(direction):
    global player_position

    old_position = list(player_position)

    direction_to_move = DIRECTION_TO_MOVE[direction]
    
    player_position[0] += direction_to_move[0]
    player_position[1] += direction_to_move[1]

    if player_position[0] < 0 or player_position[1] < 0 or player_position[0] >= mg.mapsize or player_position[1] >= mg.mapsize:
        print("You can't move there! You reached border!\n")
        player_position[0] -= direction_to_move[0]
        player_position[1] -= direction_to_move[1]

    else:
        print(f'Player position changed from {old_position} to {player_position}\n')

    row, col = player_position

    global is_player_lost
    if mg.game_map[row][col] == -1:
        is_player_lost = True

    global is_player_won
    if mg.game_map[row][col] == 1:
        is_player_won = True


DIRECTION_TO_MOVE = { 'up': [-1, 0], 'down' : [1, 0], 'left' : [0, -1], 'right' : [0, 1]  }
global player_position
