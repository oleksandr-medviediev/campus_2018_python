key = int(input("Input the key from 2 to 25:\n"))

inp = input("Input the text to code:\n")

 
key = 25 if key > 25 else key
key = 2 if key < 2 else key

result = ""

for char in inp:
    if char.isalpha():
        result += chr(ord(char) + key)
    else:
        result += chr(int(char) + key)

print(result)

input()
