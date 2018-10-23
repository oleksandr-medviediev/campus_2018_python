def rle_cypher(input_string):
    encoded_string = str()
    inspect_char = input_string[0]
    characters = []
    numbers = []
    count = 0
    for char in input_string:
        if char != inspect_char:
            numbers.append(count)
            characters.append(inspect_char)
            inspect_char = char
            count = 1
            if input_string.index(char) == len(input_string) - 1:
                numbers.append(count)
                characters.append(inspect_char)
        else:
            count += 1
            
    result = str()
    for i in range(len(numbers)):
        result += '{}{}'.format(numbers[i],characters[i])

    return result

def rle_decypher(input_string):
    count = 0
    result = str()
    for char in input_string:
        if char.isdigit():
            count = count*10 + int(char)
        else:
            for i in range(count):
                result += char
            count = 0

    return result

            
