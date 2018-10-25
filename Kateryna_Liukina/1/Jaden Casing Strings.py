input_string = input('Enter a string\n')

words = input_string.split()

for i in range(len(words)):
    words[i] = words[i].capitalize()

output_string = ' '.join(words)
print(output_string)
