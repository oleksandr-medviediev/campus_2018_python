inStr = str(input())

answer = 'True' 
for char in inStr:
    if char.isdigit() == False or int(char) > 4:
        answer = 'False'
        break

print(answer)