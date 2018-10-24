import string


print("Rotational cipher+")

alphabet = string.ascii_lowercase
alphabet_upper = string.ascii_uppercase

def process_char(char, rotation):

    curr_alphabet = alphabet

    if char.isupper():

        curr_alphabet = alphabet_upper
    
    index = curr_alphabet.find(char)
    cipher_index = index + rotation

    if cipher_index > len(curr_alphabet) - 1:
        
        cipher_index -= len(curr_alphabet)

    return curr_alphabet[cipher_index]



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

            if x.isalpha():
                    
                output += process_char(x, rotation_count)

            else:

                output += x

        print(output)
