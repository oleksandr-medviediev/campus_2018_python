import logging
import logging.config
from DungeonGame import DungeonGame


LOG_FILE_NAME = 'DungeonGameLogger.config'
logging.config.fileConfig(LOG_FILE_NAME)

logging.debug('Game start')

dungeon_game = DungeonGame()
dungeon_game.process_game_start()

should_run = True
while should_run:
    dungeon_game.run_game()
    should_run = dungeon_game.should_run()

logging.debug('Game end')
