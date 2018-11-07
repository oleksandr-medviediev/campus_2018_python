def fill_the_matrix(string, columns, matrix):
    """Function the matrix from the string.

    Args:
        string : type str,
        columns: type int,
        matrix: type list

    Returns:
        Return None,
        Out parameter: matrix
    """
    row_matrix = []

    for i in string:
        row_matrix.append(i)
        if len(row_matrix) == int(columns):
            matrix.append(row_matrix)
            row_matrix = []

    if(row_matrix):
        matrix.append(row_matrix)


def transpose_matrix(matrix, columns, rows, result_matrix):
    """Function the transpose the matrix.

    Args:
        matrix: type list
        columns: type int
        rows: type int
        result_matrix: type list

    Returns:
        Return None,
        Out parameter: result_matrix

    """
    row_matrix = []
    for i in range(columns):
        for j in range(rows):
            if i >= len(matrix[j]):
                break
            row_matrix.append(matrix[j][i])
        result_matrix.append(row_matrix)
        row_matrix = []


def encrypt(string):
    """Function encrypting data.

    Args:
        string : type str.

    Returns:
        Return str.

    """

    string = string.lower()
    string = string.replace(" ", "")
    string = string.replace(".", "")
    string = string.replace(",", "")
    string = string.replace("?", "")
    string = string.replace("!", "")

    rows = columns = 0
    index = 2

    while True:
        rows = index
        columns = len(string) / rows
        if (rows >= columns) and (columns - rows <= 1):
            break

        index += 1

    columns = round(columns)
    rows , columns = columns, rows

    matrix = []
    fill_the_matrix(string, columns, matrix)

    result_matrix = []
    transpose_matrix(matrix, columns, rows, result_matrix)

    result_string = ""
    for i in result_matrix:
        result_string += "".join(i)

    return result_string


def decrypt(string):
    """Function encrypting data.

    Args:
        string : type str.

    Returns:
        Return str.

    """
    rows = columns = 0
    index = 2

    while True:
        rows = index
        columns = len(string) / rows
        if (rows >= columns) and (columns - rows <= 1):
            break

        index += 1

    columns = round(columns)

    matrix = []
    fill_the_matrix(string, columns, matrix)

    result_matrix = []
    transpose_matrix(matrix, columns, rows, result_matrix)

    result_string = ""
    for i in result_matrix:
        result_string += "".join(i)

    return result_string


if __name__ == '__main__':
    result = encrypt("If man was meant to stay on the ground, god would have given us roots.")
    print(result)

    result2 = decrypt(result)
    print(result2)
