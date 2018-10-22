alphabet = 'abcdefghijklmnopqrstuvwxyz'

key_as_string = input('input key: ')

if not key_as_string.isdigit():
    print('wrong key')
    exit()

key = int(key_as_string)

input_string = input('input a string to cypher: ')

result = str()

for character in input_string:

    if not character.isalpha():
        result += character
        continue

    character_index = alphabet.index(character.lower())
    rotated_index = (character_index+key) % len(alphabet)

    if character.isupper():
        result += alphabet[rotated_index].upper()
    else:
        result += alphabet[rotated_index]

print(result)
