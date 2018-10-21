x_amount = 0
o_amount = 0

string = input("Enter string to compare amount of 'x' and 'o'\n")

for iter in range(len(string)):
    if string[iter] == 'x':
        x_amount += 1
    elif string[iter] == 'o':
        o_amount += 1
    else:
        continue

if x_amount == o_amount:
    print(True)
else:
    print(False)
