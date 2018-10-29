from random import randint


MAX_RAND_COEF = 27
CLEAR_COEF = 18
BOMB_COEF = 24

def generate_map(size):
    """
    :param size: size of the map size
    :rtype size: int
    
    :return: genarate map with 0 as regular cage, ! as bomb cage and # astreasue case
    :rtype: list[list[]]
    """

    ret_map = []
    for height in range(size):
        row = []
        
        for width in range(size):
            
            coef = randint(0, MAX_RAND_COEF)
            if coef < CLEAR_COEF:
                row.append("0")
            elif coef < BOMB_COEF:
                row.append("!")
            else:
                row.append("#")

        ret_map.append(row)

    return ret_map


def set_player_randomly(dung_map):
    """
    :param dung_map: map that player must be placed on
    :type dung_map: list[list[]]

    :return: player position in a map
    :rtype: list[x,y]
    """

    map_size = len(dung_map)
    x = randint(0, map_size)
    y = randint(0, map_size)
    while(dung_map[x][y] != "0"):
        x = randint(0, map_size)
        y = randint(0, map_size)

    return [x,y]



    
