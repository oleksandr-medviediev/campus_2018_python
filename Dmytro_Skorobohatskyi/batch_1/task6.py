string = input('enter the string\n')

length = len(string)

is_lenght_right = length == 4 or length == 6
is_pin_valid = is_lenght_right and string.isdigit()

print(is_pin_valid)
