"""main game logic
"""

import pickle
import os.path
from contextlib import contextmanager
import threading
import time

from decorators import debug_decorator
from decorators import info_decorator
from game_logger import log_debug
from game_logger import log_info

from player import Player
from terrain import Terrain
from enemy import Enemy


class GameSession:

    def __init__(self, player_health, win_condition, map_scale=1):
        """initialize game session

        Arguments:
            player_health {int} -- player health
            win_condition {int} -- required number of treasures
                to collect to win the game
            map_scale {int} -- map scale
        """

        self.__win_condition = win_condition
        self.__terrain = Terrain(map_scale)

        start_row, start_col = self.__terrain.start_position
        start_position_message = F"start position: ({start_row}, {start_col})"
        log_debug(start_position_message)
        log_debug("map:")
        log_debug(self.__terrain)

        self.__player = Player(start_row, start_col, player_health)
        self.__enemy = Enemy(map_scale)
        self.__is_running = False

        self.__lock = threading.Lock()

    @info_decorator
    @debug_decorator
    def __structure_is_near(self, structure):
        """find if given structure is within one square

        Arguments:
            structure str -- structure to find

        Returns:
            bool -- true if given structure is within
            one square, false otherwise
        """

        is_near = False
        scale = self.__terrain.scale

        curr_row, curr_col = self.__player.position

        if curr_col < scale - 1:
            if self.__terrain.get_square(curr_row, curr_col + 1) == structure:
                is_near = True

        if curr_col > 1:
            if self.__terrain.get_square(curr_row, curr_col - 1) == structure:
                is_near = True

        if curr_row < scale - 1:
            if self.__terrain.get_square(curr_row + 1, curr_col) == structure:
                is_near = True

        if curr_row > 1:
            if self.__terrain.get_square(curr_row - 1, curr_col) == structure:
                is_near = True

        return is_near

    @info_decorator
    @debug_decorator
    def __write_move_fail_to_log(self, dir):
        """write fail while moving in specified directoin to log

        Arguments:
            dir str -- move direction
        """

        log_debug(F"failed to move {dir}")

    def __enemy_move(self):
        """enemy moving loop
        """

        while self.__is_running:

            time.sleep(1)

            self.__lock.acquire()

            if self.__player.position == self.__enemy.position:

                if self.__player.health > 0:
                    
                    self.__player.damage(1)
                    log_info("Enemy has found and damaged the player!")

                    if self.__player.health == 0:
                        log_info("Enemy has killed the player!")
                        self.__is_running = False

            self.__lock.release()

            self.__enemy.move()

    def __player_move(self):
        """player moving loop
        """

        border = self.__terrain.scale - 1

        while self.__is_running:

            curr_row, curr_col = self.__player.position

            if self.__terrain.get_square(curr_row, curr_col) == 't':

                log_debug("player has entered a trap")
                log_info("You have entered a trap!")
                self.__player.damage(1)

            if self.__terrain.get_square(curr_row, curr_col) == '*':

                log_debug("player has found a treasure")
                log_info("You have found a treasure!")
                self.__player.grant_treasure(1)

            if self.__player.health <= 0:
                log_debug("player has died")
                log_debug("game ends")
                log_info("You have died!")
                self.__is_running = False

            if self.__player.bag >= self.__win_condition:
                log_debug("player has found enough")
                log_debug("game ends")
                log_info("You have found enogh treasure!")
                self.__is_running = False

            if self.__structure_is_near('t'):

                log_debug("trap is within one square")
                log_info('There is a trap within one square!')

            if self.__structure_is_near('*'):

                log_debug("treasure is within one square")
                log_info('There is a treasure within one square!')

            moved = False

            while not moved:

                command = input("What to do?: ")

                if not self.__is_running:
                    break

                if command == 'up':

                    if curr_row == 0:

                        log_info("You are already on top of the map!")
                        self.__write_move_fail_to_log(command)

                    else:

                        moved = True
                        curr_row -= 1
                        log_info("Moving up")

                elif command == 'down':

                    if curr_row == border:

                        log_info("You are already on bottom of the map!")
                        self.__write_move_fail_to_log(command)

                    else:

                        moved = True
                        curr_row += 1
                        log_info("Moving down")

                elif command == 'right':

                    if curr_col == border:

                        msg = "You are already on the right border of the map!"
                        log_info(msg)
                        self.__write_move_fail_to_log(command)

                    else:

                        moved = True
                        curr_col += 1
                        log_info("Moving right")

                elif command == 'left':

                    if curr_col == 0:

                        msg = "You are already on the left border of the map!"
                        log_info(msg)
                        self.__write_move_fail_to_log(command)

                    else:

                        moved = True
                        curr_col -= 1
                        log_info("Moving left")

                elif command == "save":

                    with open("sav.txt", "wb") as savefile:

                        pickle.dump(self.__dict__, savefile, protocol=0)
                        log_info("Saved succesfully")

                else:
                    log_info(F"Unknown command: {command}")

                if moved:

                    self.__lock.acquire()
                    self.__player.set_position(curr_row, curr_col)
                    self.__lock.release()

                    log_debug(F"moved {command}")
                    cur_pos_msg = F"current position: ({curr_row}, {curr_col})"
                    log_debug(cur_pos_msg)

    @info_decorator
    @debug_decorator
    def run(self):
        """run the game

            function is proceeded until player finds a
            treasure or enters a trap

        Arguments:
            start_row int -- start position row
            start_col int -- start position column
            squares_map [str] -- game map
        """
        self.__is_running = True

        enemy_thread = threading.Thread(target=self.__enemy_move)
        player_thread = threading.Thread(target=self.__player_move)

        enemy_thread.setDaemon(True)
        player_thread.setDaemon(True)

        player_thread.start()
        enemy_thread.start()

        while self.__is_running:
            time.sleep(1)

        log_info("Type \"up/down/left/right\" to move")
        log_info("Type \"save\" to save current game")

        log_info(self.__terrain)
        log_info("* - stands for a treasure")
        log_info("t - stands for a trap")
        log_info(". - stands for an empty square")
        log_info("s - stands for the start position\n")

    def load(self):
        """load the game if save file exists

        Returns:
            bool -- true if game has been succesfully loaded,
                false otherwise
        """

        has_loaded = False

        try:
            with open("sav.txt", "rb") as savefile:

                temp_dict = pickle.load(savefile)
                self.__dict__.update(temp_dict)
                log_debug("game loaded")
                has_loaded = True

        except OSError:
            log_info("No save file found :(")

        return has_loaded
