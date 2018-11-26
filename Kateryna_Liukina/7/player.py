from Game_logger import logger
from Game_logger import log_decorator
from Game_logger import debug_decorator
from custom_exeption import InvalidDirectionError


class Player:

    direction_map = {'up': [1, 0], 'down': [-1, 0], 'left': [0, -1], 'right': [0, 1]}

    @log_decorator
    @debug_decorator
    def __init__(self, game_map):
        """
        Function creates player
        Args:
            game_map(GameMap): game map where player spawn
        Returns:
            none
        """
        self.position = game_map.generate_coordinates()
        self.hp = 3
        self.treasure = 0


    @log_decorator
    @debug_decorator
    def move(self, game_map, game_input):
        """
        Function moves player on game_map in given direction
        Args:
            game_map(GameMap): game map
            game_input(str): direction to move
        Returns:
            none
        """
        if game_input not in self.direction_map.keys():
            raise InvalidDirectionError
        
        direction = self.direction_map[game_input]
        self.position[0] += direction[0]
        self.position[1] += direction[1]

        self.position[0] = max(0, min(self.position[0], game_map.size[0] - 1))
        self.position[1] = max(0, min(self.position[1], game_map.size[1]  - 1))

        if game_map.map_[self.position[0]][self.position[1]] == 1:
            self.hp -= 1
            game_map.map_[self.position[0]][self.position[1]] = 0

        elif game_map.map_[self.position[0]][self.position[1]] == 2:
            self.treasure +=1
            game_map.map_[self.position[0]][self.position[1]] = 0


    @log_decorator
    @debug_decorator
    def print_info(self):
        """
        Function prints player data
        Returns:
            none
        """
        logger.info("Your position: {}".format(self.position))
        logger.info("Your hp: {}".format(self.hp))
        logger.info("Your treasure: {}".format(self.treasure))

    @log_decorator
    @debug_decorator
    def generate_warning(self, game_map, game_item):
        """
        Function generate warning for dungeon game
        Args:
            game_map(GameMap): game map
            game_item(int): 1 - trap, 2 - treasure
        Returns:
            none
        """

        list_of_warnings = ["", "There's a trap within one square!", "There's a treasure within one square!"]
        position = [max(0, self.position[0] - 1), max(0, self.position[1] - 1)]
        while position[0] < min(self.position[0] + 2, game_map.size[0]):
            position[1] = max(0, self.position[1] - 1)
            while position[1] < min(self.position[1] + 2, game_map.size[1]):
                if game_map.map_[position[0]][position[1]] == game_item:
                    logger.warning(list_of_warnings[game_item])
                    return
                position[1] += 1
            position[0] += 1


    @log_decorator
    @debug_decorator
    def is_won(self):
        return self.treasure >= 3


    @log_decorator
    @debug_decorator
    def is_lost(self):
        return self.hp <= 0