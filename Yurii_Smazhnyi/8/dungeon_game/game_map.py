import decorators
import custom_log
import random
from dungeon_input import DungeonInput
from vector2 import Vector2
from dungeon_exceptions import MapGeneratorError

class GameMap:
    """
    Class that represents game map.

    Contains static constants for in-game symbols.
    Has method for working with it(finding/replacing/printing)
    """

    GROUND_SYMBOL = 'O'
    TRAP_SYMBOL = 'X'
    PLAYER_SYMBOL = 'T'
    ENEMY_SYMBOL = 'E'
    TREASURE_SYMBOL = '='

    TRAP_MODIFIER = 10
    TREASURE_MODIFIER = 20


    def __init__(self, map_size):
        self._map = self._create_map(map_size)
        self.spawn_enemy()


    @decorators.info_decorator
    @decorators.debug_decorator
    def _create_map(self, map_size):
        """
        Create Map for Dungeon Game.

        :param map_size: size of map.
        :map_size type: int.
        :returns: created map with traps and treasures.
        :rtype: list of strings.
        """
        try:
            trap_count = (map_size * map_size) // GameMap.TRAP_MODIFIER

            if trap_count < 3:
                raise MapGeneratorError("To few traps! Setting more!")
        except MapGeneratorError as error:
            custom_log.logger.warning(error)
            trap_count = 3

        try:
            treasure_count = (map_size * map_size) // GameMap.TREASURE_MODIFIER

            if treasure_count < 3:
                raise MapGeneratorError("To few Treasures! Setting more!")
        except MapGeneratorError as error:
            custom_log.logger.warning(error)
            treasure_count = 3


        ground_count = (map_size * map_size) - trap_count - treasure_count - 1

        str_map = GameMap.GROUND_SYMBOL * ground_count
        str_map += GameMap.TRAP_SYMBOL * trap_count
        str_map += GameMap.TREASURE_SYMBOL * treasure_count
        str_map += GameMap.PLAYER_SYMBOL

        str_map = list(str_map)
        random.shuffle(str_map)
        str_map = "".join(str_map)

        final_map = [str_map[i:i+map_size] for i in range(0, map_size*map_size, map_size)]

        return final_map


    @decorators.info_decorator
    @decorators.debug_decorator
    def replace_character(self, position, new_character):
        """
        Replace character on map with new

        :param position: position of character to replace
        :position type: Vector2
        :param new_character: new character 
        :new_character type: str

        """

        self._map[position.y] = replace_str_index(self._map[position.y], position.x, new_character)


    @decorators.info_decorator
    @decorators.debug_decorator
    def spawn_enemy(self):
        """
        Method for spawning enemy on random posion
        Raise an exeption if enemy wasn't spawned.

        :returns: None
        """


        start_index = random.randint(0, len(self._map) / 2)

        for i in range(start_index, len(self._map)):

            for j in range(0, len(self._map[0])):

                if self._map[i][j] == GameMap.GROUND_SYMBOL:

                    self._map[i] = replace_str_index(self._map[i], j, GameMap.ENEMY_SYMBOL)

                    return

        raise MapGeneratorError("Enemy couldn't spawned!")



    @decorators.info_decorator
    @decorators.debug_decorator
    def print_map(self):
        """
        Formatted shortcut for printing game_map.

        :returns: None.
        :rtype: None.
        """

        for i in range(len(self._map)):
            custom_log.logger.info((self._map[i]))


    @decorators.info_decorator
    @decorators.debug_decorator
    def get_character_pos(self, symbol):
        """
        Returns character's position from game map.
        
        :param symbol: symbol that represents character on map
        :symbol type: str
        :returns: players position as (x,y).
        :rtype: list of two ints.
        """

        x_index = -1
        y_index = -1

        for i in range(len(self._map)):

            x_index = self._map[i].find(symbol)

            if x_index != -1:
                y_index = i
                break
        
        return Vector2(x_index, y_index)


    @decorators.info_decorator
    @decorators.debug_decorator
    def get_player_pos(self):
        """
        Returns player's position from game map.

        :returns: players position as (x,y).
        :rtype: list of two ints.
        """

        return self.get_character_pos(GameMap.PLAYER_SYMBOL)


    @decorators.info_decorator
    @decorators.debug_decorator
    def get_enemy_pos(self):
        """
        Returns player's position from game map.

        :returns: players position as (x,y).
        :rtype: list of two ints.
        """

        return self.get_character_pos(GameMap.ENEMY_SYMBOL)



    @decorators.info_decorator
    @decorators.debug_decorator
    def get_character_valid_directions(self, symbol):
        """
        Returns possible character's moves.

        :param symbol: symbol that represents character on map
        :symbol type: str
        :returns: list of possible moves.
        :rtype: list of strings.
        """

        x_size = len(self._map[0])
        y_size = len(self._map)

        character_pos = self.get_character_pos(symbol)

        valid_directions = []

        if character_pos.x > 0:
            valid_directions.append(DungeonInput.COMMANDS_TYPES[0])

        if character_pos.x < x_size - 1:
            valid_directions.append(DungeonInput.COMMANDS_TYPES[1])

        if character_pos.y < y_size - 1:
            valid_directions.append(DungeonInput.COMMANDS_TYPES[2])

        if character_pos.y > 0:
            valid_directions.append(DungeonInput.COMMANDS_TYPES[3])

        return valid_directions


    @decorators.info_decorator
    @decorators.debug_decorator
    def get_player_valid_directions(self):
        """
        Returns possible player's moves.

        :returns: list of possible moves.
        :rtype: list of strings.
        """

        return self.get_character_valid_directions(GameMap.PLAYER_SYMBOL)


    @decorators.info_decorator
    @decorators.debug_decorator
    def get_enemy_valid_directions(self):
        """
        Returns possible enemy's moves.

        :returns: list of possible moves.
        :rtype: list of strings.
        """

        return self.get_character_valid_directions(GameMap.ENEMY_SYMBOL)


    @decorators.info_decorator
    @decorators.debug_decorator
    def move_player(self, direction):
        """
        Move player on Game Map.

        :param direction: direction to move.
        :direction type: str.
        :returns: item player stepped on.
        :rtype: str.
        """

        item_stepped_on = GameMap.GROUND_SYMBOL

        player_pos = self.get_player_pos()

        if direction == DungeonInput.COMMANDS_TYPES[0]:

            item_stepped_on = self._map[player_pos.y][player_pos.x - 1]
            self._map[player_pos.y] = replace_str_index(self._map[player_pos.y],player_pos.x - 1, GameMap.PLAYER_SYMBOL)
            
        elif direction == DungeonInput.COMMANDS_TYPES[1]:

            item_stepped_on = self._map[player_pos.y][player_pos.x + 1]
            self._map[player_pos.y] = replace_str_index(self._map[player_pos.y],player_pos.x + 1, GameMap.PLAYER_SYMBOL)

        elif direction == DungeonInput.COMMANDS_TYPES[2]:

            item_stepped_on = self._map[player_pos.y + 1][player_pos.x]
            self._map[player_pos.y + 1] = replace_str_index(self._map[player_pos.y + 1],player_pos.x, GameMap.PLAYER_SYMBOL)

        elif direction == DungeonInput.COMMANDS_TYPES[3]:

            item_stepped_on = self._map[player_pos.y - 1][player_pos.x]
            self._map[player_pos.y - 1] = replace_str_index(self._map[player_pos.y - 1],player_pos.x, GameMap.PLAYER_SYMBOL)
            
        self._map[player_pos.y] = replace_str_index(self._map[player_pos.y], player_pos.x, GameMap.GROUND_SYMBOL)

        return item_stepped_on


    @decorators.info_decorator
    @decorators.debug_decorator
    def move_enemy(self, direction):
        """
        Move enemy on Game Map.

        :param direction: direction to move.
        :direction type: str.
        :returns: item player stepped on.
        :rtype: str.
        """

        item_stepped_on = GameMap.GROUND_SYMBOL

        character_pos = self.get_enemy_pos()

        if direction == DungeonInput.COMMANDS_TYPES[0]:

            item_stepped_on = self._map[character_pos.y][character_pos.x - 1]

            if item_stepped_on != GameMap.PLAYER_SYMBOL:

                self._map[character_pos.y] = replace_str_index(self._map[character_pos.y],character_pos.x - 1, GameMap.ENEMY_SYMBOL)
            
        elif direction == DungeonInput.COMMANDS_TYPES[1]:

            item_stepped_on = self._map[character_pos.y][character_pos.x + 1]

            if item_stepped_on != GameMap.PLAYER_SYMBOL:

                self._map[character_pos.y] = replace_str_index(self._map[character_pos.y],character_pos.x + 1, GameMap.ENEMY_SYMBOL)

        elif direction == DungeonInput.COMMANDS_TYPES[2]:

            item_stepped_on = self._map[character_pos.y + 1][character_pos.x]

            if item_stepped_on != GameMap.PLAYER_SYMBOL:
            
                self._map[character_pos.y + 1] = replace_str_index(self._map[character_pos.y + 1],character_pos.x, GameMap.ENEMY_SYMBOL)

        elif direction == DungeonInput.COMMANDS_TYPES[3]:

            item_stepped_on = self._map[character_pos.y - 1][character_pos.x]

            if item_stepped_on != GameMap.PLAYER_SYMBOL:

                self._map[character_pos.y - 1] = replace_str_index(self._map[character_pos.y - 1],character_pos.x, GameMap.ENEMY_SYMBOL)
            
        self._map[character_pos.y] = replace_str_index(self._map[character_pos.y], character_pos.x, GameMap.GROUND_SYMBOL)

        return item_stepped_on


    @decorators.info_decorator
    @decorators.debug_decorator
    def is_item_near_player(self, item):
        """
        Returns result of check is some item near player.

        :param item: item to check.
        :item type: char.
        :returns: result of check.
        :rtype: bool.
        """

        possible_directions = self.get_player_valid_directions()

        player_pos = self.get_player_pos()

        result = False

        for direction in possible_directions:

            if direction == DungeonInput.COMMANDS_TYPES[0]:

                if self._map[player_pos.y][player_pos.x - 1] == item:
                    result = True
                    break
                
            elif direction == DungeonInput.COMMANDS_TYPES[1]:

                if self._map[player_pos.y][player_pos.x + 1] == item:
                    result = True
                    break

            elif direction == DungeonInput.COMMANDS_TYPES[2]:

                if self._map[player_pos.y + 1][player_pos.x] == item:
                    result = True
                    break

            elif direction == DungeonInput.COMMANDS_TYPES[3]:

                if self._map[player_pos.y - 1][player_pos.x] == item:
                    result = True
                    break

        return result



@decorators.info_decorator
@decorators.debug_decorator
def replace_str_index(text,index=0,replacement=''):
    """
    Replace character at string.

    :param text: string to replace in.
    :text type: str.
    :param index: index of character.
    :index type: int.
    :param replacement: character to replace.
    :replacement type: str.
    :returns: result of check.
    :rtype: bool.
    """

    return '%s%s%s'%(text[:index],replacement,text[index+1:])



if __name__ == "__main__":
    my_map = GameMap(10)
    my_map.print_map()
    my_map.get_player_pos()
