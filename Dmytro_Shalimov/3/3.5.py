print("Given a string containing brackets [], braces {}, parentheses (), or any combination thereof,")
print("verify that any and all pairs are matched and nested correctly.")

BRACKETS = ['(', ')', '[', ']', '{', '}'] 
OPENING_BRACKETS_ID = {'(': 0, '[': 1, '{': 2}
CLOSING_BRACKETS_ID = {')': 0, ']': 1, '}': 2}

def process_bracket(char, stack):
    """
    Opening bracket is pushed into the given stack.
    Closing bracket: 
        if last bracket in stack has the same ID from opening brackets - last element is poped from stack,
        otherwise current bracket pushed into stack

    :param char: bracket
    :param list stack: list of current brackets
    :return: list of processed brackets
    :rtype: list 
    """

    opening_bracket_id = OPENING_BRACKETS_ID.get(char)
    closing_bracket_id = CLOSING_BRACKETS_ID.get(char)

    if opening_bracket_id != None:
        stack.append(opening_bracket_id)

    elif closing_bracket_id != None and len(stack) > 0:

        if stack[-1] == closing_bracket_id:
            stack.pop()

        else:
            stack.append(closing_bracket_id)

    return stack


def verify_brackets(string):
    """
    Function process brackets in given string to verify all pairs are matched and nested correctly

    :param str string: string constaining text with [], (), {} brackets
    :return: True if all brackets pair are placed corerctly and stack is empty, False otherwise
    :rtype: bool
    """

    stack = []

    for x in string:

        if x in BRACKETS:
            stack = process_bracket(x, stack)

    return len(stack) == 0


user_input = input("Enter string for brackets validation: ")

print(verify_brackets(user_input))
