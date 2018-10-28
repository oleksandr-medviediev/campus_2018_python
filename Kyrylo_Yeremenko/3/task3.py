"""
This script solves task 3.3 from Coding Campus 2018 Python course
(Matrix)
"""


def read_matrix(string):
    """
    Reads matrix from string and returns rows\columns tuple
    :param string: '\n'-embedded matrix string
    :return: Rows\columns tuple
    """

    rows = [[int(number) for number in row.split()] for row in string.split('\n')]
    columns = [[rows[row_index][col_index] for row_index in range(len(rows))] for col_index in range(len(rows[0]))]

    return rows, columns

