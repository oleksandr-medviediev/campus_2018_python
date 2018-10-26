string = input()

def get_mid_char (string):
    if len(string) == 0:
        return ''
    elif len(string) % 2 != 0:
        return string[len(string) // 2]
    else:
        ind = len(string) // 2
        return string[ind - 1 : ind + 1]

print(get_mid_char(string))
    