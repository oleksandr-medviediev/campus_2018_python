string = input().replace(' ', '').replace('`', '')
is_isogram = len(set(string)) == len(string)
print(is_isogram)