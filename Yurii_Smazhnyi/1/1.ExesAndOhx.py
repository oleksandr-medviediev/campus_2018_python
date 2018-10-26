string = input("input your string: ")
x_сount = 0
o_сount = 0

for i in string:
    if i == 'x':
        x_сount += 1
    elif i == 'o':
        o_сount += 1

print(x_сount == o_сount)
