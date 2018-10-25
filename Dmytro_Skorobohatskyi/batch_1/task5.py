string = input('enter the string\n')

length = len(string)
if length <= 2:
    middle_chars = string
elif length % 2 == 1:
    middle_chars = string[length // 2]
else:
    middle = length // 2
    middle_chars = string[middle - 1:middle + 1]

print(middle_chars)
