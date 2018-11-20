from random import shuffle
from random import randint
import logger_decorator

class DungeonGameMap:

    game_entities = {'cell': '-', 'trap': '#', 'treasure':'X', 'player':'I', 'path':'+'}
    treasure_inverse_rate = 20
    trap_inverse_rate = 10


    @logger_decorator.time_logger_decorator
    @logger_decorator.debug_logger_decorator
    def generate_characters(self, map_square):
        """
        generates list of characters except player in random order
        :param: square of map
        :paramtype: int
        :return: list of characters
        :rtype:list(string)
        """
        treasures_count = map_square // self.treasure_inverse_rate
        trap_count = map_square // self.trap_inverse_rate

        empty_cells_count = map_square - (trap_count + treasures_count)

        map_filling = []
        map_filling.extend([self.game_entities['cell'] for count in range(empty_cells_count)])
        map_filling.extend([self.game_entities['trap'] for count in range(trap_count)])
        map_filling.extend([self.game_entities['treasure'] for count in range(treasures_count)])

        shuffle(map_filling)

        return map_filling


    @logger_decorator.time_logger_decorator
    @logger_decorator.debug_logger_decorator
    def spawn_player(self, map_filling):
        """
        randomly puts player on generated map
        :param: generated list of characters - map
        :paramtype: list(string)
        :return: player spawn position 
        :return type: (int,int)
        """
        is_empty_cell = False
        player_position = 0

        while not is_empty_cell:
            player_position = randint(0, len(map_filling) - 1)
            is_empty_cell = map_filling[player_position] in [self.game_entities['trap'],self.game_entities['treasure']]

        map_filling[player_position] = self.game_entities['player']

        player_start_position_x = player_position // self.map_size_x
        player_start_position_y = player_position % self.map_size_x

        return [player_start_position_x,player_start_position_y]


    @logger_decorator.time_logger_decorator
    @logger_decorator.debug_logger_decorator
    def generate_map(self):
        """
        transforms list of characters to matrix - list of lists
        :param map_size_x: number of columns
        :param map_size_y: number of rows
        :paramtype map_size_x, map_size_y: int
        """
        map_square = self.map_size_x * self.map_size_y
        map_characters_list = self.generate_characters(map_square)
        self.player_spawned_position = self.spawn_player(map_characters_list)
        self.generated_map = [map_characters_list[i*self.map_size_x:(i+1)*self.map_size_x] for i in range(self.map_size_y)]


    @logger_decorator.time_logger_decorator
    @logger_decorator.debug_logger_decorator
    def __init__(self, map_size_x, map_size_y):

        self.map_size_x = map_size_x
        self.map_size_y = map_size_y

        self.player_spawned_position = []
        self.generated_map = []

        self.generate_map()


    @logger_decorator.time_logger_decorator
    @logger_decorator.debug_logger_decorator
    def print_map(self):
        """
        prints map
        :param generated_map: map of characters list of lists
        :paramtype generated_map: list(list(string))
        :return: nothing
        :return type: None
        """
        for row in self.generated_map:
            print(''.join(row))


    @logger_decorator.time_logger_decorator
    @logger_decorator.debug_logger_decorator
    def mark_path(self, position):
        """
        marks the visited cells with +
        :param position: cell coordinates to mark
        :paramtype: list[int,int]
        """
        x = position[0]
        y = position[1]
        self.generated_map[x][y] = '+'

	
    @logger_decorator.time_logger_decorator
    @logger_decorator.debug_logger_decorator
    def get_current_cell_status(self, status):
        """
        retrieves the string-name of the cell element
        :param status: one the character of game_entities
        :paramtype: str
        :return: corresponding key from game_entities for character param
        :rtype: str
        """
        searched_value = str()

        for k, v in self.game_entities.items():
            if v == status:
                searched_value = k
                break

        return searched_value


    @logger_decorator.time_logger_decorator
    @logger_decorator.debug_logger_decorator
    def reinit(self, loaded_map, map_size):
        """
        assigns new values to generated_map and map_size_x,map_size_y
        :param loaded_map: loaded map
        :paramtype loaded_map: list(list(str))
        :param map_size: loaded map_size 
        :paramtype map_size: list(int,int)
        """
        self.generated_map = loaded_map
        self.map_size_x = map_size[0]
        self.map_size_y = map_size[1]
	

if __name__ == '__main__':

    m = DungeonGameMap(5,5)
    m.print_map()

