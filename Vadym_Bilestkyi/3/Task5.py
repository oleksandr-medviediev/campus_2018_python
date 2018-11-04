closing_to_opening_map = {
    ')': '(',
    '}': '{',
    ']': '[',
}


def verify_brackets(string):
    stack = []
    for letter in string:
        if letter in closing_to_opening_map.values():
            stack.append(letter)
        elif letter in closing_to_opening_map.keys():
            if len(stack) == 0 or stack.pop() != closing_to_opening_map[letter]:
                return False

    return len(stack) == 0


print(verify_brackets('d{[{d(d)d}]}'))
