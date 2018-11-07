def read_matrix_rows(string):
    """Function build matrix from the string and return rows.

    Args:
        string: type str.

    Returns:
        Return str.

    """

    matrix = []
    tmp_matrix = []

    for i in string:
        if not i.isdigit():
            continue
        tmp_matrix.append(int(i))
        if len(tmp_matrix) == 3:
            matrix.append(tmp_matrix)
            tmp_matrix = []

    del(tmp_matrix)

    result_string = "{}\n{}\n{}".format(matrix[0], matrix[1], matrix[2])
    result_string = result_string.replace("[", "")
    result_string = result_string.replace("]", "")

    return result_string


def read_matrix_columns(string):
    """Function build matrix from the string and return columns.

    Args:
        string: type str.

    Returns:
        Return str.

    """
    matrix = []
    tmp_matrix = []

    for i in string:
        if not i.isdigit():
            continue
        tmp_matrix.append(int(i))
        if len(tmp_matrix) == 3:
            matrix.append(tmp_matrix)
            tmp_matrix = []

    result_matrix = []
    tmp_matrix = []

    count = 0
    for j in range(0, 3, 1):
        for i in range(0, 3, 1):
            tmp_matrix.append(matrix[i][j])
            if len(tmp_matrix) == 3:
                result_matrix.append(tmp_matrix)
                tmp_matrix = []

    del(tmp_matrix)
    del(matrix)

    result_string = "{}\n{}\n{}".format(result_matrix[0], result_matrix[1], result_matrix[2])
    result_string = result_string.replace("[", "")
    result_string = result_string.replace("]", "")

    return result_string


if __name__ == '__main__':
    result = read_matrix_rows('9 8 7\n5 3 2\n6 6 7')
    print(result)

    print("\n")

    result = read_matrix_columns('9 8 7\n5 3 2\n6 6 7')
    print(result)
