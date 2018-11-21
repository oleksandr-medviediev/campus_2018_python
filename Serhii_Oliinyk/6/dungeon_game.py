import dungeon_game_player as pm
import dungeon_game_map as mm
import dungeon_game_save_and_load as io
import dungeon_game_logger as log


class DungeonGame:
    __game_map = mm.GameMap()
    __player = pm.Player()
    __io_manager = io.GameIO()


    def initialize(self):
        """
        Initialize game objects. Create map and player.

        return: None

        """
        map_size = 0

        option = int(input("Press 1 to load game and press 2 to create new game"))

        if option == 1:
            game_map = self.__io_manager.load_game()
            self.__game_map.game_matrix = game_map
        elif option == 2:
            while True:
                map_size = int(input("Enter the map size [8-15]"))

                if (map_size >= 8) and (map_size <= 15):
                    break

                log.logger.info("Wrong! Enter correct size!")
            
            self.__game_map.create_map(map_size)

        position = self.__game_map.player_position
        self.__player.position = position
    

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

        while True:
            directions = self.update_player_position()

            value = input("Choose direction 'a'-left, 'd'-right, 'w'-up, 's'-down, 'save'-to save game")
            if not value in direction_map:
                log.logger.info("Incorect input direction!")
                continue
            
            if value == "save":
                self.__io_manager.save_game(self.__game_map.game_matrix)
                log.logger.info("The game is successfully saved!")
                continue
            
            if not direction_map[value] in directions:
                log.logger.info("You cannot move in this direction!")
                continue
            
            new_position = self.__player.position
            old_position = new_position.copy()

            if value == "a":
                new_position[1] -= 1
            elif value == "d":
                new_position[1] += 1
            elif value == "w":
                new_position[0] -= 1
            elif value == "s":
                new_position[0] += 1

            is_treasure = self.__game_map.check_on_treasure(new_position)
            is_trap = self.__game_map.check_on_trap(new_position)

            if is_treasure:
                if self.__player.increase_treasure_and_check_on_win():
                    self.__game_map.update_map(old_position)
                    log.logger.info("You win!")
                    self.__game_map.print_map()
                    break
            elif is_trap:
                if self.__player.decrease_health_and_check_on_lose():
                    self.__game_map.update_map(old_position)
                    log.logger.info("You lose!")
                    self.__game_map.print_map()
                    break
            
            self.__game_map.update_map(old_position)
            self.__game_map.print_map()

    
    def update_player_position(self):
        """
        Check all available directions fro player.

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


if __name__ == ('__main__'):
    game = DungeonGame()
    game.initialize()
    game.run_game()
