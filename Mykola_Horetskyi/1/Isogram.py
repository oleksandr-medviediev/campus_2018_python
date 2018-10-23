text = input('input text:\n')

isIsogram = True

text = text.lower()

for character in text:
    if character == ' ' or character == '-':
        continue

    if text.count(character) != 1:
        isIsogram = False
        break

print(isIsogram)
        
    

