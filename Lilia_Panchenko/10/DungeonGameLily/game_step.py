from .game_map import GameMap
from .logger import my_logger


class GameStep:
    """
    Class to control game step. Responsible for setting up map, print game result, print game map, notify player about 
    surrounding traps and treasures
    """

    def __init__(self):
        """
        Constructor for GameStep class
        """
        self.my_game_map = GameMap()
        self.DIRECTION_TO_MOVE = { 'up': [-1, 0], 'down' : [1, 0], 'left' : [0, -1], 'right' : [0, 1]  }


    @my_logger.debug_decorator
    @my_logger.info_decorator
    def setup_map(self):
        """
        Function called to setup map
        """
        self.my_game_map.setup_map()


    @my_logger.debug_decorator
    @my_logger.info_decorator
    def get_to_save_data(self):
        """
        Function called to get save data
        : return : game map save data
        : rtype : tuple
        """
        return self.my_game_map.get_to_save_data()


    @my_logger.debug_decorator
    @my_logger.info_decorator
    def get_game_map(self):
        """
        Getter for game map
        : return : game map
        : rtype : GameMap
        """
        return self.my_game_map

    @my_logger.debug_decorator
    @my_logger.info_decorator
    def set_loaded_data(self, data):
        """
        Function called to set saved data
        : param : data to setup
        : ptype : tuple
        """
        self.my_game_map.mapsize = data[0]
        self.my_game_map.game_map = data[1]


    @my_logger.debug_decorator
    @my_logger.info_decorator
    def print_game_result(self, player):
        """
        Function called to print game result. Print some text message depending on player won or lost the game
        : param : player
        : ptype : Player
        """
        if player.islost:
            print('So sorry! You have lost this game :(')
        elif player.iswon:
            print('Congratulations! You have won')

            
    @my_logger.debug_decorator
    @my_logger.info_decorator        
    def print_game_map(self, player_position):
        """
        Function called to print game map. Prints map and last player position
        : param : player_position - cell where player ended game
        : ptype : list of two elements
        """
        TRAP = '#'
        TREASURE = '*'
        PLAYER = '!'
        EMPTY_CELL = '.'
        
        game_map = self.my_game_map.game_map
        game_map = [[TRAP if cell == -1 else cell for cell in row] for row in game_map ]
        game_map = [[TREASURE if cell == 1 else cell for cell in row] for row in game_map ]
        game_map = [[EMPTY_CELL if cell == 0 else cell for cell in row] for row in game_map ]

        game_map[player_position[0]][player_position[1]] = PLAYER

        for r in game_map:
            print(*r)

        print(f'Player last position: {player_position}')

          
    @my_logger.debug_decorator
    @my_logger.info_decorator
    def get_neighbour_values(self, player_position):
        """
        Function called to analyze neighbour cells for player position
        : param : player_position - cell where player ended game
        : ptype : list of two elements
        : return : list of neighbour cells for player. -1 means trap in cell, 1 means treasure in cell, 0 means empty 
        cell
        : rtype : list of ints
        """
        neighbour_cells = [[player_position[0] + direction[0], player_position[1] + direction[1]] \
        for direction in list(self.DIRECTION_TO_MOVE.values())]

        neighbour_cells = list(filter(lambda cell: cell[0] >= 0 and cell[1] >= 0 
            and cell[0] < self.my_game_map.mapsize and cell[1] < self.my_game_map.mapsize, neighbour_cells))

        neighbour_cells_values = [self.my_game_map.game_map[cell[0]][cell[1]] for cell in neighbour_cells]

        return neighbour_cells_values


    @my_logger.debug_decorator
    @my_logger.info_decorator
    def notify_player_about_traps(self, player_position):
        """
        Function called to notify player about surrounding traps
        : param : player_position - cell where player ended game
        : ptype : list of two elements
        """
        neighbour_values = self.get_neighbour_values(player_position)
        neighbour_values.sort()

        has_traps = neighbour_values[0] == -1
        if has_traps:
            print('Be careful! Trap is somewhere near you!')


    @my_logger.debug_decorator
    @my_logger.info_decorator
    def notify_player_about_treasures(self, player_position):
        """
        Function called to notify player about surrounding treasures
        : param : player_position - cell where player ended game
        : ptype : list of two elements
        """
        neighbour_values = self.get_neighbour_values(player_position)
        print(player_position[0], player_position[1])
        neighbour_values.sort(reverse = True)

        has_treasures = neighbour_values[0] == 1
        if has_treasures:
            print('You are close to win! Treasure is somewhere near you')


    @my_logger.debug_decorator
    @my_logger.info_decorator
    def perform_next_step(self, direction, player, enemy):
        """
        Function called to perform game step
        : param1 : direction player want to move
        : ptype1 : tuple
        : param2 : player
        : ptype2 : Player
        : param3 : enemy
        : ptype3 : Enemy
        """
        old_position = list(player.position)

        direction_to_move = self.DIRECTION_TO_MOVE[direction]

        player.position[0] += direction_to_move[0]
        player.position[1] += direction_to_move[1]

        player_is_attacked = enemy.is_attacked_player(player)
        if player_is_attacked:
            print("Enemy attacked player")
            enemy.spawn(self.my_game_map)
            player.lose_hp()


        if player.position[0] < 0 or player.position[1] < 0 or \
            player.position[0] >= self.my_game_map.mapsize or player.position[1] >= self.my_game_map.mapsize:

            print("You can't move there! You reached border!\n")
            player.position[0] -= direction_to_move[0]
            player.position[1] -= direction_to_move[1]

        else:
            print(f'Player position changed from ({old_position[1]},{old_position[0]}) ' 
                + f'to ({player.position[1]},{player.position[0]})')

        row, col = player.position

        if self.my_game_map.game_map[row][col] == -1:
            player.lose_hp()
            self.my_game_map.game_map[row][col] = 0

        if self.my_game_map.game_map[row][col] == 1:
            player.pick_treasure()
            self.my_game_map.game_map[row][col] = 0
