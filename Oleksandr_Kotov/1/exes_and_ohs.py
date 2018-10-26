my_str = input("type string: ")

my_str = my_str.lower()

o_count = 0
x_count = 0

for char in my_str:
    if char == 'x':
        x_count += 1

    elif char == 'o':
        o_count += 1

print(x_count == o_count)