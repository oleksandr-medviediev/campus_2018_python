string = input("input your string: ")

list_str = list(string.split())

output = ""

for i in list_str:
    output += (i.capitalize()) + " "

print(output)
