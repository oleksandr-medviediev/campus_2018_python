import time
import threading
import logging
import random
from . import dungeon_game_logger
from . import dungeon_game_error
from . import level
from .character import Character
from .enemy import Enemy
from .dungeon_game_logger import debug_decorator
from .dungeon_game_logger import log_decorator


class Game:

    def __init__(self, level):
        self.__level = level
        self.__running = True
        self.__position_lock = threading.Lock()

    @debug_decorator
    @log_decorator('Run enemy thread...', logging.INFO)
    def enemy_loop(self):

        enemy = Enemy(self.__level)
        while self.__running:

            time.sleep(1)
            enemy.move()

            self.__position_lock.acquire()
            if enemy.x == self.__level.player.x and enemy.y == self.__level.player.y:

                self.__level.player.hit(1)
                dungeon_game_logger.logger.info('Enemy hit player')
                enemy.respawn()

            self.__position_lock.release()

    @debug_decorator
    @log_decorator('Main game loop started...', logging.INFO)
    def loop(self):
        """
        main loop of dungeon game
        """

        enemy_thread = threading.Thread(target=self.enemy_loop)
        enemy_thread.start()

        while self.__running:

            self.__offer_moves()
            self.__level.update(self.__position_lock)

            is_game_over = self.__is_over()

            if is_game_over:
                self.__running = False

        enemy_thread.join()

    @debug_decorator
    @log_decorator('offering moves to player...', logging.INFO)
    def __offer_moves(self):
        """
        offer player to do move
        """

        def __validate_cell(x, y):

            cell = '#'
            try:
                cell = self.__level.cell_at(x, y)
            except dungeon_game_error.CellOutOfBoundsDungeonGameError as error:
                dungeon_game_logger.logger.warning(f'{error}')

            return cell

        up_cell = __validate_cell(self.__level.player.x, self.__level.player.y - 1)
        down_cell = __validate_cell(self.__level.player.x, self.__level.player.y + 1)
        left_cell = __validate_cell(self.__level.player.x - 1, self.__level.player.y)
        right_cell = __validate_cell(self.__level.player.x + 1, self.__level.player.y)

        message = f'\nHealth: {self.__level.player.health}, Bags: {self.__level.player.bag}'
        message += '\n# - wall (dead end)\n$ - treasure\n! - trap\n_ - empty space\np - player\n'
        env_message = '\n{:^3}\n{}p{}\n{:^3}\n'.format(up_cell, left_cell, right_cell, down_cell)

        dungeon_game_logger.logger.info(message)

        if up_cell == '!' or down_cell == '!' or left_cell == '!' or right_cell == '!':
            dungeon_game_logger.logger.info('Trap somewhere!')

        if up_cell == '$' or down_cell == '$' or left_cell == '$' or right_cell == '$':
            dungeon_game_logger.logger.info('Treasure somewhere!')

        dungeon_game_logger.logger.info(env_message)

    def __is_over(self):
        """
        checks if game is over
        """

        over = self.__level.player.is_won() or self.__level.player.is_dead()

        return over

    def on_game_finished(self):
        """
        callback which called when game is over on some reason
        """
        self.__level.print()
