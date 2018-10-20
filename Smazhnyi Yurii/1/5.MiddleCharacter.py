str = input("input your string: ")

strLen = len(str)

if strLen != 0:
    isEven = strLen % 2 == 0
    index = strLen // 2

    if isEven: 
        print(str[index - 1] + str[index])

    else:
        print(str[index])