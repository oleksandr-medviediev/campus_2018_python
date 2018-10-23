
string = input('Enter string: ')

is_valid_4pin = len(string) == 4 and string.isdigit()
is_valid_6pin = len(string) == 6 and string.isdigit()

print(is_valid_4pin or is_valid_6pin)
