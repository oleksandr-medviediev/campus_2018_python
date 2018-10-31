BRACKETS = ('(', ')', '{', '}', '[', ']')

BRACKET_PAIRS = {
    '(': ')',
    '{': '}',
    '[': ']'
}

OPENING_BRACKETS = tuple(BRACKET_PAIRS.keys())


def check_brackets(string):
    """
    Return True if string contains only properly matched brackets or no brackets at all, False otherwise.

    :param string: string that is being checked for matching brackets.
    :type string: str.

    :return: True if string contains only properly matched brackets or no brackets at all, False otherwise.
    :rtype: bool.
    """
    bracket_stack = []

    for c in (c for c in string if BRACKETS.count(c)):

        if not len(bracket_stack):
            bracket_stack.append(c)

        elif not (OPENING_BRACKETS.count(bracket_stack[-1]) and BRACKET_PAIRS[bracket_stack[-1]] == c):
            bracket_stack.append(c)

        else:
            bracket_stack.pop()

    return not len(bracket_stack)


test_str = '{([world])[hello]}'
print(check_brackets(test_str))
