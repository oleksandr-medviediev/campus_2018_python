text = input('input text:\n')

isFirstLetter = True

capitalized_text = ''

for character in text:
    
    if character == ' ':
        isFirstLetter = True
        capitalized_text += character
    elif isFirstLetter:
        capitalized_text += character.capitalize()
        isFirstLetter = False
    else:
        capitalized_text += character

print(capitalized_text)
