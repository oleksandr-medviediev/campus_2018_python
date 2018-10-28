BRACKETS = ('(', ')', '{', '}', '[', ']')

BRACKET_PAIRS = {
    '(': ')',
    '{': '}',
    '[': ']'
}

OPENING_BRACKETS = tuple(BRACKET_PAIRS.keys())


def is_bracket_pair(opening, closing):
    """
    Return True if opening and closing is a pair of matching brackets, False otherwise.

    :param opening: an opening bracket.
    :type opening: single-character str.

    :param closing: a closing bracket.
    :type closing: single-character str.

    :return: True if opening and closing is a pair of matching brackets, False otherwise.
    :rtype: bool.
    """
    return OPENING_BRACKETS.count(opening) and BRACKET_PAIRS[opening] == closing


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

        if not len(bracket_stack) or not is_bracket_pair(bracket_stack[-1], c):
            bracket_stack.append(c)
        else:
            bracket_stack.pop()

    return not len(bracket_stack)


test_str = '{([world])[hello]}'
print(check_brackets(test_str))
