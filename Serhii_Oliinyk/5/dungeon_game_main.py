import dungeon_game_map as mp
import dungeon_game_logic as logic
import dungeon_game_logger as log


def spawn_player(my_map):
    """
    Spawn player and add his position to the map.

    :param my_map: list of game map.
    :type my_map: list.

    :return: list of player position.
    :rtype: list.

    """
    size = len(my_map)
    player_position = []

    while True:
        column = mp.randrange(size)
        row = mp.randrange(size)

        if my_map[row][column] == '_':
            my_map[row][column] = "p"
            player_position.append(row)
            player_position.append(column)
            break

    return player_position


if __name__ == '__main__':
    debug_option = int(input("Press 1 activate Debug mode"))
    if(debug_option == 1):
        log.DEBUGMODE = True

    option = int(input("Press 1 to create new game and press 2 to load game state"))
    my_map = []
    position = [0, 0]

    if option == 1:
        my_map = mp.createMap()
        position = spawn_player(my_map)
    elif option == 2:
        position = logic.io.load_file(my_map)
    
    result = logic.run_game(my_map, position)
    if result:
        log.log_data("You win!")
    else:
        log.log_data("You lose!")

    for i in my_map:
        print(i)
