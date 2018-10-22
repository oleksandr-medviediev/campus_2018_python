string = input("input your string: ")
xCount = 0
oCount = 0

for i in string:
    if i == 'x':
        xCount += 1
    elif i == 'o':
        oCount += 1

print(xCount == oCount)
