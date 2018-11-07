
bracket_start = ['[', '(', '{']
bracket_end = [']', ')', '}']

string = ''
str_len = 0
i = 0

def foo(bracket):
    global string
    global str_len
    global i

    while i < str_len:
        ch = string[i]
        i += 1
        if ch in bracket_start and foo(bracket_end[bracket_start.index(ch)]) == False:
            return False
        elif ch == bracket:
            return True

    result = True if bracket == '' else False
    return result

def verify_brackets(string_with_brackets):
    global string
    global str_len
    global i

    string = string_with_brackets
    str_len = len(string_with_brackets)
    i = 0

    result = foo('')
    return result

print(verify_brackets('Some string with parentheses( and brackets []'))
print(verify_brackets('Some string with parentheses( and brackets [])'))