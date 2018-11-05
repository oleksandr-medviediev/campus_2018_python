from random import randint

import MapGenerator
import View


def check_game_over(player_position, world, trap, treasure):
    """
    Checks if game is over and returns message if its over

    :return: is game over, result message
    :rtype: tuple
    """

    is_over = False
    message = 'You in trap =/ You lose.'

    if world[player_position[0]][player_position[1]] == trap:
        is_over = True

    elif world[player_position[0]][player_position[1]] == treasure:
        is_over = True
        message = 'You captured the treasure! You won!'

    result = (is_over, message)
    return result


def handle_user_input(world, player_position):
    """
    Changes map accordingly to user input

    :param world: world map
    :param player_position: position of player
    :return: new player position
    :rtype: list
    """

    moves = ['u', 'd', 'l', 'r']
    is_valid = False

    offset_position = [0, 0]

    while not is_valid:
        move = input(
            'Choose where you want to move:\n\'u\' - up,\n\'d\' - down,\n\'l\' - left,\n\'r\' - right. Input move:')

        if move in moves:
            is_valid = True
        else:
            print('Invalid input')
            continue

        if move == 'u':
            if player_position[0] == 0:
                print('Player can\'t make this move')
                is_valid = False
            else:
                offset_position[0] -= 1

        elif move == 'l':
            if player_position[1] == 0:
                print('Player can\'t make this move')
                is_valid = False
            else:
                offset_position[1] -= 1

        elif move == 'r':
            if player_position[1] == len(world) - 1:
                print('Player can\'t make this move')
                is_valid = False
            else:
                offset_position[1] += 1

        elif move == 'd':
            if player_position[0] == len(world) - 1:
                print('Player can\'t make this move')
                is_valid = False
            else:
                offset_position[0] += 1

    player_position = add_lists(player_position, offset_position)
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

    position = [0, 0]
    is_valid = False

    while not is_valid:
        position[0] = randint(0, len(world) - 1)
        position[1] = randint(0, len(world) - 1)

        if world[position[0]][position[1]] == empty:
            is_valid = True
            world[position[0]][position[1]] = player

    return position


def square_is(position, expected, world):
    """
    Checks if square is expected, if position is invalid return False

    :param position: position
    :param expected: expected item on given position
    :param world: where to check
    :return: is it expected
    :rtype: bool
    """

    result = False
    size = len(world) - 1

    if size >= position[0] >= 0 and size >= position[1] >= 0:
        result = world[position[0]][position[1]] == expected

    return result


def add_lists(first, second):
    """
    Adds two lists and returns new

    :param first: list
    :param second: list
    :return: list
    :rtype: list
    """

    copy = []
    for (i, j) in zip(first, second):
        i += j
        copy.append(i)

    return copy


def sub_lists(first, second):
    """
    Subs two lists returns new

    :param first: list
    :param second: list
    :return: list
    :rtype: list
    """

    copy = []
    for (i, j) in zip(first, second):
        i -= j
        copy.append(i)

    return copy


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

    x_pos = [0, 1]
    y_pos = [1, 0]
    first_diagonal = [1, 1]
    second_diagonal = [1, -1]

    is_trap = False
    is_treasure = False

    if square_is(add_lists(player_position, x_pos), trap, world) or \
            square_is(sub_lists(player_position, x_pos), trap, world) or \
            square_is(add_lists(player_position, y_pos), trap, world) or \
            square_is(sub_lists(player_position, y_pos), trap, world) or \
            square_is(sub_lists(player_position, first_diagonal), trap, world) or \
            square_is(add_lists(player_position, first_diagonal), trap, world) or \
            square_is(sub_lists(player_position, second_diagonal), trap, world) or \
            square_is(add_lists(player_position, second_diagonal), trap, world):
        is_trap = True

    if square_is(add_lists(player_position, x_pos), treasure, world) or \
            square_is(sub_lists(player_position, x_pos), treasure, world) or \
            square_is(add_lists(player_position, y_pos), treasure, world) or \
            square_is(sub_lists(player_position, y_pos), treasure, world) or \
            square_is(add_lists(player_position, first_diagonal), treasure, world) or \
            square_is(sub_lists(player_position, first_diagonal), treasure, world) or \
            square_is(add_lists(player_position, second_diagonal), treasure, world) or \
            square_is(sub_lists(player_position, second_diagonal), treasure, world):
        is_treasure = True

    View.warn_player(is_treasure, is_trap)


def play_game():
    """
    Starts Dungeon game

    :return: nothing
    :rtype: None
    """

    empty_space = '~'
    trap = 'x'
    treasure = '$'
    player = '*'

    result = ''
    game_over = False
    game_world = MapGenerator.generate(10, empty=empty_space, trap=trap, treasure=treasure)

    new_player_coordinates = setup_player_position(game_world, empty_space, player)
    player_coordinates = new_player_coordinates
    hidden = [trap, treasure]

    while not game_over:
        game_world[player_coordinates[0]][player_coordinates[1]] = empty_space
        game_world[new_player_coordinates[0]][new_player_coordinates[1]] = player

        player_coordinates = new_player_coordinates
        View.print_map_hide_secrets(game_world, hidden, empty_space)

        generate_warnings_if_required(game_world, player_coordinates, trap, treasure)

        new_player_coordinates = handle_user_input(game_world, player_coordinates)
        game_over, result = check_game_over(new_player_coordinates, game_world, trap, treasure)

    print(result)
    View.print_map(game_world)


if __name__ == "__main__":
    play_game()
