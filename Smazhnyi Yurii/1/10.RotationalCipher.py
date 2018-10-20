import re
shift = int(input("input shift: "))
s = input("input your string: ")

newString = ""

for i in range(len(s)):
    intValue = ord(s[i])
    intValue += shift
    newString += chr(intValue)

print(newString)