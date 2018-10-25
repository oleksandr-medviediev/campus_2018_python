input_string = input('Enter a string\n')

input_string = input_string.lower()

x_counter = 0
o_counter = 0

for ch in input_string:
    if ch == 'x':
        x_counter += 1
    elif ch == 'o':
        o_counter += 1

print(x_counter == o_counter)