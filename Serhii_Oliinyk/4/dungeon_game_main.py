import dungeon_game_map as map
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
        column = map.randrange(size)
        row = map.randrange(size)

        if my_map[row][column] == '_':
            my_map[row][column] = "p"
            player_position.append(row)
            player_position.append(column)
            break

    return player_position


if __name__ == '__main__':
    option = int(input("Press 1 to create new game and press 2 to load game state"))
    my_map = []
    position = [0, 0]

    if option == 1:
        my_map = map.createMap()
        position = spawn_player(my_map)
    elif option == 2:
        position = logic.io.load_file(my_map)
    
    result = logic.run_game(my_map, position)
    if result:
        log.logger.info("You win!")
    else:
        log.logger.info("You lose!")

    for i in my_map:
        print(i)
