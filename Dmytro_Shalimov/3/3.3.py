print("Given a string representing a matrix of numbers, return the rows and columns of that matrix.")


def split_input(string):
    """
    Splits given string on rows by '\n' symbol and removes spaces

    :param str string: input string
    :return: list of formatted strings
    :rtype: list
    """

    formatted_list = []
    no_endl_string = string.split('\n')

    for x in no_endl_string:
        temp = x.split()
        formatted_list.append(temp)

    return formatted_list



def read_matrix_rows(string):
    """
    Read matrix rows into string

    :param str string: matrix in string
    :return: string with rows separated with newlines
    :rtype: str 
    """

    formatted_list = split_input(string)

    rows = []

    for x in formatted_list:

        rows.append(', '.join(list(x)))
        rows[-1] += '\n'

    return ''.join(rows)


def read_matrix_columns(string):
    """
    Read matrix columns into string

    :param str string: matrix in string
    :return: string with columns separated with newlines
    :rtype: str 
    """

    formatted_list = split_input(string)
    transposed_list = list(map(list, zip(*formatted_list)))

    columns = []

    for x in transposed_list:

        columns.append(', '.join(x))
        columns[-1] += '\n'


    return ''.join(columns)
        

user_matrix = ''
user_input = input("Enter maxtrix row by row with spaces between elements(enter empty string when you are done): ")

while True:

    if len(user_input) > 0:
        user_matrix += user_input + '\n'

    else:
        break

    user_input = input("Enter maxtrix row by row with spaces between elements(enter empty string when you are done): ")

formatted_user_matrix = user_matrix[ : len(user_matrix) - 1]

print(read_matrix_rows(formatted_user_matrix))
print(read_matrix_columns(formatted_user_matrix))
