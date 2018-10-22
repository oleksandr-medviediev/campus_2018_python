inStr = str(input())
size = len(inStr)

outStr = inStr[size // 2]
if size % 2 == False:
    outStr = inStr[size // 2 - 1] + outStr
print(outStr)