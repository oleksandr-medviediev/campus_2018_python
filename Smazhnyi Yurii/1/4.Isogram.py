str = input("input your string: ")

isogram = True

for i in range(len(str) - 1):
    if(i == ' '):
        pass
    elif(i == '-'):
        pass
    elif(str[i] == str[i+1]):
        isogram = False
        break

print(isogram)