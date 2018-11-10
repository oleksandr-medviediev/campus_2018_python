import logging  
import logging.config
import json


# they said it on the docs that dict config is cooler than file config, 
# but i still wanted the config to stay in file.
with open('log_config.json') as f:
    config_dict = json.load(f)
    logging.config.dictConfig(config_dict)


DEBUG_NAME = 'Debug Log'
OUTPUT_NAME = 'Output Log'

# for tracing debug info, writes to console and file, more heavy on message metadata 
debug_logger = logging.getLogger(DEBUG_NAME)
# for writing output to user - outputs message to console and file, with no metadata
output_logger = logging.getLogger(OUTPUT_NAME)

debug_logger.debug('Inited loggers')
