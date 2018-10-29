def parse_matrix(matrix_str):
    """
    :param: matrix_str : string with each line a matrix row
    :returns: 2D array of matrix rows
    """
    lines = matrix_str.splitlines()
    parse_row = lambda row: [ int(digit) for digit in row.split(' ') ]
    return [ parse_row(line) for line in lines]


def transpose(matrix):
    """
        switches rows and colums 
        :param matrix: 2D array
    """
    # so cool!
    return list(zip(*matrix))


def matrix_to_str(matrix):
    """
        :param matrix: 2D array of rows
        :returns: string where each line is matrix row
    """
    row_to_str = lambda row : " ".join(map(str, row))
    return "\n".join(map(row_to_str, matrix))


read_matrix_rows = lambda matrix_str: matrix_to_str(parse_matrix(matrix_str))
read_matrix_cols = lambda matrix_str: matrix_to_str(transpose(parse_matrix(matrix_str)))


matrix_str = '9 8 7\n5 3 2\n6 6 7'
transposed_str = '9 5 6\n8 3 6\n7 2 7'
parsed = [[9, 8, 7], [5, 3, 2], [6, 6, 7]]
transposed = [(9, 5, 6), (8, 3, 6), (7, 2, 7)]

assert parse_matrix(matrix_str) == parsed
assert transpose(parsed) == transposed

assert read_matrix_rows(matrix_str) == matrix_str
assert read_matrix_cols(matrix_str) == transposed_str
