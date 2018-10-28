num = int(input())
inStr = str(input())

outStr = ''
for ch in inStr:
    outStr += chr((ord(ch) - ord('a') + num) % 26 + ord('a'))

print(outStr)