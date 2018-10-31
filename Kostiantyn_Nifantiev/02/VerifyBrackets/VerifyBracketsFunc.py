def test_parenthes(sequence_to_test):
    """
    Using list as stack to track all parentheses, brackets, braces openings and closings
    """
    test_stack = list()
    result = True

    opening = ['(', '[', '{']
    closing = [')', ']', '}']

    for char in sequence_to_test:

        if char in opening:

            test_stack.append(char)

        elif char in closing:

            if test_stack.pop() != opening[closing.index(char)]:

                result = False
                break

    return result
