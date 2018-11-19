import json


config_filename = 'dungeon_game_config.json'
IS_DEBUG_MODE = None

def load_config():
    '''
    The function is used to load config variables from a JSON file. This function will be executed only once when file
    will be firstly imported.
    '''
    with open(config_filename, 'r') as config_file:
        config_variables = json.load(config_file)
        # is there some way to not write string rep of this variable?
        global IS_DEBUG_MODE
        IS_DEBUG_MODE = config_variables['IS_DEBUG_MODE']


load_config()
