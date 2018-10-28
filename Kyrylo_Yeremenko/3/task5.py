"""
This script solves task 3.5 from Coding Campus 2018 Python course
(Verify brackets)
"""

brackets = \
    {
        '{': '}',
        '[': ']',
        '(': ')'
    }


def verify_brackets(string):
    """
    Verify that all brackets in string are paired and matched correctly
    :param string: Input string containing brackets
    :return: True/False depending on bracket validity
    """

    bracket_stack = [character for character in string if character in brackets or character in brackets.values()]
    bracket_stack.reverse()
    pair_stack = []

    while bracket_stack:

        next_item = bracket_stack.pop()
        if next_item in brackets:
            pair_stack.append(brackets[next_item])
        elif pair_stack and next_item != pair_stack.pop():
            return False

    return not pair_stack

