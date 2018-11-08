def verify_brackets(string):
    """
    Checks the correct nesting of brackets, braces and parentheses in string

Args:
    string (str) string which is checked

Returns:
    (bool) whether brackets, braces and parentheses are nested correctly
    """

    brackets = {"(":")" ,"[":"]", "{":"}"}

    result = all([string.count(key) == string.count(value)
                  for key, value in brackets.items()])
    
    if not result:
        return result

    open_brackets = []

    for character in string:
        
        if character in brackets.keys():
            open_brackets.append(character)
            
        elif character in brackets.values():
            
            if character == brackets[open_brackets[-1]]:
                open_brackets.pop()
                
            else:
                result = False
                break;

    if result and open_brackets:
        result = False

    return result
