string = input('enter the string\n')

list = string.split()

for i in range(len(list)):
    list[i] = list[i].capitalize()

    
string = " ".join(list)
print(string)
