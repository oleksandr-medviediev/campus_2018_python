import game_map
from logger import debug_decorator
from logger import info_decorator

class GameStep:

    def __init__():
        print('ok1')
        my_game_map = GameMap()


    @debug_decorator
    @info_decorator
    def get_to_save_data():
        return my_game_map.get_to_save_data()


    @debug_decorator
    @info_decorator
    def get_game_map():
        return my_game_map.game_map

    @debug_decorator
    @info_decorator
    def set_loaded_data(data):

        my_game_map.mapsize = data[0]
        my_game_map.game_map = data[1]


    @debug_decorator
    @info_decorator
    def print_game_result():

        if is_player_lost:
            print('So sorry! You have lost this game :(')
        elif is_player_won:
            print('Congratulations! You have won')

            
    @debug_decorator
    @info_decorator        
    def print_game_map(player_position):

        TRAP = '#'
        TREASURE = '*'
        PLAYER = '!'
        EMPTY_CELL = '.'
        
        game_map = my_game_map.game_map
        game_map = [[TRAP if cell == -1 else cell for cell in row] for row in game_map ]
        game_map = [[TREASURE if cell == 1 else cell for cell in row] for row in game_map ]
        game_map = [[EMPTY_CELL if cell == 0 else cell for cell in row] for row in game_map ]

        game_map[player_position[0]][player_position[1]] = PLAYER

        for r in game_map:
            print(*r)

        print(f'Player last position: {player_position}')

          
    @debug_decorator
    @info_decorator
    def get_neighbour_values(player_position):

        neighbour_cells = [[player_position[0] + direction[0], player_position[1] + direction[1]] 
        for direction in list(DIRECTION_TO_MOVE.values())]
        neighbour_cells = list(filter(lambda cell: cell[0] >= 0 and cell[1] >= 0 
            and cell[0] < my_game_map.mapsize and cell[1] < my_game_map.mapsize, neighbour_cells))

        neighbour_cells_values = [my_game_map.game_map[cell[0]][cell[1]] for cell in neighbour_cells]

        return neighbour_cells_values


    @debug_decorator
    @info_decorator
    def notify_player_about_traps(player_position):

        neighbour_values = get_neighbour_values(player_position)
        neighbour_values.sort()

        has_traps = neighbour_values[0] == -1
        if has_traps:
            print('Be careful! Trap is somewhere near you!')


    @debug_decorator
    @info_decorator
    def notify_player_about_treasures():

        neighbour_values = get_neighbour_values(player_position)
        neighbour_values.sort(reverse = True)

        has_treasures = neighbour_values[0] == 1
        if has_treasures:
            print('You are close to win! Treasure is somewhere near you')


    @debug_decorator
    @info_decorator
    def perform_next_step(direction, player):

        old_position = list(player.position)

        direction_to_move = DIRECTION_TO_MOVE[direction]
        
        player.position[0] += direction_to_move[0]
        player.position[1] += direction_to_move[1]

        if player.position[0] < 0 or player.position[1] < 0 or player.position[0] >= my_game_map.mapsize or player.position[1] >= my_game_map.mapsize:

            print("You can't move there! You reached border!\n")
            player.position[0] -= direction_to_move[0]
            player.position[1] -= direction_to_move[1]

        else:
            print(f'Player position changed from ({old_position[1]},{old_position[0]}) ' 
                + f'to ({player.position[1]},{player.position[0]})')

        row, col = player.position

        if my_game_map.game_map[row][col] == -1:
            player.pick_trap()

        if my_game_map.game_map[row][col] == 1:
            player.pick_treasure()


    DIRECTION_TO_MOVE = { 'up': [-1, 0], 'down' : [1, 0], 'left' : [0, -1], 'right' : [0, 1]  }
