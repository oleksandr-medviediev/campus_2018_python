print("Rotational cipher+")

def process_char(char, rotation, alphabet):
    index = alphabet.find(char)
    cipher_index = index + rotation

    if cipher_index > len(alphabet) - 1:
        cipher_index -= len(alphabet)

    return alphabet[cipher_index]

alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabet_upper = alphabet.upper()

rotation_count = int(input("Enter rotation count: "))

if rotation_count > len(alphabet) - 1:
    print("invalid rotation")

else:
    user_input = input("Enter string: ")
    output = str()

    for x in user_input:
        if x.isalpha() == True:
            if x.isupper() == True:
                output += process_char(x, rotation_count, alphabet_upper)

            else:
                output += process_char(x, rotation_count, alphabet)
                
        else:
            output += x

    print(output)
