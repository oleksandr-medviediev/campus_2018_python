my_str = input("type string: ")

counters = {}

is_isogram = True

for char in my_str:
    if char in counters:
        counters[char] = counters[char] + 1

        if counters[char] > 1:
            is_isogram = False
            break

    else:
        counters[char] = 1

print(is_isogram)