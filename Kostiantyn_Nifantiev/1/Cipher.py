plain_alphabet = 'abcdefghijklmnopqrstuvwxyz'
upper_plain_alphabet = plain_alphabet.upper()

while True:

    shift = int(input('Enter shift key: '))
    shift %= 26

    rotated_alphabet = plain_alphabet[shift : len(plain_alphabet)] + plain_alphabet[0 : shift]
    upper_rotated_alphabet = rotated_alphabet.upper()

    dictionary = {}

    for i in range(len(plain_alphabet)):

        dictionary[plain_alphabet[i]] = rotated_alphabet[i]
        dictionary[upper_plain_alphabet[i]] = upper_rotated_alphabet[i]

    #print(dictionary) #It is for debug

    incoming_string = input('Enter your message to chipher: ')
    ciphered_string = ''

    for char in incoming_string:

        if char.isalpha():

            ciphered_string += dictionary[char]

        else:

            ciphered_string += char

    print(ciphered_string)
