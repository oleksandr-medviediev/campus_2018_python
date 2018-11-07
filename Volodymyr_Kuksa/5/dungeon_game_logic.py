from dungeon_game_maps import GAME_CHARACTERS
from dungeon_game_serialization import SAVE_COMMAND, serialize

AVAILABLE_MOVES = {'up': (0, -1),
                   'down': (0, 1),
                   'left': (-1, 0),
                   'right': (1, 0)}

VECTORS_TO_ADJACENT_TILES = tuple(AVAILABLE_MOVES.values())

MOVE_NAMES = tuple(AVAILABLE_MOVES.keys())


def query_player_input():
    """
    Query player for next command and return the name of entered command.

    :return: name of requested move.
    :rtype: str.
    """
    move = input(f'\nWhere to go next? {MOVE_NAMES}, {SAVE_COMMAND}: ').lower()

    while not MOVE_NAMES.count(move) and move != SAVE_COMMAND:
        move = input('Wrong! Try again: ').lower()

    return move


def execute_player_move(map_size, player_x, player_y, move_name):
    """
    Apply move_name to player position and return the new position.

    :param map_size: size of the side of game map.
    :type map_size: int.

    :param player_x: x coordinate of the player.
    :type player_x: int.

    :param player_y: y coordinate of the player.
    :type player_y: int.

    :param move_name: name of the requested move.
    :type move_name: str.

    :return: new player position (x, y).
    :rtype: int, int.
    """
    new_x = player_x + AVAILABLE_MOVES[move_name][0]
    new_y = player_y + AVAILABLE_MOVES[move_name][1]

    if 0 <= new_x < map_size and 0 <= new_y < map_size:
        player_x, player_y = new_x, new_y
    else:
        print('That path is blocked!')

    return player_x, player_y


def check_end_game_condition(game_map, player_x, player_y):
    """
    Return False if game has finished, True otherwise.

    :param game_map: generated game map.
    :type game_map: square 2d list of single-character strings.

    :param player_x: x coordinate of the player.
    :type player_x: int.

    :param player_y: y coordinate of the player.
    :type player_y: int.

    :return: False if game has finished, True otherwise.
    :rtype: bool.
    """
    is_game_running = False
    player_tile = game_map[player_y][player_x]

    if player_tile == GAME_CHARACTERS['Treasure']:
        print('You Won!')
    elif player_tile == GAME_CHARACTERS['Trap']:
        print('You Lost(')
    else:
        is_game_running = True

    return is_game_running


def output_game_state(treasures, traps):
    """
    Output information about nearby treasures and traps.

    :param treasures: number of treasures in tiles, adjacent to the player.
    :type treasures: int.

    :param traps: number of traps in tiles, adjacent to the player.
    :type traps: int.

    :return: None.
    """
    if treasures == 1:
        print('There is a treasure nearby!')
    elif treasures:
        print('There are multiple treasures nearby!')

    if traps == 1:
        print('There is a trap nearby!')
    elif traps:
        print('There are multiple traps nearby!')

    if not treasures and not traps:
        print('There is nothing nearby.')


def update_game_state(game_map, player_x, player_y):
    """
    Update game state, and output it to the console.

    :param game_map: generated game map.
    :type game_map: square 2d list of single-character strings.

    :param player_x: x coordinate of the player.
    :type player_x: int.

    :param player_y: y coordinate of the player.
    :type player_y: int.

    :return: None.
    """
    map_size = len(game_map[0])
    treasures = 0
    traps = 0

    for vector in VECTORS_TO_ADJACENT_TILES:

        adjacent_x = player_x + vector[0]
        adjacent_y = player_y + vector[1]

        if not 0 <= adjacent_x < map_size or not 0 <= adjacent_y < map_size:
            continue

        adjacent_tile = game_map[adjacent_y][adjacent_x]

        if adjacent_tile == GAME_CHARACTERS['Treasure']:
            treasures += 1
        elif adjacent_tile == GAME_CHARACTERS['Trap']:
            traps += 1

    output_game_state(treasures, traps)


def mark_as_visited(game_map, x, y):
    """
    Mark tile of game_map with the coordinates(x, y) as visited if it is empty, do nothing otherwise.

    :param game_map: generated game map.
    :type game_map: square 2d list of single-character strings.

    :param x: x coordinate.
    :type x: int.

    :param y: y coordinate.
    :type y: int.

    :return: game_map with marked tile.
    :rtype: square 2d list of single-character strings.
    """
    if game_map[y][x] == GAME_CHARACTERS['Empty']:
        game_map[y][x] = GAME_CHARACTERS['Visited']

    return game_map


def run_game(game_map, player_x, player_y):
    """
    Execute game logic.

    :param game_map: generated game map.
    :type game_map: square 2d list of single-character strings.

    :param player_x: x coordinate of the player.
    :type player_x: int.

    :param player_y: y coordinate of the player.
    :type player_y: int.

    :return: None.
    """
    map_size = len(game_map)
    is_game_running = True

    game_map[player_y][player_x] = GAME_CHARACTERS['Spawn']

    while is_game_running:

        update_game_state(game_map, player_x, player_y)

        player_input = query_player_input()

        if player_input == SAVE_COMMAND:
            serialize(game_map, player_x, player_y)
        else:
            player_x, player_y = execute_player_move(map_size, player_x, player_y, player_input)

        is_game_running = check_end_game_condition(game_map, player_x, player_y)

        game_map = mark_as_visited(game_map, player_x, player_y)
