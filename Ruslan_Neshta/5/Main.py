from random import randint
from itertools import product

import MapGenerator
import View
import DungeonSaver
from DungeonLogger import main_logger


def check_game_over(player_position, world, trap, treasure):
    """
    Checks if game is over and returns message if its over

    :return: is game over, result message
    :rtype: tuple
    """

    main_logger.debug(f'started {player_position}, {world}, {trap}, {treasure}')
    is_over = False
    message = 'You in trap =/ You lose.'

    if world[player_position[0]][player_position[1]] == trap:
        is_over = True

    elif world[player_position[0]][player_position[1]] == treasure:
        is_over = True
        message = 'You captured the treasure! You won!'

    result = (is_over, message)
    main_logger.debug(f'ended {result}')
    return result


def try_player_move(player_position, index, bound, move):
    """
    Tries to move player in given direction

    :param player_position: list of coordinates that defines player position
    :param index: defines what coordinate from player_position we want to change
    :param bound: number that restricts player movement
    :param move: number that will be added to player_position if move is possible
    :return: true if moved
    :rtype: bool
    """

    main_logger.debug(f'started {player_position}, {index}, {bound}, {move}')
    if move > 0:
        succeeded = player_position[index] + move < bound
    else:
        succeeded = player_position[index] + move >= bound

    if succeeded:
        player_position[index] += move

    main_logger.debug(f'ended {succeeded}')
    return succeeded


def handle_player_move(world, player_position):
    """
    Changes map accordingly to user input

    :param world: world map
    :param player_position: position of player
    :return: new player position
    :rtype: list
    """

    main_logger.debug(f'started {world}, {player_position}')

    player_move_fail = 'Player can\'t make this move'
    user_input_fail = 'Invalid input'
    user_input_prompt = 'Choose where you want to move:\n\'u\' - up,\n\'d\' - down,\n\'l\' - left,\n\'r\' - right.\n\
Input move:'

    moves = {'u': (0, 0), 'd': (0, 1), 'l': (1, 0), 'r': (1, 1)}
    bounds = (0, len(world))

    player_moves = (-1, 1)
    is_valid = False

    possible_moves = {k: [index, bounds[axis], player_moves[axis]] for (k, (index, axis)) in moves.items()}

    while not is_valid:
        main_logger.info(user_input_prompt)
        move = input()

        if move not in moves:
            main_logger.info(user_input_fail)
            continue

        is_valid = try_player_move(player_position, *possible_moves[move])
        if not is_valid:
             main_logger.info(player_move_fail)

    main_logger.debug(f'ended {world}, {player_position}')
    return player_position


def setup_player_position(world, empty, player):
    """
    Randomizes player position on map

    :param world: map
    :param empty: empty field on which player can be spawned
    :param player: defines player
    :return: player position
    :rtype: list
    """

    main_logger.debug(f'started {world}, {empty}, {player}')
    position = [0, 0]
    is_valid = False

    while not is_valid:
        position[0] = randint(0, len(world) - 1)
        position[1] = randint(0, len(world) - 1)

        if world[position[0]][position[1]] == empty:
            is_valid = True
            world[position[0]][position[1]] = player

    main_logger.debug(f'ended {position}')
    return position


def is_around_of(pos, what, world):
    """
    Returns true if there is 'what' around of 'position'

    :param pos: list that defines coordinates
    :param what: searching item
    :param world: list of lists that defines world
    :return: true if there is wanted item
    :rtype: bool
    """

    main_logger.debug(f'started {pos}, {what}, {world}')
    comb = product((-1, 0, 1), (-1, 0, 1))
    size = len(world)

    squares = [(pos[0] + p[0], pos[1] + p[1]) for p in comb if 0 <= pos[0] + p[0] < size if 0 <= pos[1] + p[1] < size]
    result = set(map(lambda p: world[p[0]][p[1]] == what, squares))

    found = True in result
    main_logger.debug(f'ended {found}')
    return found


def generate_warnings_if_required(world, player_position, trap, treasure):
    """
    Generates warnings if required

    :param world: worlds map
    :param player_position: players position
    :param trap: defines trap
    :param treasure: defines treasure
    :return: nothing
    :rtype: None
    """

    main_logger.debug(f'started {world}, {player_position}, {trap}, {treasure}')
    is_trap = is_around_of(player_position, trap, world)
    is_treasure = is_around_of(player_position, treasure, world)

    View.warn_player(is_treasure, is_trap)
    main_logger.debug(f'ended {is_treasure}, {is_trap}')


def play_game(game_save={}):
    """
    Starts Dungeon game

    :param game_save: saved game state(if any)
    :return: nothing
    :rtype: None
    """

    main_logger.debug(f'started')
    empty_space = '~'
    explored_space = '.'
    trap = 'x'
    treasure = '$'
    player = '*'

    move_command = 'Move'
    save_command = 'Save'
    end_game_session = 'End'

    user_options = [move_command, save_command, end_game_session]
    user_prompt = '\n'.join(user_options)

    result = ''
    game_over = False

    if game_save == {}:
        game_world = MapGenerator.generate(10, empty=empty_space, trap=trap, treasure=treasure)
        player_coordinates = setup_player_position(game_world, empty_space, player)

    else:
        game_world = game_save['map']
        player_coordinates = game_save['player']

    old_player_coordinates = player_coordinates
    hidden = [trap, treasure]

    while not game_over:
        game_world[old_player_coordinates[0]][old_player_coordinates[1]] = explored_space
        game_world[player_coordinates[0]][player_coordinates[1]] = player

        old_player_coordinates = player_coordinates.copy()
        View.print_map_hide_secrets(game_world, hidden, empty_space)

        generate_warnings_if_required(game_world, player_coordinates, trap, treasure)

        main_logger.info(user_prompt)
        choice = input()

        if choice == move_command:
            handle_player_move(game_world, player_coordinates)

        elif choice == save_command:
            objects = {'map' : game_world, 'player' : player_coordinates}
            DungeonSaver.save_game(objects)

        elif choice == end_game_session:
            result = 'Game over'
            break

        else:
            main_logger.info('Invalid input')

        game_over, result = check_game_over(player_coordinates, game_world, trap, treasure)

    main_logger.info(result)
    View.print_map(game_world)
    main_logger.debug(f'ended {result}')


def main_menu():
    """
    Shows main menu and allows user to make choice

    :return: nothing
    :rtype: None
    """

    new_game = 'New'
    load_game = 'Load'
    exit_game = 'Exit'
    prompt = 'Choose one of options above:'
    save_not_found = 'There is no saved games'
    invalid_input = 'Invalid input'

    menu_items = [new_game, load_game, exit_game, prompt]
    quit_game = False

    main_logger.debug('program launched')
    while not quit_game:

        main_logger.info('\n'.join(menu_items))
        choice = input()

        if choice not in menu_items:
            main_logger.info(invalid_input)

        elif choice == new_game:
            play_game()

        elif choice == load_game:
            try:
                save = DungeonSaver.load_game()
                play_game(save)

            except FileNotFoundError:
                main_logger.info(save_not_found)

        else:
            quit_game = True

    main_logger.debug(f'ended')


if __name__ == "__main__":
    main_menu()
