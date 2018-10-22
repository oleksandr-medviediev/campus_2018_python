input_string = input('input a string to determine if it is an isogram: ')

input_string = input_string.casefold()

for character in input_string:
    if character.isspace() or character == '-':
        continue

    if input_string.count(character) != 1:
        print(False)
        break

else:
    print(True)
