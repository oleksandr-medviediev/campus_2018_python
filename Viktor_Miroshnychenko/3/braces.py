def check_braces(string):
    """
    :param string: string to check
    :type string: str

    :return: True if all braces closed and False otherwise
    :rtype: bool
    """

    ret_val = True
    if string.count("(") != string.count(")"):
        ret_val = False
    elif string.count("[") != string.count("]"):
        ret_val = False
    elif string.count("{") != string.count("}"):
        ret_val = False
    else:
        braces1 = 0
        braces2 = 0
        braces3 = 0
        for char in string:
            if char == "[":
                braces1 += 1
            elif char == "]":
                braces1 -= 1
            elif char == "(":
                braces2 += 1
            elif char == ")":
                braces2 -= 1
            elif char == "{":
                braces3 += 1
            elif char == "}":
                braces3 -= 1

            if braces1 < 0 or braces2 < 0 or braces3 < 0:
                ret_val = False
                break

    return ret_val


print(check_braces("Some () string with[braces]"))
print(check_braces("Some () {string with[braces]"))
print(check_braces("[[]{{{(}})}]"))
