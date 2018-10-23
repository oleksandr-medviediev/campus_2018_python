import math

s = input('Enter a string: ')

if len(s) == 0:
    # nothing to print
    pass
else:
    if len(s) % 2 == 0:
        rightMiddleIndex = int(len(s) / 2)
        print(s[rightMiddleIndex - 1:rightMiddleIndex + 1])
    else:
        print(s[math.floor(len(s) / 2)])
