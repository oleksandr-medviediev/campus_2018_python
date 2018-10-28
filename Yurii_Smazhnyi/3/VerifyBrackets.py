brackets_dict = {'[' : ']', '{' : '}', '(' : ')'}


def verify_brackets(string):
    """
    Verifies given string for correct open/close of brackets.

    :param string: string with brackets.
    :string type: str.
    :returns: result of verifying
    :rtype: bool.
    """

    unclosed_brackets = []
    result = True

    for ch in string:

        if ch in brackets_dict.keys():

            unclosed_brackets.append(ch)

        elif ch in brackets_dict.values():

            if len(unclosed_brackets) == 0:
                
                result = False
                break

            bracket = unclosed_brackets.pop()

            if bracket not in brackets_dict:

                result = False
                break

            if ch != brackets_dict[bracket]:
                return False
    
    return result


print(verify_brackets("{[{qwerty}]}"))
