import pickle
import custom_log

FILE_NAME = "game_map.sav"


def save_map(game_map):
    """
    Save Game map.

    :param game_map: game map.
    :game_map type: str.
    :returns: None.
    :rtype: None.
    """

    map_file = open(FILE_NAME,"wb")

    pickle.dump(game_map, map_file)

    custom_log.logger.info("Map Saved!")
    custom_log.logger.info("---------------------------------------------------")



def load_map():
    """
    Load Game map.

    :returns: Game Map.
    :rtype: str.
    """

    game_map = ""

    with open(FILE_NAME,"rb") as map_file:
        game_map = pickle.load(map_file)
        custom_log.logger.info("Map Loaded!")
        custom_log.logger.info("---------------------------------------------------")
    
    return game_map
