brackets = {
    '{': '}',
    '[': ']',
    '(': ')'}


def verify_brackets(string):
    """verifies brackets in string

    Arguments:
        string {str} -- string that contains brackets

    Returns:
        bool -- True is brackets are correct
    """

    bracket_stack = [ch for ch in string if ch in brackets or ch in brackets.values()]
    bracket_stack.reverse()
    pair_stack = list()

    while bracket_stack:

        next = bracket_stack.pop()
        if next in brackets:
            pair_stack.append(brackets[next])
        elif pair_stack and next != pair_stack.pop():
            return False

    return not pair_stack


inp = input("enter text with brackets\n")

print(verify_brackets(inp))
