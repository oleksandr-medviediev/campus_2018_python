def verify_brackets(in_string):
    """
    checks if string has lexically-proper bracket usage
        :param str in_string: string to verify
        :return: boolean statement whether string has proper bracket alignment
        :rtype: bool
    """

    brackets_opposites = {
        '[': ']',
        '{': '}',
        '(': ')'
    }

    bracket_stack = []
    for ch in in_string:

        if ch in brackets_opposites:
            bracket_stack.append(brackets_opposites[ch])
        elif len(bracket_stack) > 0 and ch == bracket_stack[-1]:
            bracket_stack.pop()

    valid_brackets = len(bracket_stack) == 0

    return valid_brackets
