input_string = input('Enter a string\n')

words = [word.capitalize() for word in input_string.split()]

output_string = ' '.join(words)
print(output_string)
