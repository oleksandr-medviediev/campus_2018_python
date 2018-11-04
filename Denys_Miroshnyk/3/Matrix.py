
def split_input(string):

    formatted_list = []
    no_endl_string = string.split('\n')

    for x in no_endl_string:
        temp = x.split()
        formatted_list.append(temp)

    return formatted_list


def read_matrix_rows(string):

    formatted_list = split_input(string)

    rows = []

    for x in formatted_list:

        rows.append(', '.join(list(x)))
        rows[-1] += '\n'

    return ''.join(rows)


def read_matrix_columns(string):

    formatted_list = split_input(string)
    transposed_list = list(map(list, zip(*formatted_list)))

    columns = []

    for x in transposed_list:

        columns.append(', '.join(x))
        columns[-1] += '\n'

    return ''.join(columns)


print(read_matrix_rows('9 8 7\n5 3 2\n6 6 7'))
# 9, 8, 7
# 5, 3, 2
# 6, 6, 7
print(read_matrix_columns('9 8 7\n5 3 2\n6 6 7'))
#  9, 5, 6
#  8, 3, 6
#  7, 2, 7
