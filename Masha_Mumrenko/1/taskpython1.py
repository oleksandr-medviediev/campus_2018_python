import string
def if_xo_equal_string(string_check):
    string_to_check_casefold = string_check.lower()
    x_number = string_to_check_casefold.count('x')
    o_number = string_to_check_casefold.count('o')

    return (x_number==o_number)


