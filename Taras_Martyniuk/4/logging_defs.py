import logging  
import logging.config
import json


def config_logs():
    # they said it on the docs that dict config is cooler than file config, 
    # but i still wanted the config to stay in file.
    with open('log_config.json') as f:
        config_dict = json.load(f)
        logging.config.dictConfig(config_dict)


config_logs()

l = logging.getLogger('MY LOG')
l.debug('WOW! DEBUG')
l.info('OMG - INFO')


