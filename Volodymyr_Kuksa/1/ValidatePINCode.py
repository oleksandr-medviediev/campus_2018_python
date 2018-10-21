input_string = input("enter PIN code to validate it: ")

is_valid_length = len(input_string) == 4 or len(input_string) == 6

if input_string.isdigit() and is_valid_length:
    print(True)
else:
    print(False)

