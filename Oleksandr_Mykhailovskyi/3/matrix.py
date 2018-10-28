import re


def get_matrix(string_matrix):
    """
    Args:
        string_matrix (str): string that represents matrix.
    Return:
        [[str]...]
    """
    mlist = re.split('\n', string_matrix)
    matrix = [i.split() for i in mlist]

    return matrix


def transpose(matrix):
    """
    Transpose operation on given matrix. Tij = Tji.

    Args:
        matrix ([[str]...]): list of lists of strs
    Return:
        [[str]...]. Transposed matrix.
    """
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


def matrix_to_str(matrix):
    """
    Args:
        matrix ([[str]...]): list of lists of strs.
    Return:
        str. Matrix in str view.
    """
    mstr = ""
    for row in matrix:
        mstr += ' '.join(row)
        mstr += '\n'
    return mstr


mstr = "1 2 3\n4 5 6\n7 8 9"
matrix = get_matrix(mstr)
print(matrix_to_str(matrix))

transpose(matrix)
print(matrix_to_str(matrix))
