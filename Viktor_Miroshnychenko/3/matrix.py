def read_matrix_rows(string):
    """
    :pararm string: string representing matrix
    :type string: str

    :return: string of rows
    :rtype: str
    """

    ret_val = ""
    rows = string.split("\n")
    for row in rows:
        ret_val += row + "\n"
    ret_val = ret_val[:-1]
    
    return ret_val


def read_matrix_columns(string):
    """
    :pararm string: string representing matrix
    :type string: str

    :return: string of columns
    :rtype: str
    """

    ret_val = ""
    rows = string.split("\n")
    row_len = len(rows[0])//2 + 1
    pos = 0
    for it in range(row_len):
        for row in rows:
            ret_val += row[pos] + " "
        ret_val = ret_val[:-1]
        ret_val += "\n"
        pos += 2

    return ret_val

    
print(read_matrix_rows("9 8 7\n5 3 2\n6 6 7"))
print(read_matrix_columns("9 8 7\n5 3 2\n6 6 7"))
