def verify_brackets(string):
    """
    Function verify brackets
    Args:
        string(str): string to verify brackets
    Returns:
        bool: return true if all brackets are closed and are in right order
    """
    brackets_opening = ('(', '[', '{')
    brackets_closing = (')', ']', '}')
    brackets_dict = dict(zip(brackets_opening, brackets_closing))

    bracket_stack = []

    for ch in string:
        if ch in brackets_opening:
            bracket_stack.append(ch)
        elif ch in brackets_closing:
            if ch == brackets_dict[bracket_stack[-1]]:
                bracket_stack.pop(-1)
            else:
                return False

    return(len(bracket_stack) == 0)
