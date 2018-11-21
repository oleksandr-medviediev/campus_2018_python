import json


config_filename = 'dungeon_game_config.json'
IS_DEBUG_MODE = None
PLAYER_HP = None
NUMBER_OF_TREASURES_TO_WIN = None

def load_config():
    '''
    The function is used to load config variables from a JSON file. This function will be executed only once when file
    will be firstly imported.
    '''
    with open(config_filename, 'r') as config_file:
        config_variables = json.load(config_file)
        # is there some way to not write string rep of this variable?
        global IS_DEBUG_MODE
        global PLAYER_HP
        global NUMBER_OF_TREASURES_TO_WIN
        IS_DEBUG_MODE = config_variables['IS_DEBUG_MODE']
        PLAYER_HP = config_variables['PLAYER_HP']
        NUMBER_OF_TREASURES_TO_WIN = config_variables['NUMBER_OF_TREASURES_TO_WIN']


load_config()
