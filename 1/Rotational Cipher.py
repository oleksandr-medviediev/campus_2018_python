key = int(input("Input the key from 2 to 25:\n"))

inp = input("Input the text to code:\n")

 
key = 25 if key > 25 else key
key = 2 if key < 2 else key

result = ""

for letter in inp:
	if letter.isalpha():
		num = ord(letter)
		if (num + key) > 122: 
			x = (num + key) - 122
			result += chr(x + ord('a') - 1)
		elif((num + key <= 122)):
			result += chr(num + key)
	else:
		result += letter
print(result)

input()
