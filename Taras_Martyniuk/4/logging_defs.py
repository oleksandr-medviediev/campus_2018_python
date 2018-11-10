import logging  
import logging.config
import json


# they said it on the docs that dict config is cooler than file config, 
# but i still wanted the config to stay in file.
with open('log_config.json') as f:
    config_dict = json.load(f)
    logging.config.dictConfig(config_dict)


LOGGER_NAME = 'Dungeon Log'
dungeon_logger = logging.getLogger(LOGGER_NAME)

dungeon_logger.debug('Inited dungeon logger')
