import logging.config
from dungeon_game import DungeonGame

logging.config.fileConfig('dungeon_game_logger.config')

if __name__ == '__main__':

    game = DungeonGame()

    game.run_game()
