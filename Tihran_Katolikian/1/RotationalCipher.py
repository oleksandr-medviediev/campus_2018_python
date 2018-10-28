key = input('Key: ')
key = int(key)

s = input('String: ')

rotatedString = ''

for char in s:
    if char.isalpha():
        rotatedString += chr(ord(char) + key)
    else:
        rotatedString += str((int(char) + key) % 10)

print(rotatedString)
