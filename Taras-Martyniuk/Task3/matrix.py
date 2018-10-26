# def read_matrix_rows(matrix_str):

def parse_row(row):

    return [ int(digit) for digit in row.split(' ') ]


def parse_matrix(matrix_str):

    lines = matrix_str.splitlines()
    return [ parse_row(line) for line in lines]


def transpose(matrix):

    return list(zip(*matrix))


def matrix_to_str(matrix):

    """
        :param matrix: 
    """

    row_to_str = lambda row : " ".join(map(str, row))

    return "\n".join(map(row_to_str, matrix))


matrix_str = '9 8 7\n5 3 2\n6 6 7'
transposed_str = '9, 5, 6\n8, 3, 6\n7, 2, 7'
parsed = [[9, 8, 7], [5, 3, 2], [6, 6, 7]]
transposed = [(9, 5, 6), (8, 3, 6), (7, 2, 7)]

assert parse_matrix(matrix_str) == parsed
assert transpose(parsed) == transposed

assert matrix_to_str(parsed) == matrix_str
assert matrix_to_str(transposed) == transposed_str
