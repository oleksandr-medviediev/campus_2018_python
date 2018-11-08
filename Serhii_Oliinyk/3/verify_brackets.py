def verify_brackets(string):
    """Function verifies brackets in input string.

    Args:
        string: type str.

    Returns:
        Return True of False.

    """
    string_list = list(string)

    check_list = []
    for i in string_list:
        if (i == "(") or (i == "{") or (i == "["):
            check_list.append(i)
        elif (i == ")") and (len(check_list) > 0) and (check_list[len(check_list) - 1] == "("):
            check_list.pop()
        elif (i == "}") and (len(check_list) > 0) and (check_list[len(check_list) - 1] == "{"):
            check_list.pop()
        elif (i == "]") and (len(check_list) > 0) and (check_list[len(check_list) - 1] == "["):
            check_list.pop()

    result = True

    if len(check_list) > 0:
        result = False

    return result


if __name__ == '__main__':
    check = verify_brackets('Some string with parentheses( and brackets [])')
    print(check)
