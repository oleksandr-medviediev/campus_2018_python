from random import randrange


def createMap():
    """
    Generate list of characters for game map.

    :param map_size: the size of game map.
    :type map_size: int.

    :return: list of characters for game map.
    :rtype: list.

    """
    map_size = get_map_size()

    matrix = []

    for i in range(map_size):
        line = ["_" for i in range(map_size)]
        matrix.append(line)
    
    traps_number = int((map_size ** 2) / 10)
    treasure_number = int((map_size ** 2) / 20)

    count = 0

    while True:
        row = randrange(map_size)
        column = randrange(map_size)

        if matrix[row][column] == "_":
            matrix[row][column] = "x"
            count += 1
        
        if count == traps_number:
            break

    count = 0

    while True:
        row = randrange(map_size)
        column = randrange(map_size)

        if matrix[row][column] == "_":
            matrix[row][column] = "$"
            count += 1
        
        if count == treasure_number:
            break

    return matrix
    

def get_map_size():
    """
    Generate size of map.

    :return: size of map.
    :rtype: int.

    """
    result_size = 0

    while True:
        result_size = int(input("Enter the map size [5-10]"))

        if (result_size >= 5) and (result_size <= 10):
            break

        print("Wrong! Enter correct size!")
    
    return result_size
