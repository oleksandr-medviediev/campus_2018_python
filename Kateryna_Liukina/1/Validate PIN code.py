input_string = input('Enter a string\n')

acceptable_sizes = [4, 6]
acceptable_char = [str(i) for i in range(10)]

is_pin_validated = True

if len(input_string) not in acceptable_sizes:
    is_pin_validated = False

elif not input_string.isdigit():    
    is_pin_validated = False

print(is_pin_validated)
