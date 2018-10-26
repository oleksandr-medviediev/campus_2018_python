key = input('key: ')
key = int(key)

s = input('string: ')

rotatedString = ''

for char in s:
    if char.isalpha():
        rotatedString += chr(ord(char) + key)
    else:
        rotatedString += chr(int(char) + key)

print(rotatedString)
