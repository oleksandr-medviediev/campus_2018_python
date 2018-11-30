from DungeonMap import DungeonMap, DungeonCell
import DungeonGameConfig
import random
import time
import threading
import logging
from LoggerDecorator import logger_decorator


class Enemy:

    def __init__(self, enemy_name, player, dungeon_map):
        '''
        Constructor of enemy class.
        :param enemy_name: the name of enemy;
        :param player: a player to hunt;
        :param dungeon_map: the map on which enemy will be placed;
        :type enemy_name: str;
        :type player: Character;
        :type dungeon_map: DungeonMap.
        '''
        super().__init__()

        self.__name = enemy_name
        self.__dungeon_map = dungeon_map
        self.__is_free_cell = lambda cell: cell is DungeonCell.EMPTY
        self.__position = dungeon_map.get_random_cell_if(self.__is_free_cell)
        self.__should_move = False
        self.__moving_thread = None
        self.__dungeon_map.add_enemy_on_position(self.__position)
        self.__player = player

    
    @logger_decorator
    def __move(self):
        while self.__should_move:
            time.sleep(DungeonGameConfig.ENEMY_SPEED)
            cells_near = self.__dungeon_map.get_cells_near(self.__position)
            if DungeonCell.PLAYER in cells_near:
                logging.info(f'Enemy deals {DungeonGameConfig.ENEMY_DAMAGE} damage to a player!')
                self.__player.receive_damage(DungeonGameConfig.ENEMY_DAMAGE)
                if not self.__player.is_alive():
                    logging.info(f'Player dies:( Game over...')
                    break
                else:
                    self.__position = self.__dungeon_map.get_random_cell_if(self.__is_free_cell)
                    self.__dungeon_map.move_enemy(self.__position)
            else:
                possible_moves = self.__dungeon_map.get_positions_near(self.__position)
                is_empty_cell = lambda position: self.__dungeon_map.get_cell_on_position(position) is DungeonCell.EMPTY
                empty_cells_positions = filter(is_empty_cell, possible_moves)
                if empty_cells_positions:
                    new_position = random.choice(list(empty_cells_positions))
                    self.__position = new_position
                    self.__dungeon_map.move_enemy(new_position)


    @logger_decorator
    def start_moving(self):
        self.__should_move = True
        self.__moving_thread = threading.Thread(name='Enemy moving thread', target=self.__move)
        self.__moving_thread.start()


    @logger_decorator
    def stop_moving(self):
        self.__should_move = False
        self.__moving_thread.join()
