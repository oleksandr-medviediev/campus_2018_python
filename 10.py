import string

print("Rotational cipher+")

def process_char(char, rotation, alphabet):

    index = alphabet.find(char)
    cipher_index = index + rotation

    if cipher_index > len(alphabet) - 1:
        
        cipher_index -= len(alphabet)

    return alphabet[cipher_index]




alphabet = string.ascii_lowercase
alphabet_upper = string.ascii_uppercase

rotation_count = input("Enter rotation count: ")

if not rotation_count.isnumeric():

    print("invalid rotation")

else:

    rotation_count = int(rotation_count)

    if rotation_count > len(alphabet) - 1:

        print("invalid rotation")

    else:

        user_input = input("Enter string: ")
        output = str()

        for x in user_input:

            char = x
            if char.isalpha():

                if char.isupper():

                    char = process_char(char, rotation_count, alphabet_upper)

                else:

                    char = process_char(char, rotation_count, alphabet)
                    
            output += char

        print(output)
