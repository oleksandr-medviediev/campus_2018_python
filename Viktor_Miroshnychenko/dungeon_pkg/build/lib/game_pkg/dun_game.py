import time
import threading
import dungeon_logger
import dungeon_decorators
import dun_player
import dun_map
import dungeon_enemy
import dungeon_serializer
import dungeon_exception


class Game:

    def __init__(self):

        self.player = dun_player.Player()
        self.dun_map = dun_map.DungeonMap(5)
        self.enemy = dungeon_enemy.Enemy()
        self.closing = False

        dungeon_logger.logger.info('Default map size = 3\n')
        command = input("Press 'Y' to change map size\n")
        command.lower()
        if command == 'y':

            self.set_map_size()
        

    def set_map_size(self):
        """
        :description: created new map with user size
        """
        size = ""
        while size.isdigit() == False:

            size = input("Enter new map size\n")

        try:
            size = int(size)
        except ValueError as error:
            dungeon_logger.logger(f'ValueError: {error}')
        self.dun_map = dun_map.DungeonMap(size)


    def init_game(self):
        """
        :description: initialize required data for game
        """

        self.dun_map.set_player_on_map(self.player)
        self.enemy.position = dun_map.dungeon_map_generate.set_character_randomly(self.dun_map.dun_map)

    def enemy_update(self):

        while self.closing is False:
            time.sleep(1)
            self.enemy.process_move(self.dun_map)
            if self.enemy.position == self.player.position:

                self.enemy.attack(self.player)
                dungeon_logger.logger.info('You were attacked by enemy!')

    def run_game(self):
        """
        :description: run game frame
        """

        while self.player.hit_points > 0 and self.player.treasure_picked < 3:

            self.player.get_command()

            if self.player.command in dun_player.COMMANDS:

                try:
                    self.player.process_move(self.dun_map)
                except (dungeon_exception.CommandError, dungeon_exception.MapCageError) as error:
                    dungeon_logger.logger.info(f'Invalid Player command: {error}')
                
                self.dun_map.print_map()

            elif self.player.command in dun_player.MENU_COMMANDS:

                if self.player.command == 'save':

                    game = Game()
                    game.player = self.player
                    game.dun_map = self.dun_map
                    dungeon_serializer.serialize_dungeon_game(game)
                else:
                    
                    game = dungeon_serializer.deserialize_dungeon_game()
                    self.player = game.player
                    self.dun_game = game.dun_map

        self.closing = True
        if self.player.hit_points == 0:
            dungeon_logger.logger.info('You LOST')
        elif self.player.treasure_picked == 3:
            dungeon_logger.logger.info('You WON')


    def run(self):

        game_thread = threading.Thread(target=self.run_game)
        enemy_thread = threading.Thread(target=self.enemy_update)

        game_thread.start()
        enemy_thread.start()
        game_thread.join()
        enemy_thread.join()


game = Game()
game.init_game()
game.run()
