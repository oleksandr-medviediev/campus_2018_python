from game_logger import logger
from decorator import debug_decorator
from random import randint

from dungeon_cell import unassigned_cell,\
empty_cell, entrance_cell, treasure_cell

from trap import Trap, trap_types,\
trap_goblins, trap_hidden_blade, trap_curse, trap_inquisition

from utils import Position

from custom_errors import DungeonMapInitializationError,\
 DungeonMapCellOutOfBoundsError

directions = (Position(0, 1),
             Position(1, 0),
             Position(0, -1),
             Position(-1, 0))

class DungeonMap:

    cells_dict = {unassigned_cell.legend : unassigned_cell,
    empty_cell.legend : empty_cell,
    entrance_cell.legend : entrance_cell,
    treasure_cell.legend : treasure_cell,
    trap_goblins.legend : trap_goblins,
    trap_hidden_blade.legend : trap_hidden_blade,
    trap_curse.legend : trap_curse,
    trap_inquisition.legend : trap_inquisition
    }

    cells_dict_explained = {
    empty_cell.legend : "empty ",
    entrance_cell.legend : "entrance",
    treasure_cell.legend : "treasure",
    trap_goblins.legend : "goblins",
    trap_hidden_blade.legend : "hidden_blade",
    trap_curse.legend : "curse",
    trap_inquisition.legend : "inquisition"
    }

    discovery_dict = {
    "entrance":"e",
    "player":"p",
    "unknown":"?",
    "empty":"0",
    "treasure near":"+",
    "trap near":"-",
    "treasure and trap near":"%"
    }


    def __init__(self):
        """
        Constructor of DungeonMap class
        """
        self.height = 0
        self.width = 0
        self.cells = ()


    @debug_decorator
    def is_position_in_map(self, pos):
        """
        Checks whether dungeon map has tile with specified coordinates.

        Args:
        pos (Position) position in question

        Returns:
        (bool) True if dungeon map has tile with this coordinates,
               False otherwise
        """

        is_inside = (pos.x >= 0
                     and pos.y >= 0
                     and pos.x < self.width
                     and pos.y < self.height)

        return is_inside


    @debug_decorator
    def cell(self, pos):
        """
        Gets value of cell with specified coordinates or returns False

        param: pos (Position) position of the cell in question

        returns: value of cell with those coordinates if it's inside map
        False otherwise
        """
        # Not using DungeonMapCellOutOfBoundsError since returning False is part
        # of intended functionality
        if not self.is_position_in_map(pos):
            return False

        return self.cells[pos.x][pos.y]

    @debug_decorator
    def assign_cell(self, pos, value):
        """
        Assignes value to cell at position pos.

        param: pos (Position) position of the cell
        """

        try:
            self.cells[pos.x][pos.y] = value

        except IndexError:
            raise DungeonMapCellOutOfBoundsError("Attempt to assign value to "
            "cell out of dungeon map bounds", pos)


    @debug_decorator
    def initialize(self, height, width, treasure_number, traps, start_pos):
        """
        Initializes DungeonMap

        param: height (int) height of the map
        param: width (int) width of the map
        param: treasure_number (int) number of treasures on map
        param: traps (iterateble) traps to put on map
        param: start_pos (Position) player starting position on map
        """
        try:
            is_input_valid = width * height > treasure_number + len(traps) + 1
        except TypeError as error:
            raise DungeonMapInitializationError("Incorrect parameter type in "
            "DungeonMap initialize. \n {}".fromat(str(error)))
        else:
            if not is_input_valid:
                raise DungeonMapInitializationError("Incorrect parameters in "
                "DungeonMap initialize. Map can't fit all of the cells.")

        self.width = width
        self.height = height

        self.cells = [[empty_cell.legend for i in range(height)]
         for j in range(width)]

        logger.debug("empty map generated")

        try:
            self.cells[start_pos.x][start_pos.y] = entrance_cell.legend
        except IndexError:
            raise DungeonMapInitializationError("Incorrect parameters in "
            "DungeonMap initialize. Strating position is out of DungeonMap "
            "boundaries")

        while treasure_number > 0:
            pos = Position.generate_random_position(width, height)

            if self.cell(pos) == empty_cell.legend:
                self.cells[pos.x][pos.y] = treasure_cell.legend
                treasure_number -= 1

        logger.debug("treasures generated")

        while traps:
            pos = Position.generate_random_position(width, height)

            if self.cell(pos) == empty_cell.legend:
                self.cells[pos.x][pos.y] = traps.pop()

        logger.debug("traps generated")


    @debug_decorator
    def initialize_discovered_map(self, height, width, start_pos):
        """
        Creates players map for the beginning of the game
        """
        self.width = width
        self.height = height

        self.cells = [[DungeonMap.discovery_dict["unknown"] for i in range(height)]
        for j in range(width)]

        self.cells[start_pos.x][start_pos.y] = DungeonMap.discovery_dict["empty"]


    @debug_decorator
    def print_map(self):
        """
        Prints map
        """
        printed_map = [[row[i] for row in self.cells]
                   for i in range(self.height)]

        printed_map.reverse()

        for row in printed_map:
            for cell in row:
                print(str(cell), " ", end = '')

            print('')

    @debug_decorator
    def check_for_adjacent_types(self, pos, types):
        """
        Checks if any of ajacent to pos cells contain any element from types.

        param:pos (Position) cells adjucent to which need to be checked
        param:types (iterable) types which appearance in ajucent cells
        needs to bre checked

        return: (bool) True if ajucent cells contain element from types,
        False otherwise
        """

        for direction in directions:
            for type in types:
             if self.cell(pos + direction) == type:
                 return True

        return False
