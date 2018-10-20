str = input("input your string: ")

listStr = list(str.split())

output = ""

for i in listStr:
    output += (i.capitalize()) + " "

print(output)