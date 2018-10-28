def verify(sequence):
    """
    Verify that all brackets match.

    Args:
        sequence (str): str to verify.

    Returns:
        True if all brackets match. False otherwise.
    """
    opening = ("(", "[", "{")
    closing = (")", "]", "}")

    brackets = []
    for i in sequence:
        if i in opening:
            brackets.append(i)
        elif i in closing and brackets[-1] != opening[closing.index(i)]:
            return False
        elif i in closing and brackets[-1] == opening[closing.index(i)]:
            brackets.pop()
    if len(brackets) == 0:
        return True
    return False


def verify_ver2(sequence):
    """
    Verify that all brackets match.

    Args:
        sequence (str): str to verify.

    Returns:
        True if all brackets match. False otherwise.
    """
    opening = ("(", "[", "{")
    closing = (")", "]", "}")
    brackets_list = [i for i in sequence if i in opening or i in closing]

    if len(brackets_list) % 2 != 0:
        return False

    index = (len(brackets_list) >> 1) - 1
    while index > 0:
        bracket = brackets_list[index]
        next_bracket = brackets_list[index + 1]
        if bracket in opening and next_bracket in closing:
            if opening.index(bracket) == closing.index(next_bracket):
                brackets_list.pop(index)
                brackets_list.pop(index + 1)
            else:
                return False
        else:
            return False
        index -= 1
    return True


test_string = input()
print("Results(2 functions): ")
print(verify(test_string))
print(verify_ver2(test_string))
