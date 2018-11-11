def brackets_match(first_bracket, second_bracket):
    '''
    Function used to test brackets
    :param first_bracket: a bracket '(', '[', '{'
    :param second_bracket: a bracket ')', ']', '}'
    :return: True is first bracket matches to a second one
    :type first_bracket: str
    :type second_bracket: str
    :rtype: bool
    '''
    bracket_map = {
        '{' : '}',
        '[' : ']',
        '(' : ')'
    }
    
    if first_bracket not in bracket_map.keys():
        result = False
    else:
        result = bracket_map[first_bracket] is second_bracket
    return result


def verify_brackets(string_with_brackets):
    '''
    Function verifies that any and all pairs of brackets are
    matched and nested correctly
    :param string_with_brackets: a string that contains brackets like
    {}, (), []
    :return: True if all brackets are matched and nested correctly, False
    otherwise
    :type string_with_brackets: str
    :rtype: bool
    '''
    brackets = ['(', ')', '{', '}', '[',']']
    only_brackets = [c for c in string_with_brackets if c in brackets]
    
    result = True
    if len(only_brackets) % 2 is 1:
        result = False
    else:
        number_of_brackets = len(only_brackets)
        for i in range(0, int(number_of_brackets / 2)):
            result = brackets_match(only_brackets[i], only_brackets[number_of_brackets - i - 1])
    return result


string_to_verify = input('String to verify: ')
print(verify_brackets(string_to_verify))
