import string
def ceasar_cipher():
    key = input("enter key")
    while not key.isdigit():
        key = input("enter key")
        
    input_string = input("Enter string to cypher")
    alphabet = string.ascii_lowercase

    result = str()

    for char in input_string:
        if not char.isalpha():
            result += char
        else:
            shifted_index = alphabet.index(char.lower()) + int(key)
            shifted_index %= len(alphabet)
            if char.isupper():
                result += alphabet[shifted_index].upper()
            else:
                result += alphabet[shifted_index]

    return result


