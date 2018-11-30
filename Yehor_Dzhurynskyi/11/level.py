import random
import pickle
import logging
import math
from player import Player
from dungeon_game_logger import debug_decorator
from dungeon_game_logger import log_decorator
import dungeon_game_logger
import dungeon_game_error


class Level:

    def update(self, lock):
        """
        function that being called on each tick
        """

        dx, dy = self.player.input(self)
        desired_x = self.player.x + dx
        desired_y = self.player.y + dy

        try:
            destination_cell = self.cell_at(desired_x, desired_y)
        except dungeon_game_error.CellOutOfBoundsDungeonGameError as error:

            dungeon_game_logger.logger.info('f{error}')
            return

        lock.acquire()

        self.player.x += dx
        self.player.y += dy

        lock.release()

        self.player.on_location_changed(destination_cell)

        if destination_cell == '!' or destination_cell == '$':
            lvl = list(self.__level_data)
            lvl[desired_x + desired_y * self.size] = '_'
            self.__level_data = ''.join(lvl)

        if self.player.is_dead():
            dungeon_game_logger.logger.info('You fell into third trap, GAME OVER =<')
        elif self.player.is_won():
            dungeon_game_logger.logger.info('You found three treasure, VICTORY!')

    def cell_at(self, x, y):
        """
        retrieves string representation of cell in coords (x, y)
            :param int x: x-coord of cell
            :param int y: y-coord of cell
            :return: cell of level in coords (x, y)
            :rtype: str
        """

        out_of_bounds = x < 0 or y < 0 or x >= self.size or y >= self.size
        if out_of_bounds:
            raise dungeon_game_error.CellOutOfBoundsDungeonGameError(self.size, x, y)

        cell = self.__level_data[x + y * self.size]

        return cell

    @property
    def size(self):
        return self.__size

    @property
    def player(self):
        return self.__player

    @debug_decorator
    @log_decorator('saving level...')
    def save(self):
        """
        saves level in file
        """

        with open('save.pickable', 'wb') as handle:
            pickle.dump(self, handle)

    @staticmethod
    @debug_decorator
    @log_decorator('loading level...')
    def load():
        """
        loads level from file
        :return: loaded level from file
        :rtype: Level
        """

        with open('save.pickable', 'rb') as handle:
            loaded_level = pickle.load(handle)

        return loaded_level

    @staticmethod
    @debug_decorator
    @log_decorator('generating level...')
    def generate(size):
        """
        generating level for dungeon game
            :param int size: size of level that should be generated
            :return: randomly generated level
            :rtype: Level
        """

        num_of_traps = (size * size) // 5
        num_of_treasures = (size * size) // 8
        num_of_empty_space = (size * size) - num_of_traps - num_of_treasures

        generated_level = '!' * num_of_traps + '$' * num_of_treasures + '_' * num_of_empty_space
        cells = list(generated_level)
        random.shuffle(cells)

        generated_level = Level()
        generated_level.__level_data = ''.join(cells)
        generated_level.__size = size

        player_x, player_y = generated_level.random_inner_point()
        generated_level.__player = Player(player_x, player_y)

        return generated_level

    @debug_decorator
    @log_decorator('randoming inner point...', logging.INFO)
    def random_inner_point(self):
        """
        reserve valid location for character on level
            :return: x and y coord of spawned character
            :rtype: tuple
        """

        while True:

            cell_pos = random.randint(0, len(self.__level_data) - 1)
            if self.__level_data[cell_pos] == '_':

                point_x, point_y = cell_pos % self.size, cell_pos // self.size
                break

        return point_x, point_y

    def print(self):
        """
        prints string representation of level
        """

        for row in range(self.size):

            lvl_row = self.__level_data[row * self.size: row * self.size + self.size]
            print(lvl_row)

    @property
    def level_data(self):
        return self.__level_data