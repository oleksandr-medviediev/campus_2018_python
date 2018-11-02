closing_to_opening_map = {
    ')': '(',
    '}': '{',
    ']': '[',
}


def verify_brackets(string):
    stack = []
    for letter in string:
        if letter in ('{', '(', '['):
            stack.append(letter)
        elif letter in ('}', ')', ']'):
            if len(stack) == 0 or stack.pop() != closing_to_opening_map[letter]:
                return False

    return len(stack) == 0


print(verify_brackets('d{[{d(d)d}]}'))
