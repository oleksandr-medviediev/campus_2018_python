str = input('enter the string\n')

length = len(str)
if length <= 2:
    middle_chars = str
elif length % 2 == 1:
    middle_chars = str[length // 2]
else:
    middle = length // 2
    middle_chars = str[middle - 1:middle + 1]

print(middle_chars)

    
