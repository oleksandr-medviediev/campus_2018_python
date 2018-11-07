def save_game(my_map):
    """
    save game state in the file.

    :param my_map: the list of game map.
    :type my_map: list.

    :rtype: None

    """

    save_file = open("file.txt", "w")

    for i in my_map:
        string = ' '.join(i) + " \n"
        save_file.write(string)

    save_file.close()   


def load_file(my_map):
    """
    load game state from the file.

    :param my_map: the list of game map.
    :type my_map: list.

    :return player_position: the list of player position.
    :rtype player_position: list.

    """
    load_file = open("file.txt", "r")
    
    data = load_file.readlines()
    load_file.close()

    player_position = []

    for i in range(len(data)):
        line = list(data[i].split(' '))
        line.pop()

        if "p" in line:
            player_position = [i, line.index("p")]

        my_map.append(line)

    return player_position
