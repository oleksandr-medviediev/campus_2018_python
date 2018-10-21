string = input("input your string: ")

isogram = True

for i in range(len(string) - 1):
    if(i == ' '):
        pass
    elif(i == '-'):
        pass
    elif(string[i] == string[i+1]):
        isogram = False
        break

print(isogram)
