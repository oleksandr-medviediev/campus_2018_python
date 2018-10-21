shift = int(input("input shift: "))
string = input("input your string: ")

newString = ""

for i in range(len(string)):
    intValue = ord(string[i])
    intValue += shift
    newString += chr(intValue)

print(newString)
