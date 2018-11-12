from random import choice
from logger import m_logger


global mapsize
global game_map
game_map = []


def init():

    set_map_size()
    generate_map()


def generate_traps():

    traps_amount = mapsize * mapsize // 10
    m_logger.debug(f'map_generating: traps amount will be {traps_amount}')

    m_logger.debug(f'map_generating: start trap generating')

    traps = [choice(range(mapsize * mapsize)) for i in range(traps_amount)]    

    m_logger.debug(f'map_generating: traps generated')

    return traps


def generate_treasures():

    treasures_amount = mapsize * mapsize // 20
    m_logger.debug(f'map_generating: treasures amount will be {treasures_amount}')

    m_logger.debug(f'map_generating: start treasure generating')

    treasures = [choice(range(mapsize * mapsize)) for i in range(treasures_amount)]

    m_logger.debug(f'map_generating: treasures generated')

    return treasures


def generate_map():

    traps = generate_traps()
    treasures = generate_treasures()
    traps_replacement = [-1 for i in traps]
    treasures_replacement = [1 for i in treasures] 

    m_logger.debug(f'map_generating: start map generating')
    global game_map
    game_map = [ 0 for i in range(mapsize) for j in range(mapsize)]

    m_logger.debug(f'map_generating: empty map as list generated')

    for (trap, replacement) in zip(traps, traps_replacement):
        game_map[trap] = replacement

    m_logger.debug(f'map_generating: traps spawned on map')

    for (treasure, replacement) in zip(treasures, treasures_replacement):
        game_map[treasure] = replacement

    m_logger.debug(f'map_generating: start treasure generation')

    game_map = [ game_map [i * mapsize: (i + 1) * mapsize] for i in range(mapsize) ]

    m_logger.debug(f'map_generating: map splited in rows')


def spawn_player():

    player_position = choice(range(mapsize * mapsize))

    m_logger.debug(f'map_generating: player_position randomly generated {player_position}')

    row, col = player_position // mapsize, player_position % mapsize

    while game_map[row][col] == -1 or game_map[row][col] == 1:

        player_position = choice(range(mapsize * mapsize))
        row, col = player_position // mapsize, player_position % mapsize

        m_logger.debug(f'map_generating: player_position generated once more {player_position}')


    return row, col


def set_map_size():

    global mapsize

    m_logger.info("Enter size of game map: ")
    mapsize = input()

    while (not mapsize.isdigit()) or int(mapsize) < 5:

        m_logger.info("Something wrong entered\nTry again: ")
        mapsize = input()

    mapsize = int(mapsize)
