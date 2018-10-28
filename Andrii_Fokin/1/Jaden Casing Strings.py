incomingStr = str(input())

outStr = ''
for word in incomingStr.split():
    outStr += word.capitalize() + ' '

print(outStr)