import dungeon_game_maps
import dungeon_game_logic


def query_map_size():
    """
    Query player for the size of the game map and return integer representing player's input.

    :return: game map size.
    :rtype: int.
    """
    size = input('Enter map size (5 - 20): ')

    while not size.isdigit() or not 5 <= int(size) <= 20:
        size = input('Wrong! Try again: ')

    return int(size)


if __name__ == '__main__':

    map_size = query_map_size()
    game_map = dungeon_game_maps.generate_map(map_size)
    dungeon_game_logic.run_game(game_map)
    dungeon_game_maps.game_map_to_string(game_map)
