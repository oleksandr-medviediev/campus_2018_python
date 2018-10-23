text = input('input text:\n')

textLength = len(text)

if textLength == 0:
    print('string is empty')
else:
    middle_characters = ''
              
    if textLength%2 != 0:
        middle_characters = text[textLength // 2]
    else:
        middle_characters = text[textLength // 2 - 1 : textLength // 2 + 1]

    print(middle_characters)
