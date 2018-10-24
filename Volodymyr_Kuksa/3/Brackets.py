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
    bracket_pairs = {'(': ')', '{': '}', '[': ']'}
    opening_brackets = tuple(bracket_pairs.keys())

    return opening_brackets.count(opening) and bracket_pairs[opening] == closing


def check_brackets(string):
    """
    Return True if string contains only properly matched brackets or no brackets at all, False otherwise.

    :param string: string that is being checked for matching brackets.
    :type string: str.

    :return: True if string contains only properly matched brackets or no brackets at all, False otherwise.
    :rtype: bool.
    """
    brackets = ('(', ')', '{', '}', '[', ']')

    only_brackets = [c for c in string if brackets.count(c)]

    i = 0

    while i < len(only_brackets) - 1:

        current_bracket = only_brackets[i]
        next_bracket = only_brackets[i + 1]

        if is_bracket_pair(current_bracket, next_bracket):

            del only_brackets[i:i + 2]

            i = 0

        else:

            i += 1

    return not len(only_brackets)
