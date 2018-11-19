import dungeon_game_generate
import dun_player


GAME_STATE = ['lost', 'won', 'ingame']
COMMANDS = ['r', 'l', 'u', 'd']
WARNINGS = {'bomb':'Bomb is near you!',
            'treasue':'Tresure is near you'}


class dungeon_map:

    def __init__(self, size):
        """
        :param size: size of  the square map
        :type size: int
        """
        
        self.dun_map = dungeon_game_generate.generate_map(size)


    def set_player_on_map(self, player):
        """
        :param player: player that must be set on the map
        :type player: Player

        :return: player position in a map
        :rtype: list[x,y]
        """

        ret_val = dungeon_game_generate.set_player_randomly(dun_map)

        return ret_val


    def procces_move(player):
        """
        :param player: player that must make a move
        :type player: Player
        """
    
