import dungeon_game_player as pm
import dungeon_game_enemy as em
from map_test_package import dungeon_game_map as mm
import dungeon_game_logger as log
import dungeon_game_save_and_load as io
import dungeon_game_exceptions as exc
import threading
import time


class DungeonGame:
    __game_map = mm.GameMap()
    __player = pm.Player()
    __enemy = em.Enemy()
    __io_manager = io.GameIO()
    __lock = threading.Lock()


    def initialize(self):
        """
        Initialize game objects. Create map and player.

        return: None

        """

        result = True
        map_size = 0
        input_value = 0

        try:
            option = str(input("Press 1 to load game and press 2 to create new game"))

            if not option.isdigit():
                raise TypeError

            input_value = int(option)
            
            if (input_value < 1) or (input_value > 2):
                raise ValueError

        except TypeError:
            log.logger.error("TypeError exception. Invalid input data type.")
            result = False

        except ValueError:
            log.logger.error("ValueError exception. Invalid input data.")
            result = False

        if input_value == 1:
            game_map = self.__io_manager.load_game()
            self.__game_map.game_matrix = game_map

            if len(game_map) == 0:
                result = False

        elif input_value == 2:
            while True:
                try:
                    map_size = int(input("Enter the map size [8-15]"))

                    if (map_size >= 8) and (map_size <= 15):
                        break

                    raise exc.MapException("Invalid map size!")
                except exc.MapException as map_error:
                    log.logger.error(map_error.message)
            
            self.__game_map.create_map(map_size)

        if result:
            player_position = self.__game_map.player_position
            self.__player.position = player_position

            enemy_position = self.__game_map.enemy_position
            self.__enemy.position = enemy_position
        
        return result
    

    def run_game(self):
        """
        Describe game logic, update player position and map, check if player win or lose.

        :return: None.

        """

        direction_map = {
            "a": "left",
            "d": "right",
            "w": "up",
            "s": "down",
            "save": ""
        }

        enemy_thread = threading.Thread(target=self.update_enemy, name="enemy_thread")
        enemy_thread.start()

        while True:
            if self.__player.is_player_dead():
                break
                
            directions = self.update_player_directions()
        
            try:
                value = input("Choose direction 'a'-left, 'd'-right, 'w'-up, 's'-down, 'save'-to save game")
                if not value in direction_map:
                    raise ValueError

                if value == "save":
                    self.__io_manager.save_game(self.__game_map.game_matrix)
                    log.logger.info("The game is successfully saved!")
                    continue
                
                if not direction_map[value] in directions:
                    raise exc.InvalidDirectionException(self.__player.position, direction_map[value])

            except ValueError:
                log.logger.info("Incorect input value!")
                continue
            except exc.InvalidDirectionException as dir_error:
                log.logger.error(dir_error.message)
                continue
            
            new_position = self.__player.position
            old_position = new_position.copy()

            try:
                if value == "a":
                    new_position[1] -= 1
                elif value == "d":
                    new_position[1] += 1
                elif value == "w":
                    new_position[0] -= 1
                elif value == "s":
                    new_position[0] += 1

                if (new_position[0] < 0) or (new_position[0] > self.__game_map.get_map_size()) or \
                    (new_position[1] < 0) or (new_position[1] > self.__game_map.get_map_size()):
                    raise exc.InvalidPositionException(new_position)
            
            except exc.InvalidPositionException as pos_error:
                log.error(pos_error.position)
                continue

            is_treasure = self.__game_map.check_on_treasure(new_position)
            is_trap = self.__game_map.check_on_trap(new_position)

            if is_treasure:
                if self.__player.increase_treasure_and_check_on_win():
                    self.__game_map.update_map(old_position)
                    self.__game_map.print_map()
                    break
            elif is_trap:
                if self.__player.decrease_health_and_check_on_lose():
                    self.__game_map.update_map(old_position)
                    self.__game_map.print_map()
                    break
            
            if self.__enemy.position == self.__player.position:
                self.__player.decrease_health_and_check_on_lose()

                self.__game_map.spawn_enemy()
                self.__enemy.position = self.__game_map.enemy_position

            self.__game_map.update_map(old_position)
            self.__game_map.print_map()

        enemy_thread.join()

    
    def update_player_directions(self):
        """
        Check all available directions for player.

        :return: list of directions.
        :rtype: list.

        """
        size = self.__game_map.get_map_size()

        x = self.__player.position[0]
        y = self.__player.position[1]

        surround_points = []
        move_direction = []

        surround_points.append([x, y + 1])
        surround_points.append([x + 1, y])
        surround_points.append([x, y - 1])
        surround_points.append([x - 1, y])

        move_direction.append("right")
        move_direction.append("down")
        move_direction.append("left")
        move_direction.append("up")

        point_value = [-1, -1]
        str_value = ""

        for i in range(len(surround_points)):
            if ((surround_points[i][0] < 0) or
                (surround_points[i][0] > (size - 1)) or
                (surround_points[i][1] < 0) or
                (surround_points[i][1] > (size - 1))):
                surround_points[i] = point_value
                move_direction[i] = str_value

        while point_value in surround_points:
            surround_points.remove(point_value)

        while str_value in move_direction:
            move_direction.remove(str_value)

        self.__game_map.discover_surround_area(surround_points)

        log.logger.info("You can move: ")
        for i in move_direction:
            log.logger.info(i)
        
        return move_direction


    def update_enemy_directions(self):
        """
        Check all available directions for enemy.

        :return: list of directions.
        :rtype: list.

        """
        size = self.__game_map.get_map_size()

        x = self.__enemy.position[0]
        y = self.__enemy.position[1]

        surround_points = []
        move_direction = []

        surround_points.append([x, y + 1])
        surround_points.append([x + 1, y])
        surround_points.append([x, y - 1])
        surround_points.append([x - 1, y])

        move_direction.append("right")
        move_direction.append("down")
        move_direction.append("left")
        move_direction.append("up")

        point_value = [-1, -1]
        str_value = ""

        for i in range(len(surround_points)):
            if ((surround_points[i][0] < 0) or
                (surround_points[i][0] > (size - 1)) or
                (surround_points[i][1] < 0) or
                (surround_points[i][1] > (size - 1))):
                surround_points[i] = point_value
                move_direction[i] = str_value

        while point_value in surround_points:
            surround_points.remove(point_value)

        while str_value in move_direction:
            move_direction.remove(str_value)
        
        return move_direction


    def update_enemy(self):
        """
        Method of the thread. Update enemy position each 3 seconds.

        :return: None.

        """

        while True:
            time.sleep(3)

            self.__lock.acquire()

            if self.__player.is_player_dead() or self.__player.is_player_win():
                break

            old_enemy_position = self.__enemy.position.copy()
            directions = self.update_enemy_directions()
            self.__enemy.update_direction(directions)

            enemy_position = self.__enemy.position
            self.__game_map.update_enemy_position(old_enemy_position, enemy_position)

            if enemy_position == self.__player.position:
                self.__player.decrease_health_and_check_on_lose()

                self.__game_map.spawn_enemy()
                self.__enemy.position = self.__game_map.enemy_position

            print("\n\n\n")
            self.__game_map.print_map()

            self.__lock.release()


if __name__ == ('__main__'):
    """
        In this program the module 'map_test_package' was downloaded from  https://test.pypi.org/project/map-test-package/
    """

    game = DungeonGame()
    is_game_init = game.initialize()

    if is_game_init:
        game.run_game()
