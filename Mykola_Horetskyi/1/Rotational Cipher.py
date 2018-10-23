alphabet = 'abcdefghijklmnopqrstuvwxyz'

key = input('input key: ')

if not key.isdigit():
    print('key is invalid')
else:
    key = int(key)

    text = input('input text: ')

    encrypted_text = ''

    for character in text:
        if not character.isalpha():
            encrypted_text += character
        else:
            index = alphabet.index(character.lower())
            shiftedIndex = (index + key) % len(alphabet)
            if character.isupper():
                encrypted_text += alphabet[shiftedIndex].upper();
            else:
                encrypted_text += alphabet[shiftedIndex]
            
    print(encrypted_text)
    
