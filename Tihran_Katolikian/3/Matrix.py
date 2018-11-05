import sys


def output_matrix(matrix_2D):
    '''
    Does formatted output of given matrix
    :param matrix_2D: matrix represented as a list of lists
    :type matrix_2D: a list of lists of integers
    '''
    for row in matrix_2D:
        for i in range(len(row)):
            if i < len(row) - 1:
                sys.stdout.write(f'{row[i]}, ')
            else:
                sys.stdout.write(f'{row[i]}\n')


def read_matrix_rows(matrix):
    '''
    Function prints rows of given matrix
    :param matrix: a string representation of matrix
    '''
    rows = matrix.split('\n')
    for i in range(len(rows)):
        rows[i] = rows[i].split(' ')

    output_matrix(rows)


def read_matrix_columns(matrix):
    '''
    Function prints columns of given matrix
    :param matrix: a string representation of matrix
    '''
    rows = matrix.split('\n')
    for i in range(len(rows)):
        rows[i] = rows[i].split(' ')

    # this is the best thing that exists in Python
    cols = list(zip(*rows))

    output_matrix(cols)


example = '9 8 7\n5 3 2\n6 6 7'
read_matrix_rows(example)
print('')
read_matrix_columns(example)
