import map_generating as mg
from logger import m_logger


def init_game():
    m_logger.debug(f'game_step : starting game map initialization')
    mg.init()
    m_logger.debug(f'game_step : game map initialized')

    global player_position
    player_position = list(mg.spawn_player())
    m_logger.debug(f'game_step : player spawned')

    global is_player_lost
    is_player_lost = False

    global is_player_won
    is_player_won = False


def get_to_save_data():
    m_logger.debug(f'game_step : data to save ready to return')
    return mg.mapsize, mg.game_map


def set_loaded_data(data):
    m_logger.debug(f'game_step : starting data loading')
    mg.mapsize = data[0]
    mg.game_map = data[1]
    m_logger.debug(f'game_step : data loaded')
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
        m_logger.info('So sorry! You have lost this game :(')
    elif is_player_won:
        m_logger.info('Congratulations! You have won')
        
        
def print_game_map():

    TRAP = '#'
    TREASURE = '*'
    PLAYER = '!'
    EMPTY_CELL = '.'
    m_logger.debug(f'game_step : game map formatting to print started')
    game_map = mg.game_map
    game_map = [[TRAP if cell == -1 else cell for cell in row] for row in game_map ]
    m_logger.debug(f'game_step : game map traps formatted')
    game_map = [[TREASURE if cell == 1 else cell for cell in row] for row in game_map ]
    m_logger.debug(f'game_step : game map treasures formatted')
    game_map = [[EMPTY_CELL if cell == 0 else cell for cell in row] for row in game_map ]
    m_logger.debug(f'game_step : game map empty cells formatted')

    game_map[player_position[0]][player_position[1]] = PLAYER
    m_logger.debug(f'game_step : game map player position formatted')
    m_logger.debug(f'game_step : game map formatted')

    for r in game_map:
        print(*r)
    m_logger.debug(f'game_step : game map printed')

    m_logger.info(f'Player last position: {player_position}')
      

def get_neighbour_values():
    m_logger.debug(f'game_step : starting list of neighbour cells forming')
    neighbour_cells = [[player_position[0] + direction[0], player_position[1] + direction[1]]  for direction in list(DIRECTION_TO_MOVE.values())]
    neighbour_cells = list(filter(lambda cell: cell[0] >= 0 and cell[1] >= 0 and cell[0] < mg.mapsize and cell[1] < mg.mapsize, neighbour_cells))
    m_logger.debug(f'game_step : list of neighbour cells formed')

    neighbour_cells_values = [mg.game_map[cell[0]][cell[1]] for cell in neighbour_cells]
    m_logger.debug(f'game_step : list of neighbour cells values calculated')

    return neighbour_cells_values


def notify_player_about_traps():

    neighbour_values = get_neighbour_values()
    m_logger.debug(f'game_step : got list of neighbour cells')
    neighbour_values.sort()
    m_logger.debug(f'game_step : sorted list of neighbour cells')
   

    has_traps = neighbour_values[0] == -1
    if has_traps:
        m_logger.info('Be careful! Trap is somewhere near you!')


def notify_player_about_treasures():

    neighbour_values = get_neighbour_values()
    m_logger.debug(f'game_step : got list of neighbour cells')
    neighbour_values.sort(reverse = True)
    m_logger.debug(f'game_step : sorted (reverse = True) list of neighbour cells')

    has_treasures = neighbour_values[0] == 1
    if has_treasures:
        m_logger.info('You are close to win! Treasure is somewhere near you')


def perform_next_step(direction):
    global player_position
    old_position = list(player_position)
    m_logger.debug(f'game_step : saved previous position')

    direction_to_move = DIRECTION_TO_MOVE[direction]
    m_logger.debug(f'game_step : got direction to move by text value of direction')
    
    player_position[0] += direction_to_move[0]
    player_position[1] += direction_to_move[1]
    m_logger.debug(f'game_step : updated player position')

    if player_position[0] < 0 or player_position[1] < 0 or player_position[0] >= mg.mapsize or player_position[1] >= mg.mapsize:
        m_logger.info("You can't move there! You reached border!\n")
        m_logger.debug(f'game_step : player tried to move out from map')
        player_position[0] -= direction_to_move[0]
        player_position[1] -= direction_to_move[1]
        m_logger.debug(f'game_step : player position reverted')

    else:
        m_logger.info(f'Player position changed from ({old_position[1]},{old_position[0]}) to ({player_position[1]},{player_position[0]})')

    row, col = player_position

    global is_player_lost
    if mg.game_map[row][col] == -1:
        m_logger.debug(f'game_step : player lost')
        is_player_lost = True

    global is_player_won
    if mg.game_map[row][col] == 1:
        m_logger.debug(f'game_step : player won')
        is_player_won = True


DIRECTION_TO_MOVE = { 'up': [-1, 0], 'down' : [1, 0], 'left' : [0, -1], 'right' : [0, 1]  }
global player_position
