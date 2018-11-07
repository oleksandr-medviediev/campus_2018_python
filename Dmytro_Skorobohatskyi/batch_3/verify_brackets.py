def verify_brackets(string):

    """ Function verify closing of brackets, parentheses, braces.

        Args:
            string(str): a string containing brackets [], braces {},
            parentheses (), or any combination thereof

        Returns:
            bool: Return True if all brackets are closed, otherwise - False.

    """
    
    opening = ['(', '{', '[']
    closing = [')', '}', ']']

    corresponding = dict(zip(closing, opening))

    is_brackets_closed = True
    
    stack = []
    
    for i, el in enumerate(string):
        if el in opening:
            stack.append(el)
        elif el in closing:
            if (len(stack)):
                last_element = stack.pop()
                if last_element != corresponding[el]:
                    is_brackets_closed = False
                    break
            else:
                is_brackets_closed = False
                break

    if len(stack):
        is_brackets_closed = False
        
    return is_brackets_closed
