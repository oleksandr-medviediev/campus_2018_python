from random import randrange
import dungeon_game_logger as log


class GameMap:
    __game_matrix = []
    __player_position = []
    __enemy_position = []

    
    def create_map(self, map_size):
        """
        Create game map.

        :param map_size: width and height of map.
        :type my_map: int.

        :return: None.

        """
        self.__map_size = map_size

        for i in range (map_size):
            line = ["_" for j in range(map_size)]
            self.__game_matrix.append(line)

        trap_number = int((map_size ** 2) / 10)
        treasure_number = int((map_size ** 2) / 20)

        count = 0

        while True:
            row = randrange(map_size)
            column = randrange(map_size)

            if self.__game_matrix[row][column] == "_":
                self.__game_matrix[row][column] = "x"
                count += 1
            
            if count == trap_number:
                break

        count = 0

        while True:
            row = randrange(map_size)
            column = randrange(map_size)

            if self.__game_matrix[row][column] == "_":
                self.__game_matrix[row][column] = "$"
                count += 1
            
            if count == treasure_number:
                break

        while True:
            row = randrange(map_size)
            column = randrange(map_size)

            if self.__game_matrix[row][column] == '_':
                self.__game_matrix[row][column] = "p"
                self.__player_position = [row, column]
                break
        
        self.spawn_enemy()
        
        self.print_map()


    def spawn_enemy(self):
        """
        Spawn and respawn enemy on map.

        :return: None.

        """
        while True:
            map_size = len(self.__game_matrix)

            row = randrange(map_size)
            column = randrange(map_size)

            if self.__game_matrix[row][column] == "_":
                self.__game_matrix[row][column] = "e"
                self.__enemy_position = [row, column]
                break


    @property
    def game_matrix(self):
        return self.__game_matrix


    @game_matrix.setter
    def game_matrix(self, game_matrix):
        self.__game_matrix = game_matrix
        
        for i in range(len(self.__game_matrix)):
            line = self.__game_matrix[i]
            index = [i for i in range(len(line)) if line[i] == "p"]
            if len(index) > 0:
                self.__player_position = [i, index[0]]
                break


    @property
    def player_position(self):
        return self.__player_position

    
    @property
    def enemy_position(self):
        return self.__enemy_position


    def update_map(self, old_position):
        """
        Update player position on the map.

        :param my_map: old player position.
        :type my_map: list.

        :return: None.

        """
        old_x = old_position[0]
        old_y = old_position[1]

        x = self.__player_position[0]
        y = self.__player_position[1]

        self.__game_matrix[old_x][old_y] = "_"
        self.__game_matrix[x][y] = "p"


    def update_enemy_position(self, old_enemy_position, enemy_position):
        """
        Update enemy position on the map.

        :param old_enemy_position: old enemy position.
        :type old_enemy_position: list.

        :param new_enemy_position: new enemy position.
        :type new_enemy_position: list.

        :return: None.

        """
        old_x = old_enemy_position[0]
        old_y = old_enemy_position[1]

        if self.__game_matrix[old_x][old_y] == "e":
            self.__game_matrix[old_x][old_y] = "_"

        new_x = enemy_position[0]
        new_y = enemy_position[1]

        if self.__game_matrix[new_x][new_y] == "_":
            self.__game_matrix[new_x][new_y] = "e"

        self.__enemy_position = enemy_position


    def print_map(self):
        """
        Print game map.

        :return: None.

        """
        for i in self.__game_matrix:
            print(i)

    
    def get_map_size(self):
        """
        Return size of game map.

        :return: map size.
        :rtype: int.

        """
        return len(self.__game_matrix)

    
    def discover_surround_area(self, points):
        """
        Check on trap and treasure naerby.

        :param my_map: player position.
        :type my_map: list.

        :return: None.

        """
        for i in points:
            row = i[0]
            col = i[1]
            
            if self.__game_matrix[row][col] == "$":
                log.logger.info("Treasure is nearby!")
            elif self.__game_matrix[row][col] == "x":
                log.logger.info("Trap is nearby!")


    def check_on_treasure(self, treasure_position):
        """
        Check if player find treasure.

        :param my_map: treasure position.
        :type my_map: list.

        :return: True of False.
        :rtype: bool.

        """
        result = False

        x = treasure_position[0]
        y = treasure_position[1]

        if self.__game_matrix[x][y] == "$":
            log.logger.info("You find treasure")
            result = True

        return result


    def check_on_trap(self, trap_position):
        """
        Check if player find trap.

        :param my_map: treasure position.
        :type my_map: list.

        :return: True of False.
        :rtype: bool.

        """
        result = False

        x = trap_position[0]
        y = trap_position[1]

        if self.__game_matrix[x][y] == "x":
            log.logger.info("You find trap")
            result = True

        return result    
