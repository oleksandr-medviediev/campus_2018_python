import level
import logging
from character import Character
from dungeon_game_logger import debug_decorator
from dungeon_game_logger import log_decorator
import dungeon_game_logger
import dungeon_game_error


class Game:

    def __init__(self, level):
        self.__level = level

    @debug_decorator
    @log_decorator('Main game loop started...', logging.INFO)
    def loop(self):
        """
        main loop of dungeon game
        """

        while True:

            self.__offer_moves()
            self.__level.update()
            is_game_over = self.__is_over()

            if is_game_over:
                break


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
