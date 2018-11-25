from map_creator import DungeonGameMap
from player import Player
from enemy import Enemy
from input_module import read_input
from input_module import read_game_config
from input_module import main_menu_option
import files_module
import logger
import logger_decorator
import time
from random import choice
import threading


class Game:
    
    moves = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    moving_commands = { 'up':moves[0], 'down':moves[1], 'right':moves[2], 'left':moves[3] }
    managing_commands = ["save"]
    warnings = ["This is impasse\n", "The trap is near you\n", "The treasure is near you\n", "The enemy found you\n"]


    def __init__(self, map_size_x, map_size_y, name):

        self.game_map = DungeonGameMap(map_size_x, map_size_y)
        self.player = Player(name,self.game_map.player_spawned_position)
        self.enemy = Enemy([0,0])
        self.enemy.spawn_in_random_position((map_size_x, map_size_y))
        

    @logger_decorator.time_logger_decorator
    @logger_decorator.debug_logger_decorator
    def perform_move(self,command):
        """
        Changes player's position according to command
        :param player_pos_x: current player's position x  
        :param player_pos_y: current player's position y
        :param command: command to execute from moving_commands
        :return: new position
        :rtype: (int,int)
        """        
        self.game_map.mark_path(self.player.position)
        
        self.player.move(self.moving_commands[command])

        if not self.player.check_new_position([self.game_map.map_size_x,self.game_map.map_size_y]):
            self.player.move_opposite(self.moving_commands[command])
            logger.logging_object.warning(self.warnings[0])            


    @logger_decorator.time_logger_decorator
    @logger_decorator.debug_logger_decorator
    def is_game_ended(self):
        """
        Checks if game is ended
        :param: player's position information - game entity character
        :paramtype: str
        :return: if the end game condition is reached
        :rtype: bool
        """
        is_ended = True

        player_status = self.player.check_player_status()

        if player_status == 'You won!':
            logger.logging_object.info(player_status)
        elif player_status == 'You lost':
            logger.logging_object.info(player_status)
        else:
            is_ended = False

        return is_ended


    @logger_decorator.time_logger_decorator
    @logger_decorator.debug_logger_decorator
    def update(self):
        """
        Checks the current game state(neighbour positions) and outputs information about it
        :param player_pos_x: player's position x
        :param player_pos_y: player's position y
        :paramtype player_pos_x,player_pos_y: int
        :return: nothing
        :rtype: None
        """   
        number_of_treasures_near = 0
        number_of_traps_near = 0
        
        for direction in self.moves:

            neighbour_cell_x = self.player.position[0] + direction[0]
            neighbour_cell_y = self.player.position[1] + direction[1]

            if not 0 <= neighbour_cell_x < self.game_map.map_size_y or not 0 <= neighbour_cell_y < self.game_map.map_size_x:
                continue

            if self.game_map.generated_map[neighbour_cell_x][neighbour_cell_y] == self.game_map.game_entities['treasure']:
                number_of_treasures_near += 1
            elif self.game_map.generated_map[neighbour_cell_x][neighbour_cell_y] == self.game_map.game_entities['trap']:
                number_of_traps_near += 1
            
        if number_of_treasures_near > 0:
            logger.logging_object.warning(self.warnings[2])
            
        if number_of_traps_near > 0:
            logger.logging_object.warning(self.warnings[1])


    @logger_decorator.time_logger_decorator
    @logger_decorator.debug_logger_decorator
    def reinit(self, reinit_list):

        loaded_map, map_size = reinit_list[0], reinit_list[1]
        position, bag, hp, name, enemy_position = reinit_list[2], reinit_list[3], reinit_list[4], reinit_list[5], reinit_list[6]
        self.game_map.reinit(loaded_map, map_size)
        self.player.reinit(name, position, bag, hp)
        self.enemy.reinit(enemy_position)


    @logger_decorator.time_logger_decorator
    @logger_decorator.debug_logger_decorator
    def update_enemy(self):

        is_end = False

        while not is_end:
            time.sleep(3)
            
            command = choice(list(self.moving_commands.keys()))
            self.enemy.move(self.moving_commands[command])
            

            if not self.enemy.check_new_position([self.game_map.map_size_x,self.game_map.map_size_y]):
                self.enemy.move_opposite(self.moving_commands[command])

            if self.enemy.check_enemy_status(self.player.position):
                logger.logging_object.warning(self.warnings[3])
                self.player.take_damage()
                self.enemy.spawn_in_random_position((self.game_map.map_size_x,self.game_map.map_size_y))
            
            is_end = self.is_game_ended()
            

    @logger_decorator.time_logger_decorator
    @logger_decorator.debug_logger_decorator
    def run_game_loop(self):
        """
        Runs the main game logic
        :param start_pos_x: player's starting position x
        :param start_pos_y: player's startin position y
        :paramtype start_pos_x,start_pos_y: int
        :return: nothing
        :rtype: None
        """  
        is_end = False

        while not is_end:

            self.update()
            command = read_input(self.moving_commands,self.managing_commands)

            logger.logging_object.info(f'Input command {command}')

            if command == self.managing_commands[0]:

                map_size = (self.game_map.map_size_x, self.game_map.map_size_y)
                files_module.save_game_state(self.game_map.generated_map, self.player.position, map_size, self.player.bag, self.player.hp, self.player.name, self.enemy.position)
                logger.logging_object.info('Game is saved successfully') 
                continue
            
            self.perform_move(command)

            current_cell_element = self.game_map.generated_map[self.player.position[0]][self.player.position[1]]
            current_cell_status = self.game_map.get_current_cell_status(current_cell_element)

            self.player.resolve_new_position(current_cell_status)
            
            is_end = self.is_game_ended()

            #self.game_map.print_map()

        self.game_map.generated_map[self.player.position[0]][self.player.position[1]] = self.game_map.game_entities['player']


if __name__ == '__main__':

    player_name = input("Input your name\n")
    
    option = main_menu_option()
    
    if option == 'start':

        map_size_x,map_size_y = read_game_config()
        game = Game(map_size_x, map_size_y, player_name)
        
    elif files_module.check_loading():

        game = Game(5, 5, player_name)
        game.reinit(files_module.load_game())

    else:
        
        logger.logging_object.info("Can't load game\n")
        map_size_x,map_size_y = read_game_config()
        game = Game(map_size_x, map_size_y, "DefaultName")

    game_main_thread = threading.Thread(target=game.run_game_loop)
    enemy_thread = threading.Thread(target=game.update_enemy)

    game_main_thread.start()
    enemy_thread.start()

    enemy_thread.join()
    game_main_thread.join()
    
    game.game_map.print_map()
        
