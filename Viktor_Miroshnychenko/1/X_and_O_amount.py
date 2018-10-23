x_amount = 0
o_amount = 0

string = input("Enter string to compare amount of 'x' and 'o'\n")

for char in string:
    if char == 'x':
        x_amount += 1
    elif char == 'o':
        o_amount += 1
    else:
        continue

print(x_amount == o_amount)
