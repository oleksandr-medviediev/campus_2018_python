def read_matrix_rows(string):
    """
    Reads rows of matrix and returns matrix printed in line

    :param string: matrix in rows, separated by newline symbol
    :return: printed matrix
    :rtype: str
    """
    rows = string.split("\n")
    matrix = []

    for el in rows:
        matrix.append(el.split(" "))

    normal_matrix = matrix
    matrix = []

    for el in normal_matrix:
        matrix.append(" ".join(el))

    matrix_string = "\n".join(matrix)
    return matrix_string


def read_matrix_columns(string):
    """
    Reads columns of matrix and returns matrix printed in line

    :param string: matrix in columns, separated by newline symbol
    :return: printed matrix
    :rtype: str
    """
    columns = string.split("\n")
    matrix = []

    for el in columns:
        matrix.append(el.split(" "))

    normal_matrix = list(zip(*matrix))
    matrix = []

    for el in normal_matrix:
        matrix.append(" ".join(el))

    matrix_string = "\n".join(matrix)
    return matrix_string


if __name__ == "__main__":
    line_of_text = '1 2 3\n4 5 6\n7 8 9'

    res = read_matrix_rows(line_of_text)
    print("Rows:", res, sep="\n")

    res = read_matrix_columns(line_of_text)
    print("Columns:", res, sep="\n")
