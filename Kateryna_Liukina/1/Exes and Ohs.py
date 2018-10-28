input_string = input('Enter a string\n')

input_string = input_string.lower()

x_counter = input_string.count('x')
o_counter = input_string.count('o')

print(x_counter == o_counter)
