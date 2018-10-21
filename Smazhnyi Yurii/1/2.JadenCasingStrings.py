string = input("input your string: ")

listStr = list(string.split())

output = ""

for i in listStr:
    output += (i.capitalize()) + " "

print(output)
