def verify(string):
    """
    Verifies brackets, braces and parentheses

    :param string: text

    :return: is brackets/braces/parentheses matched
    :rtype: bool
    """

    stack = []
    is_valid = True

    for ch in string:

        if ch == '(' or ch == '[' or ch == '{':
            stack.append(ch)
        elif ch == ')' or ch == ']' or ch == '}':

            if len(stack) == 0:
                is_valid = False
                break

            else:
                if ch == ')' and stack[-1] == '(' or ch == ']' and stack[-1] == '[' or ch == '}' and stack[-1] == '{':
                    stack.pop(-1)
                else:
                    stack.append(ch)

    else:
        is_valid = len(stack) == 0

    return is_valid


if __name__ == "__main__":
    line = 'Some string with parentheses( and brackets [])'
    is_line_valid = verify(line)
    print(is_line_valid)
