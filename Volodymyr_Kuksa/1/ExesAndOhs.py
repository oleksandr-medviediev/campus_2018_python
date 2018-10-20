input_string = input('input a string to check for amount of Exes and Ohs: ')

input_string = input_string.casefold()

print(input_string.count('x') == input_string.count('o'))
