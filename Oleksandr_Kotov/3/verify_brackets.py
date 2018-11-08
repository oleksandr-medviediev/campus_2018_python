def verify_brackets(string):
    """find if brackets in expression are put correctly"""

    brackets = []
    braces = []
    parentheses = []

    for char in string:

        if char == '(':
            parentheses.append(char)
        elif char == '{':
            braces.append(char)
        elif char == '[':
            brackets.append(char)
        elif char == ')':

            if (len(parentheses) == 0):
                return False
            else:
                parentheses.pop()

        elif char == '}':

            if (len(braces) == 0):
                return False
            else:
                braces.pop()

        elif char == ']':

            if (len(brackets) == 0):
                return False
            else:
                brackets.pop()

    closed_brackets = len(brackets) == 0
    closed_parentheses = len(parentheses) == 0
    closed_braces = len(braces) == 0

    correct = closed_brackets and closed_parentheses and closed_braces

    return correct
