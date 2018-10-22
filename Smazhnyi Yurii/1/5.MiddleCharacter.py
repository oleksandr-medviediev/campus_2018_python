string = input("input your string: ")

strLen = len(string)

if strLen != 0:
    isEven = strLen % 2 == 0
    index = strLen // 2

    if isEven: 
        print(string[index - 1] + string[index])

    else:
        print(string[index])
