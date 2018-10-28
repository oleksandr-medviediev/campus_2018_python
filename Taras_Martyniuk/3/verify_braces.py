def verify_braces(string):

    """
        :param string: string
        :returns: True if all pairs of brackets [], braces {}, parentheses () 
        are matched and nested correctly.
    """

    opening = '({['
    closing = ')}]'
    mapping = dict(zip(opening, closing))
    match_queue = []

    for ch in string:
        if ch in opening:
            match_queue.append(mapping[ch])
        elif ch in closing:
            if not match_queue or ch != match_queue.pop():
                return False
    return not match_queue

assert not verify_braces('___sss___   ()   [')
assert verify_braces('___sss((___  []  )){}')