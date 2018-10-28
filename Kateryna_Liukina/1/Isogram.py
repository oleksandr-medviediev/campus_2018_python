input_string = input('Enter a string\n')

is_isogram = True

exeption_char = [' ', '-']

for i in range(len(input_string)):
    if input_string[i] in exeption_char:
        continue
    if input_string.find(input_string[i], i + 1) > 0:
        is_isogram = False
        break

print(is_isogram)
