inStr = str(input())
ansver = "True"

for i in range(len(inStr)):
    if inStr[i].isalpha() and inStr.count(inStr[i], i,) != 1:
        ansver = "False"
        break

print(ansver)
