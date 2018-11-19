import pickle
import custom_log
import decorators


class Serializer:


    FILE_NAME = "game_map.sav"


    @decorators.info_decorator
    @decorators.debug_decorator
    @staticmethod
    def save_map(game_map):
        """
        Save Game map.

        :param game_map: game map.
        :game_map type: str.
        :returns: None.
        :rtype: None.
        """

        map_file = open(Serializer.FILE_NAME,"wb")

        pickle.dump(game_map, map_file)

        custom_log.logger.info("Map Saved!")
        custom_log.logger.info("---------------------------------------------------")


    @decorators.info_decorator
    @decorators.debug_decorator
    @staticmethod
    def load_map():
        """
        Load Game map.

        :returns: Game Map.
        :rtype: str.
        """

        game_map = ""

        with open(Serializer.FILE_NAME,"rb") as map_file:
            game_map = pickle.load(map_file)
            custom_log.logger.info("Map Loaded!")
            custom_log.logger.info("---------------------------------------------------")
        
        return game_map
