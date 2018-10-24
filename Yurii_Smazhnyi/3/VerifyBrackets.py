brackets_dict = {'[' : ']', '{' : '}', '(' : ')'}

def verify_brackets(string):

    """
    Verifies given string for correct open/close of brackets.

    @param string: string with brackets.
    @returns: result of verifying
    """

    unclosed_brackets = []

    for ch in string:

        if ch in brackets_dict.keys():

            unclosed_brackets.append(ch)

        elif ch in brackets_dict.values():

            try:

                bracket = unclosed_brackets.pop()

                if ch != brackets_dict[bracket]:
                    return False

            except IndexError:

                return False

            except KeyError:

                return False
    
    return unclosed_brackets == []


print(verify_brackets("[{{qwerty}]}"))
