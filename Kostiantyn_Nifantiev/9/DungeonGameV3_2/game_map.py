from dungeon_logger import my_logger
from dungeon_logger import log_decorator
from random import randint
from random import shuffle
from math import ceil
from my_exceptions import MapCoordinatesError
from my_exceptions import MapSizeError

class BasicMap:
    """
    Base class for map: just setting size and output into stream
    """
    @log_decorator
    def __init__(self):

        self.map_size = [20, 10]
        self.dungeon_map = []


    @log_decorator
    def reset_map_size(self):

        self.map_size = [20, 10]


    @log_decorator
    def set_map_size(self, width, height):


        if isinstance(width, int) and isinstance(height, int):

            try:

                if width < 5:

                    raise MapSizeError("", width, height)
                    width = 5

                elif width > 119:

                    raise MapSizeError("", width, height)
                    width = 119

                elif height < 5:

                    raise MapSizeError("", width, height)
                    height = 5

                elif height > 30:

                    raise MapSizeError("", width, height)
                    height = 30

            except MapSizeError as map_size_error:

                my_logger.exception(map_size_error)
                my_logger.error("Map size will be resetted to default value!")
                self.reset_map_size()
                return False

            self.map_size = [width, height]
            my_logger.debug("Map size has been stored successfully")
            return True

        else:

            my_logger.error("Wrong size type! Please, check the input")
            return False


    @log_decorator
    def draw_map(self):

        for row in self.dungeon_map:

            my_logger.info("".join(row))


    @log_decorator
    def set_cell_content(self, cell_x, cell_y, new_value):

        try:

            if cell_x >= self.map_size[0] or cell_y >= self.map_size[1]:

                raise MapCoordinatesError("Appeared while setting cell content", self.map_size, [cell_x, cell_y])

        except MapCoordinatesError as map_exception:

                my_logger.exception(map_exception)
                return False

        self.dungeon_map[cell_y][cell_x] = new_value
        return True


    @log_decorator
    def get_cell_content(self, cell_x, cell_y):

        try:

            if cell_x >= self.map_size[0] or cell_y >= self.map_size[1]:

                raise MapCoordinatesError("Appeared while getting cell content", self.map_size, [cell_x, cell_y])

        except MapCoordinatesError as map_exception:
            
            my_logger.exception(map_exception)
            return "-"

        return self.dungeon_map[cell_y][cell_x]


class DungeonMap(BasicMap):
    """
    This class coud make randomized map
    for further usage by game
    """
    @log_decorator
    def generate_map(self):

        width = self.map_size[0]
        height = self.map_size[1]

        cells_count = width * height
        treasures_count = ceil((cells_count) / 20)
        trap_count = ceil((cells_count) / 10)

        my_logger.debug("Traps and treasures quantity has been calculated")

        my_logger.debug("Generating map...")

        self.dungeon_map = ['T' for x in range(0, treasures_count)]
        self.dungeon_map.extend(['X' for x in range(0, trap_count)])
        self.dungeon_map.extend(['-' for x in range(0, cells_count - treasures_count - trap_count)])

        shuffle(self.dungeon_map)

        self.dungeon_map = [self.dungeon_map[x * width : x * width + width] for x in range(0, height)]



class PlayerMap(BasicMap):
    """
    Player map intended to show game world (dungeon) for player
    """
    @log_decorator
    def init_map(self):

        self.dungeon_map = [['?' for x in range(0, self.map_size[0])] for y in range(0, self.map_size[1])]


    @log_decorator
    def update_map(self, real_map, player_x, player_y):

        my_logger.debug("Checking for wall near player...")

        min_row_index = player_y - 1 if player_y - 1 > 0 else 0
        max_row_index = player_y + 2 if player_y + 1 < self.map_size[1] else self.map_size[1]
        row_range = range(min_row_index, max_row_index)

        min_column_index = player_x - 1 if player_x - 1 > 0 else 0
        max_column_index = player_x + 2 if player_x + 1 < self.map_size[0] else self.map_size[0]
        column_range = range(min_column_index, max_column_index)

        my_logger.debug("Wall check done")

        my_logger.debug("Checking for treasures and traps around")

        is_treasure = False
        is_trap = False

        for y in row_range:

            for x in column_range:

                if real_map.get_cell_content(x, y) == 'T':

                    is_treasure = True

                elif real_map.get_cell_content(x, y) == 'X':

                    is_trap = True

        if is_treasure and is_trap:

            cell_filler = '!'

        elif is_treasure:

            cell_filler = 't'

        elif is_trap:

            cell_filler = 'x'

        else:

            cell_filler = '-'

        my_logger.debug("Treasures and traps check done")

        my_logger.debug("Making output for player")

        for y in row_range:

            for x in column_range:

                if self.dungeon_map[y][x] == '@':

                    self.dungeon_map[y][x] = '-'

                elif not self.dungeon_map[y][x] == '-':

                    self.dungeon_map[y][x] = cell_filler

        self.dungeon_map[player_y][player_x] = '@'

        if is_treasure:

            my_logger.info('There is a treasure!')

        elif is_trap:

            my_logger.info('There is a trap!')

        my_logger.debug("Player output finished")

        return None
