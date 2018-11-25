import decorators
import custom_log
from threading import Event
from serializer import Serializer
from vector2 import Vector2
from dungeon_input import DungeonInput
from game_map import GameMap
from player import Player
from enemy import Enemy
from enemy_thread import EnemyThread


class Game:

    TREASURE_TO_WIN = 3

    def __init__(self):
        self.game_map = GameMap(10)
        self.player = Player("Halk", 3)
        self.enemy = Enemy()

    @decorators.info_decorator
    @decorators.debug_decorator
    def start(self):
        """
        Start Game.

        :returns: None.
        :rtype: None.
        """

        while True:

            debug_status = "Off" if decorators.is_debug else "On"
            info_status = "Off" if decorators.is_info else "On"
            string = input(f"Start Game(1)/Load Game(2)/Exit Game(3)/Turn { debug_status } Debug(4)/Turn { info_status } Info(5):")

            if string == '1':

                self.player = Player("Halk", 3)
                self.game_map = GameMap(10)
                custom_log.logger.info("Game Started!")
                self.play()

            elif string == '2':
                game_map = Serializer.load_map()

                if game_map == "":
                    custom_log.logger.error("Failed to Load Game")
                    continue

                custom_log.logger.info("Game Started!")
                self.play()

            elif string == '3':
                break

            elif string == '4':
                decorators.is_debug = not decorators.is_debug

            elif string == '5':
                decorators.is_info = not decorators.is_info



    @decorators.info_decorator
    @decorators.debug_decorator
    def play(self):
        """
        Function where whole game is happening.

        :returns: None.
        :rtype: None.
        """

        stop_flag = Event()

        enemy_thread = EnemyThread(self.enemy, self.player, self.game_map, stop_flag)
        enemy_thread.start()

        custom_log.logger.info("---------------------------------------------------")

        while True:

            valid_direction = self.game_map.get_player_valid_directions()

            custom_log.logger.info("Input 'save'/'load' to save/load the game.")
            custom_log.logger.info(f"Valid directions - {valid_direction}")

            self.player.check_status(self.game_map)
            self.player.print_status()

            self.game_map.print_map()

            direction = DungeonInput.get_direction()

            if direction == "save":
                Serializer.save_map(self.game_map)
                continue

            elif direction == "load":
                new_game_map = Serializer.load_map()

                if new_game_map == "":
                    custom_log.logger.error("Failed to Load Game")
                    continue

                self.game_map = new_game_map
                continue


            if direction not in valid_direction:
                custom_log.logger.warning("Can't move there!")
                continue

            self.player.move(self.game_map, direction)

            custom_log.logger.info("---------------------------------------------------")

            if self.player.hp <= 0:
                self.end_game()
                break
            elif self.player.bag == Game.TREASURE_TO_WIN:
                self.win_game()
                break
        
        stop_flag.set()


    @decorators.info_decorator
    @decorators.debug_decorator
    def end_game(self):
        """
        Ends game prints map.

        :returns: None.
        :rtype: None.
        """
        custom_log.logger.info("You Lost!")
        self.game_map.print_map()


    @decorators.info_decorator
    @decorators.debug_decorator
    def win_game(self):
        """
        Wins game prints map.

        :returns: None.
        :rtype: None.
        """
        custom_log.logger.info("You Won!")
        self.game_map.print_map()


if __name__ == "__main__":
    game = Game()
    game.start()
