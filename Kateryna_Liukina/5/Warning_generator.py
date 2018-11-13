from Game_logger import logger


def generate_warning(game_map, player_position, game_item):
    """
    Function generate warning for dungeon game
    Args:
        game_map(list(list(int))): game map
        player_position(list(int)): player position
        game_item(int): 1 - trap, 2 - treasure
    Returns:
        none
    """

    list_of_warnings =["", "There's a trap within one square!", "There's a treasure within one square!"]
    position = [max(0, player_position[0] - 1), max(0, player_position[1] - 1)]
    while position[0] < player_position[0] + 1 and position[0] < len(game_map):
        while position[1] < player_position[1] + 1 and position[1] < len(game_map[0]):
            if game_map[position[0]][position[1]] == game_item:
                logger.warning(list_of_warnings[game_item])
                return
            position[1] += 1
        position[0] += 1
